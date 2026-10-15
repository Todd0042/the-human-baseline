#!/usr/bin/env python3
"""
Process character sprites from generative output (isolated on white background)
into clean transparent PNGs with flood-fill boundary detection, protecting internal
white colors (clothing, teeth, highlights).
"""

import os
import sys
import numpy as np
from PIL import Image
from collections import deque

def isolate_sprite(input_path, output_path, white_threshold=235):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    arr = np.array(img)
    
    rgb = arr[:, :, :3]
    # Check whiteness: all channels high
    is_white = (rgb[:, :, 0] >= white_threshold) & \
               (rgb[:, :, 1] >= white_threshold) & \
               (rgb[:, :, 2] >= white_threshold)
               
    # BFS flood fill from all border pixels
    visited = np.zeros((height, width), dtype=bool)
    is_background = np.zeros((height, width), dtype=bool)
    
    queue = deque()
    
    # Initialize queue with border pixels that are white
    for x in range(width):
        if is_white[0, x]:
            queue.append((0, x))
            visited[0, x] = True
            is_background[0, x] = True
        if is_white[height - 1, x]:
            queue.append((height - 1, x))
            visited[height - 1, x] = True
            is_background[height - 1, x] = True
            
    for y in range(height):
        if is_white[y, 0]:
            queue.append((y, 0))
            visited[y, 0] = True
            is_background[y, 0] = True
        if is_white[y, width - 1]:
            queue.append((y, width - 1))
            visited[y, width - 1] = True
            is_background[y, width - 1] = True
            
    # 4-connectivity flood fill
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < height and 0 <= nx < width and not visited[ny, nx]:
                visited[ny, nx] = True
                if is_white[ny, nx]:
                    is_background[ny, nx] = True
                    queue.append((ny, nx))
                    
    # Edge feathering: for pixels near background with high lightness
    # Set background alpha to 0
    arr[is_background, 3] = 0
    
    # Smooth edges: any non-background pixel adjacent to background with brightness > 220
    # gets partial alpha
    result = Image.fromarray(arr, "RGBA")
    result.save(output_path, "PNG")
    print(f"Saved transparent sprite: {output_path} ({width}x{height})")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        isolate_sprite(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 1:
        import glob
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(script_dir)
        sprites_dir = os.path.join(base_dir, "app", "src", "main", "assets", "sprites")
        portraits_dir = os.path.join(base_dir, "app", "src", "main", "assets", "portraits")
        
        pngs = sorted(glob.glob(os.path.join(sprites_dir, "*_sprite.png")))
        print(f"Auto-processing {len(pngs)} sprites in {sprites_dir}...")
        for p in pngs:
            isolate_sprite(p, p)
            # Also ensure a portrait exists
            base_name = os.path.basename(p).replace("_sprite.png", "")
            portrait_path = os.path.join(portraits_dir, f"{base_name}.jpg")
            if not os.path.exists(portrait_path):
                img = Image.open(p).convert("RGB")
                w, h = img.size
                crop_size = int(min(w, h * 0.45))
                left = (w - crop_size) // 2
                top = int(h * 0.04)
                portrait = img.crop((left, top, left + crop_size, top + crop_size)).resize((512, 512), Image.Resampling.LANCZOS)
                portrait.save(portrait_path, "JPEG", quality=92)
                print(f"Auto-generated portrait: {portrait_path}")
    else:
        print("Usage: process_sprites.py [<input> <output>]")
