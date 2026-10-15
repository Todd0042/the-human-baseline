# The Human Baseline: Master Character Sprite Generation Guide

This guide provides self-contained generative prompts for all 11 character sprites in *The Human Baseline*.

All sprites are designed in the grounded, cinematic 35mm film aesthetic, framed in vertical **9:16 aspect ratio** (~768x1376 px), and isolated against a **completely solid pure white background (`#FFFFFF`)** with no cast shadows and no floor.

---

## Processing Pipeline

1. **Generate**: Copy and paste any prompt into your image generator.
2. **Save**: Save the generated image directly to:
   ```
   app/src/main/assets/sprites/<character>_sprite.png
   ```
3. **Isolate Transparency**: Run the edge-connected BFS flood-fill script:
   ```bash
   python3 tools/process_sprites.py
   ```
   *This automatically converts the exterior white background into clean alpha transparency while protecting internal white clothing, badges, teeth, and highlights.*

---

## 1. Character Sprite Prompts

### 1. Todd (Lead Diagnostic Automotive Technician — Protagonist)
- **Target Path:** `app/src/main/assets/sprites/todd_sprite.png`
- **Staging:** Screen Left (angled slightly toward the right).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Todd, a handsome athletic mid-20s lead diagnostic automotive technician (age 24-28). Lean muscular build, sexy mid-length dark curly hair falling slightly across his forehead, light stubble along a sharp confident jawline, intelligent observant brown eyes with a subtle sardonic smirk, faint grease smudge on cheekbone. Wearing a navy blue mechanic service button-up shirt with sleeves rolled neatly up to mid-forearm, a clean white crew-neck undershirt visible at the open collar, dark charcoal durable work trousers, and scuffed brown leather work boots. Standing in a relaxed, confident three-quarter pose angled slightly to the right, hands loosely at his sides with a vintage chrome 10mm combination wrench held casually in his right hand. Grounded cinematic anime visual novel character art style, crisp clean outlines, refined digital painting, warm natural ambient workshop lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 2. Adriana (Retail Liquor Department Manager — Co-Lead)
- **Target Path:** `app/src/main/assets/sprites/adriana_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Adriana, a striking capable young woman in her mid-20s (age 24-28), retail liquor department manager. Sharp angular cheekbones, observant dark eyes with quiet resilience and dry humor, dark wavy hair pulled back into a neat practical braid with loose strands framing her face. Wearing a fitted black canvas retail department vest over an olive-drab thermal waffle-knit long-sleeve shirt, dark slim-fit work pants, and durable black slip-resistant work shoes. A retail store lanyard with keys and an employee badge clipped to her chest. Standing in an alert, grounded three-quarter pose angled slightly to the left, arms crossed comfortably across her chest or holding an inventory clip tally board. Grounded cinematic anime visual novel character art style, crisp clean outlines, refined digital painting, warm natural ambient lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 3. Pete (Master Diagnostic Technician & Shop Owner)
- **Target Path:** `app/src/main/assets/sprites/pete_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Pete, a 58-year-old weathered master automotive technician and independent garage owner. Stocky muscular build, salt-and-pepper hair, thick silver mustache, honest warm crinkled brown eyes, and deep laugh lines. Wearing a dark grey mechanic service shirt with an oval patch reading 'Pete' embroidered in red cursive over the chest pocket, dark work pants with grease wear, and heavy-duty steel-toe boots. Reading glasses rest on a black cord hanging around his neck. Standing in a sturdy, relaxed three-quarter pose angled slightly to the left, thumbs hooked loosely in his front belt loops. Grounded cinematic anime visual novel character art style, crisp clean outlines, detailed textile textures, warm natural lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 4. Marcus (Software Developer & Data Specialist)
- **Target Path:** `app/src/main/assets/sprites/marcus_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Marcus, an intelligent expressive young man in his mid-20s (age 24-28). Short faded dark hair, neatly trimmed light stubble, thoughtful weary yet earnest dark eyes behind modern matte-black wire-frame glasses. Wearing a heather-grey zip-up fleece hoodie over a dark graphic t-shirt, slim dark indigo denim jeans, and clean low-profile sneakers. Standing in a slightly hesitant three-quarter pose angled slightly to the left, one hand in his hoodie pocket and the other casually gesturing. Grounded cinematic anime visual novel character art style, crisp clean outlines, refined digital painting, natural soft lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 5. Diane Sterling (Lead Broadcast Television News Anchor)
- **Target Path:** `app/src/main/assets/sprites/news_anchor_sprite.png`
- **Staging:** Screen Right or Center (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Diane Sterling, a poised articulate television news anchor in her late 30s to early 40s (age 38-44). Shoulder-length dark chestnut hair in a neat professional broadcast blow-dry, calm authoritative hazel eyes, subtle realistic fine character lines around eyes, confident composed expression. Wearing a tailored deep burgundy suit blazer over a silk cream blouse, matching burgundy pencil skirt or trousers, and subtle silver earrings with a discreet black lavalier microphone clip on her left lapel. Standing in a dignified upright broadcast stance angled slightly to the left, holding a neat blue news briefing folder with both hands. Grounded cinematic anime visual novel character art style, crisp clean outlines, refined digital painting, soft balanced studio lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 6. Chloe (Registered Nurse — Cookout Friend)
- **Target Path:** `app/src/main/assets/sprites/chloe_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Chloe, a compassionate sharp 28-year-old registered nurse. Light brown wavy hair tied back in a secure surgical clip with loose strands, alert empathetic hazel eyes, gentle determined expression. Wearing fitted teal-blue hospital medical scrubs with a white and blue hospital ID badge reading 'CHLOE RN' clipped to her pocket, a clinical stethoscope draped securely around her neck, and comfortable supportive hospital nursing clogs. Standing in a warm approachable three-quarter pose angled slightly to the left, leaning lightly with hands clasped comfortably. Grounded cinematic anime visual novel character art style, crisp clean outlines, soft hospital ambient lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 7. Sam (Corporate Senior Auditor — Cookout Friend)
- **Target Path:** `app/src/main/assets/sprites/sam_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Sam, a 28-year-old pragmatic corporate auditor. Neatly parted light brown hair, clean-shaven, thoughtful blue-grey eyes behind classic round tortoiseshell reading glasses. Wearing a crisp sky-blue Oxford button-down collared dress shirt with sleeves rolled up to mid-forearm, charcoal tailored wool dress trousers, a brown leather belt, and polished brown leather oxfords. Standing in an observant three-quarter pose angled slightly to the left, holding a sleek black leather document portfolio under his arm. Grounded cinematic anime visual novel character art style, crisp clean outlines, refined fabric shading, soft office ambient lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 8. Kendra (College Student & Retail Sales Clerk)
- **Target Path:** `app/src/main/assets/sprites/kendra_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Kendra, an energetic 21-year-old college student and supermarket retail clerk. Curly voluminous dark hair tied up in a high messy ponytail with loose curls framing her face, expressive warm brown eyes, subtle silver nose stud, warm natural smile. Wearing an olive-green store polo shirt with an embroidered 'Oakridge KENDRA' name badge clipped to her chest, a woven fabric lanyard with register keys hanging around her neck, dark denim jeans, and worn black sneakers. Standing in an energetic, candid three-quarter pose angled slightly to the left, hands on her hips with youthful optimism. Grounded cinematic anime visual novel character art style, crisp clean outlines, commercial store ambient lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 9. Elena (Independent Gig Delivery Courier)
- **Target Path:** `app/src/main/assets/sprites/elena_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Elena, a hardworking 33-year-old Latina gig-delivery courier and mother. Dark wavy hair gathered in a quick practical ponytail, tired but intensely resilient dark eyes, faint freckles across an olive complexion. Wearing a black weatherproof fleece zip vest over a dark grey hooded sweatshirt, durable cargo joggers with utility pockets, and athletic running shoes. She wears a black lanyard branded 'Delivery App' around her neck and holds a modern smartphone in her left hand. Standing in a weary yet determined three-quarter pose angled slightly to the left. Grounded cinematic anime visual novel character art style, crisp clean outlines, authentic working-class textures, natural daylight, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 10. Senator Vance (State Senate Commerce Committee Chairman)
- **Target Path:** `app/src/main/assets/sprites/senator_vance_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Senator Vance, a distinguished 64-year-old state senator and committee chairman. Neatly combed silver hair, wire-rimmed glasses, piercing attentive grey eyes, dignified serious judicial expression. Wearing a tailored charcoal wool two-piece suit, crisp white dress shirt, deep burgundy silk necktie, and an enameled state senate lapel pin. Standing in an authoritative formal posture angled slightly to the left, one hand resting on a polished wooden podium rail. Grounded cinematic anime visual novel character art style, crisp clean outlines, rich architectural lighting, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```

---

### 11. Maya (Vocational Automotive Apprentice)
- **Target Path:** `app/src/main/assets/sprites/maya_sprite.png`
- **Staging:** Screen Right (angled slightly toward the left).
- **Prompt:**
```text
Full-body standing visual novel character sprite of Maya, a 20-year-old vocational automotive apprentice. Dark hair tucked beneath a backward black snapback shop cap, intense eager dark eyes with a smudge of grease along her temple, focused youthful expression. Wearing heavy-duty dark blue denim work bib overalls over a dark grey waffle-knit thermal shirt, mechanic work gloves tucked into the bib front pocket, and scuffed steel-toe work boots. Standing in an attentive three-quarter apprentice stance angled slightly to the left, holding an automotive analog multimeter testing probe. Grounded cinematic anime visual novel character art style, crisp clean outlines, warm garage trouble-light glow, isolated on a completely solid pure white background (#FFFFFF) with no cast shadows, no floor, and no background scenery. 9:16 vertical aspect ratio.
```
