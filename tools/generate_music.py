#!/usr/bin/env python3
"""
The Human Baseline - Dynamic BGM Soundtrack Generator.
Synthesizes 9 original, cinematic act-specific background music tracks
matching the socio-economic narrative arc of the visual novel.
Outputs loopable 44.1kHz stereo Vorbis (.ogg) files under assets/audio/music/.
"""

import os
import sys
import math
import numpy as np
from scipy import signal
from scipy.io import wavfile
import subprocess

SAMPLE_RATE = 44100

def note_to_freq(note_name_or_midi):
    if isinstance(note_name_or_midi, (int, float)):
        return 440.0 * (2.0 ** ((note_name_or_midi - 69) / 12.0))
    # Parse note like "C4", "F#3", "Bb2"
    name = note_name_or_midi.upper().strip()
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    flats = {"DB": "C#", "EB": "D#", "GB": "F#", "AB": "G#", "BB": "A#"}
    
    if len(name) >= 3 and name[:2] in flats:
        pitch = flats[name[:2]]
        octave = int(name[2:])
    elif len(name) >= 2 and name[1] == '#':
        pitch = name[:2]
        octave = int(name[2:])
    else:
        pitch = name[0]
        octave = int(name[1:])
    midi = 12 * (octave + 1) + notes.index(pitch)
    return 440.0 * (2.0 ** ((midi - 69) / 12.0))

class SynthEngine:
    def __init__(self, sample_rate=SAMPLE_RATE):
        self.sr = sample_rate

    def create_reverb(self, audio, room_size=0.6, damp=0.4, mix=0.35):
        """High-quality synthetic stereo convolution reverb."""
        decay_time = room_size * 2.5
        ir_len = int(self.sr * decay_time)
        t = np.linspace(0, decay_time, ir_len)
        
        # Exponential decay with low-pass filtering
        noise_l = np.random.normal(0, 1, ir_len) * np.exp(-3.0 * t / (decay_time * (1.0 - damp * 0.5)))
        noise_r = np.random.normal(0, 1, ir_len) * np.exp(-3.0 * t / (decay_time * (1.0 - damp * 0.5)))
        
        # Early reflections
        for delay_ms, amp in [(18, 0.6), (31, 0.45), (47, 0.35), (63, 0.25)]:
            idx = int(self.sr * delay_ms / 1000.0)
            if idx < ir_len:
                noise_l[idx] += amp
                noise_r[idx] += amp * 0.8
                
        # Lowpass filter the IR
        b, a = signal.butter(2, 4500.0 / (self.sr / 2.0), btype='low')
        ir_l = signal.lfilter(b, a, noise_l)
        ir_r = signal.lfilter(b, a, noise_r)
        
        # Convolve (using FFT)
        rev_l = signal.fftconvolve(audio[:, 0], ir_l)[:len(audio)]
        rev_r = signal.fftconvolve(audio[:, 1], ir_r)[:len(audio)]
        
        # Normalize reverb component
        max_rev = max(np.max(np.abs(rev_l)), np.max(np.abs(rev_r)), 1e-6)
        rev_l = (rev_l / max_rev) * np.max(np.abs(audio[:, 0]))
        rev_r = (rev_r / max_rev) * np.max(np.abs(audio[:, 1]))
        
        out_l = (1.0 - mix) * audio[:, 0] + mix * rev_l
        out_r = (1.0 - mix) * audio[:, 1] + mix * rev_r
        return np.column_stack([out_l, out_r])

    def render_pluck(self, freq, duration, velocity=0.8, pan=0.0):
        """Karplus-Strong physical modeling of plucked acoustic string."""
        n_samples = int(self.sr * duration)
        buf_len = max(2, int(round(self.sr / freq)))
        
        # Excitation noise burst shaped with lowpass
        excitation = np.random.uniform(-1, 1, buf_len)
        decay_factor = 0.992 - (0.00008 * freq)
        decay_factor = max(0.96, min(0.996, decay_factor))
        
        buf = np.copy(excitation)
        output = np.zeros(n_samples)
        
        # One-pole Karplus-Strong loop
        idx = 0
        prev = 0.0
        for i in range(n_samples):
            current = buf[idx]
            filtered = 0.5 * (current + prev) * decay_factor
            prev = current
            buf[idx] = filtered
            output[i] = current
            idx = (idx + 1) % buf_len
            
        # Velocity and envelope fade-out at end to prevent clicks
        env_tail = int(min(n_samples * 0.05, 500))
        output[-env_tail:] *= np.linspace(1.0, 0.0, env_tail)
        output *= velocity
        
        # Panning (-1.0 to 1.0)
        pan_l = math.cos((pan + 1.0) * math.pi / 4.0)
        pan_r = math.sin((pan + 1.0) * math.pi / 4.0)
        return np.column_stack([output * pan_l, output * pan_r])

    def render_rhodes(self, freq, duration, velocity=0.7, pan=0.0):
        """Warm Rhodes electric piano tine synthesis."""
        t = np.linspace(0, duration, int(self.sr * duration), endpoint=False)
        
        # Envelopes
        env_body = np.exp(-t * (1.8 + freq * 0.002))
        env_tine = np.exp(-t * 28.0) * 0.35
        env_bell = np.exp(-t * 12.0) * 0.25
        
        # Harmonics
        f1 = np.sin(2 * np.pi * freq * t) * env_body
        f2 = np.sin(2 * np.pi * freq * 2.0 * t) * env_body * 0.45
        f3 = np.sin(2 * np.pi * freq * 3.0 * t) * env_body * 0.15
        tine = np.sin(2 * np.pi * freq * 7.05 * t) * env_tine
        bell = np.sin(2 * np.pi * freq * 4.02 * t) * env_bell
        
        raw = (f1 + f2 + f3 + tine + bell) * velocity
        # Gentle tape saturation
        saturated = np.tanh(raw * 1.3)
        
        # Stereo tremolo (3.2 Hz)
        tremolo = 0.85 + 0.15 * np.sin(2 * np.pi * 3.2 * t)
        
        pan_l = math.cos((pan + 1.0) * math.pi / 4.0) * tremolo
        pan_r = math.sin((pan + 1.0) * math.pi / 4.0) * (2.0 - tremolo)
        return np.column_stack([saturated * pan_l, saturated * pan_r])

    def render_pad(self, chord_freqs, duration, velocity=0.4, cutoff=1200.0):
        """Lush warm analog string/pad synth with detuned oscillators and filter sweep."""
        t = np.linspace(0, duration, int(self.sr * duration), endpoint=False)
        total_l = np.zeros(len(t))
        total_r = np.zeros(len(t))
        
        # ADSR Envelope: gentle swell and release
        attack_len = int(self.sr * min(1.8, duration * 0.3))
        release_len = int(self.sr * min(2.2, duration * 0.35))
        sustain_len = len(t) - attack_len - release_len
        
        env = np.concatenate([
            np.linspace(0.0, 1.0, attack_len),
            np.ones(max(0, sustain_len)),
            np.linspace(1.0, 0.0, release_len)
        ])
        if len(env) < len(t):
            env = np.pad(env, (0, len(t) - len(env)))
        else:
            env = env[:len(t)]
            
        for f in chord_freqs:
            # 3 slightly detuned oscillators per note for lush chorus width
            f_center = f
            f_detune1 = f * 1.003
            f_detune2 = f * 0.997
            
            # Band-limited sawtooth / sine blend
            saw1 = signal.sawtooth(2 * np.pi * f_center * t) * 0.4 + np.sin(2 * np.pi * f_center * t) * 0.6
            saw2 = signal.sawtooth(2 * np.pi * f_detune1 * t) * 0.5
            saw3 = signal.sawtooth(2 * np.pi * f_detune2 * t) * 0.5
            
            voice_l = (saw1 * 0.6 + saw2 * 0.5) * env
            voice_r = (saw1 * 0.6 + saw3 * 0.5) * env
            
            total_l += voice_l
            total_r += voice_r
            
        # Lowpass filter with subtle resonance
        norm_cutoff = max(100.0, min(self.sr * 0.45, cutoff)) / (self.sr / 2.0)
        b, a = signal.butter(3, norm_cutoff, btype='low')
        total_l = signal.lfilter(b, a, total_l)
        total_r = signal.lfilter(b, a, total_r)
        
        # Normalize and scale
        scale = velocity / max(len(chord_freqs), 1)
        return np.column_stack([total_l * scale, total_r * scale])

    def render_sub_bass(self, freq, duration, velocity=0.6):
        """Warm, deep sub-bass pulse."""
        t = np.linspace(0, duration, int(self.sr * duration), endpoint=False)
        env = np.exp(-t * 1.2)
        # Fundamental sine + subtle 2nd harmonic
        wave = np.sin(2 * np.pi * freq * t) * 0.85 + np.sin(2 * np.pi * 2.0 * freq * t) * 0.15
        sig = np.tanh(wave * 1.2) * env * velocity
        return np.column_stack([sig, sig])

    def render_heartbeat_pulse(self, duration=1.0, velocity=0.35, interval=0.28):
        """Authentic biological chest heartbeat sound (lub-dub).
        Deep, warm, low-frequency acoustic chest cavity thud with natural damping.
        """
        n_samples = int(self.sr * duration)
        out = np.zeros(n_samples)
        
        # S1 (lub): deep, rounded ventricular contraction
        len1 = int(self.sr * 0.18)
        t1 = np.linspace(0, 0.18, len1, endpoint=False)
        f1 = 56.0 * (1.12 - 0.32 * (t1 / 0.18))
        sine1 = np.sin(2 * np.pi * f1 * t1)
        env1 = (1.0 - np.exp(-t1 * 100.0)) * np.exp(-t1 * 18.0)
        noise1 = np.random.normal(0, 0.25, len1) * env1
        
        b, a = signal.butter(2, 95.0 / (self.sr / 2.0), btype='low')
        s1 = signal.lfilter(b, a, sine1 * env1 * 0.9 + noise1 * 0.2)
        out[:len1] += s1 * 0.9
        
        # S2 (dub): crisper semilunar valve closure at +0.28s
        offset = int(self.sr * interval)
        len2 = int(self.sr * 0.14)
        if offset + len2 < n_samples:
            t2 = np.linspace(0, 0.14, len2, endpoint=False)
            f2 = 68.0 * (1.15 - 0.28 * (t2 / 0.14))
            sine2 = np.sin(2 * np.pi * f2 * t2)
            env2 = (1.0 - np.exp(-t2 * 120.0)) * np.exp(-t2 * 24.0)
            noise2 = np.random.normal(0, 0.20, len2) * env2
            s2 = signal.lfilter(b, a, sine2 * env2 * 0.85 + noise2 * 0.18)
            out[offset:offset+len2] += s2 * 0.70
            
        scaled = out * velocity
        # Gentle stereo width (slightly left-biased like anatomical heart position)
        pan = -0.15
        pan_l = math.cos((pan + 1.0) * math.pi / 4.0)
        pan_r = math.sin((pan + 1.0) * math.pi / 4.0)
        return np.column_stack([scaled * pan_l, scaled * pan_r])

    def render_heartbeat_base_note(self, freq, duration, velocity=0.55, interval=0.28):
        """Musical base note keyed to the chord fundamental, articulated with
        the heartbeat rhythm (lub-dub pulse followed by warm harmonic sustain).
        """
        n_samples = int(self.sr * duration)
        t = np.linspace(0, duration, n_samples, endpoint=False)
        out = np.zeros(n_samples)
        
        # S1 base impulse
        len1 = int(self.sr * min(duration, 0.45))
        t1 = np.linspace(0, min(duration, 0.45), len1, endpoint=False)
        env1 = (1.0 - np.exp(-t1 * 60.0)) * np.exp(-t1 * 3.5)
        wave1 = np.sin(2 * np.pi * freq * t1) * 0.8 + np.sin(2 * np.pi * 2.0 * freq * t1) * 0.2
        out[:len1] += wave1 * env1 * 0.85
        
        # S2 base impulse at +interval
        offset = int(self.sr * interval)
        if offset < n_samples:
            rem_dur = duration - interval
            len2 = int(self.sr * rem_dur)
            t2 = np.linspace(0, rem_dur, len2, endpoint=False)
            env2 = (1.0 - np.exp(-t2 * 70.0)) * np.exp(-t2 * 2.0)
            wave2 = np.sin(2 * np.pi * freq * t2) * 0.85 + np.sin(2 * np.pi * 2.0 * freq * t2) * 0.15
            out[offset:offset+len2] += wave2 * env2 * 0.65
            
        # Subtle sub-bass body sustain
        body_env = (1.0 - np.exp(-t * 20.0)) * np.exp(-t * 1.2) * 0.35
        body_wave = np.sin(2 * np.pi * (freq * 0.5) * t)
        out += body_wave * body_env
        
        sig = np.tanh(out * 1.1) * velocity
        return np.column_stack([sig, sig])

def add_clip(target_track, clip, start_sample):
    """Mix a stereo clip into the target track buffer."""
    clip_len = len(clip)
    end_sample = start_sample + clip_len
    target_len = len(target_track)
    
    if start_sample >= target_len:
        return
    if end_sample > target_len:
        clip = clip[:target_len - start_sample]
        end_sample = target_len
        
    target_track[start_sample:end_sample] += clip

def render_track_to_ogg(track_audio, output_ogg_path, synth_engine):
    """Applies master compression, reverb, normalization, and encodes to OGG."""
    # Apply master stereo reverb
    wet = synth_engine.create_reverb(track_audio, room_size=0.65, damp=0.35, mix=0.28)
    
    # Peak normalization to -1.0 dB
    peak = np.max(np.abs(wet))
    if peak > 0:
        normalized = (wet / peak) * 0.89
    else:
        normalized = wet
        
    # Temporary WAV output
    temp_wav = output_ogg_path.replace(".ogg", ".temp.wav")
    int_audio = (normalized * 32767.0).astype(np.int16)
    wavfile.write(temp_wav, SAMPLE_RATE, int_audio)
    
    # Encode with ffmpeg to high quality 128k Vorbis OGG
    cmd = [
        "ffmpeg", "-y", "-i", temp_wav,
        "-c:a", "libvorbis", "-q:a", "4",
        output_ogg_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
    print(f"Generated: {output_ogg_path} ({len(track_audio)/SAMPLE_RATE:.1f}s)")

# ==============================================================================
# ACT MUSIC COMPOSITIONS
# ==============================================================================

def compose_act1_warm_engine(synth, duration=48.0):
    """Act I: The Warm Engine (Year 0) - Hopeful, rhythmic, acoustic warmth."""
    bpm = 84.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Dmaj9 -> Gmaj7 -> Bm7 -> A(add9)
    chords = [
        ["D3", "A3", "F#4", "C#5"],
        ["G2", "B3", "D4", "F#4"],
        ["B2", "F#3", "D4", "A4"],
        ["A2", "E3", "C#4", "B4"]
    ]
    
    chord_dur = 4 * beat_dur # 1 bar per chord
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Pad bed
        pad = synth.render_pad(chord_freqs, chord_dur * 1.15, velocity=0.22, cutoff=1400.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Sub bass root on downbeat
        bass = synth.render_sub_bass(chord_freqs[0] * 0.5, chord_dur * 0.9, velocity=0.45)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Acoustic pluck pattern (arpeggiated)
        for step in range(8): # eighth notes
            t_note = curr_time + step * (beat_dur / 2.0)
            if t_note >= duration:
                break
            # Fingerpicking pattern
            pick_note_idx = [0, 2, 1, 3, 2, 1, 3, 2][step]
            f = chord_freqs[pick_note_idx]
            pan = -0.4 if step % 2 == 0 else 0.4
            vel = 0.55 if step % 4 == 0 else 0.38
            pluck = synth.render_pluck(f, beat_dur * 1.8, velocity=vel, pan=pan)
            add_clip(master, pluck, int(t_note * SAMPLE_RATE))
            
            # Subtle Rhodes tine accents on beats 2 and 4
            if step in [2, 6]:
                rhodes = synth.render_rhodes(chord_freqs[2] * 2.0, beat_dur * 1.5, velocity=0.35, pan=0.2)
                add_clip(master, rhodes, int(t_note * SAMPLE_RATE))
                
        curr_time += chord_dur
        
    return master

def compose_act2_first_tremors(synth, duration=48.0):
    """Act II: The First Tremors (Year 1) - Subtle tension, minor shifts, nervous curiosity."""
    bpm = 78.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Em9 -> Am7 -> Cmaj7 -> B7(b9)
    chords = [
        ["E2", "G3", "B3", "F#4"],
        ["A2", "E3", "G3", "C4"],
        ["C3", "G3", "B3", "E4"],
        ["B2", "F#3", "A3", "D#4"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Colder, slightly darker pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.1, velocity=0.24, cutoff=900.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Deep pulse bass
        bass = synth.render_sub_bass(chord_freqs[0], chord_dur * 0.85, velocity=0.5)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Tremolo Rhodes chords
        for b in range(4):
            t_beat = curr_time + b * beat_dur
            if t_beat >= duration:
                break
            if b in [0, 2]:
                rh = synth.render_rhodes(chord_freqs[1], beat_dur * 2.2, velocity=0.4, pan=-0.3)
                add_clip(master, rh, int(t_beat * SAMPLE_RATE))
                
            # Intermittent plucked acoustic harmonics
            if b in [1, 3]:
                plk = synth.render_pluck(chord_freqs[3], beat_dur * 1.5, velocity=0.42, pan=0.4)
                add_clip(master, plk, int((t_beat + beat_dur * 0.5) * SAMPLE_RATE))
                
        curr_time += chord_dur
    return master

def compose_act3_severed_ladder(synth, duration=48.0):
    """Act III: The Severed Ladder (Year 2) - Algorithmic fatigue, cognitive isolation, cold shimmer."""
    bpm = 72.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Cm9 -> Abmaj7 -> Ebmaj7 -> Gm7
    chords = [
        ["C3", "Eb3", "G3", "D4"],
        ["Ab2", "C3", "Eb3", "G4"],
        ["Eb3", "G3", "Bb3", "D4"],
        ["G2", "D3", "F3", "Bb3"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Dark filtered pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.2, velocity=0.22, cutoff=800.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Low drone bass
        bass = synth.render_sub_bass(chord_freqs[0] * 0.5, chord_dur * 0.9, velocity=0.52)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Repetitive mechanical Rhodes arpeggio
        notes_pattern = [0, 2, 1, 3, 2, 3]
        for step, n_idx in enumerate(notes_pattern):
            t_note = curr_time + step * (beat_dur * 0.66)
            if t_note >= duration:
                break
            rh = synth.render_rhodes(chord_freqs[n_idx % len(chord_freqs)], beat_dur * 1.2, velocity=0.35, pan=(step % 2) * 0.5 - 0.25)
            add_clip(master, rh, int(t_note * SAMPLE_RATE))
            
        curr_time += chord_dur
    return master

def compose_act4_commuter_drain(synth, duration=48.0):
    """Act IV: The Commuter Drain (Year 3) - Nocturnal highway rain, deep exhaustion, low tempo."""
    bpm = 66.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Fm7 -> Dbmaj7 -> Bbm9 -> C7(b9)
    chords = [
        ["F2", "C3", "Ab3", "Eb4"],
        ["Db3", "Ab3", "C4", "F4"],
        ["Bb2", "F3", "Ab3", "C4"],
        ["C3", "G3", "Bb3", "E4"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Moody ambient swell
        pad = synth.render_pad(chord_freqs, chord_dur * 1.15, velocity=0.25, cutoff=650.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Heavy slow sub-bass
        bass = synth.render_sub_bass(chord_freqs[0], chord_dur * 0.95, velocity=0.6)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Soft Rhodes rain drops
        for step in [0, 1.5, 2.5, 3.2]:
            t_note = curr_time + step * beat_dur
            if t_note >= duration:
                break
            rh = synth.render_rhodes(chord_freqs[2] * 1.5, beat_dur * 1.6, velocity=0.32, pan=-0.2)
            add_clip(master, rh, int(t_note * SAMPLE_RATE))
            
        curr_time += chord_dur
    return master

def compose_act5_middle_age_squeeze(synth, duration=48.0):
    """Act V: The Middle-Age Squeeze (Year 4) - Somber economic grit, stoic family burden."""
    bpm = 64.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Bm(add9) -> Gmaj7 -> D/F# -> Em9
    chords = [
        ["B2", "F#3", "D4", "C#5"],
        ["G2", "D3", "B3", "F#4"],
        ["F#2", "C#3", "A3", "D4"],
        ["E2", "B2", "G3", "D4"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Somber acoustic strings bed
        pad = synth.render_pad(chord_freqs, chord_dur * 1.2, velocity=0.20, cutoff=1100.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Slow resonant pluck bass
        bass = synth.render_pluck(chord_freqs[0], chord_dur * 0.9, velocity=0.65, pan=0.0)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Resonant guitar arpeggio
        for i, f in enumerate(chord_freqs[1:]):
            t_note = curr_time + (i + 1) * (beat_dur * 0.85)
            if t_note >= duration:
                break
            plk = synth.render_pluck(f, beat_dur * 2.2, velocity=0.48, pan=0.35)
            add_clip(master, plk, int(t_note * SAMPLE_RATE))
            
        curr_time += chord_dur
    return master

def compose_act6_caregiving_crucible(synth, duration=48.0):
    """Act VI: The Great Caregiving Crucible (Year 5) - Clinical fragility, tenderness, quiet sorrow."""
    bpm = 60.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Am9 -> Fmaj7(#11) -> Cmaj9 -> G6
    chords = [
        ["A2", "E3", "C4", "B4"],
        ["F2", "C3", "E4", "B4"],
        ["C3", "G3", "E4", "D5"],
        ["G2", "D3", "B3", "E4"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Soft, breathing pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.3, velocity=0.18, cutoff=750.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Sparse, crystal-clear high bell-piano notes
        for b in [0, 2]:
            t_note = curr_time + b * beat_dur
            if t_note >= duration:
                break
            f = chord_freqs[3] if b == 0 else chord_freqs[2]
            rh = synth.render_rhodes(f, beat_dur * 2.8, velocity=0.38, pan=0.0)
            add_clip(master, rh, int(t_note * SAMPLE_RATE))
            
        # Distant low octave support
        bass = synth.render_sub_bass(chord_freqs[0], chord_dur * 0.8, velocity=0.4)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        curr_time += chord_dur
    return master

def compose_act7_breaking_point(synth, duration=48.0):
    """Act VII: The Breaking Point (Year 6) - Picket line fire, defiance, steady marching momentum."""
    bpm = 92.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Em -> D -> C -> Bm (steady rising march)
    chords = [
        ["E2", "B2", "G3", "E4"],
        ["D2", "A2", "F#3", "D4"],
        ["C2", "G2", "E3", "C4"],
        ["B1", "F#2", "D3", "B3"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Tense, gritty analog pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.05, velocity=0.28, cutoff=1600.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Driving quarter-note bass march
        for beat in range(4):
            t_beat = curr_time + beat * beat_dur
            if t_beat >= duration:
                break
            bass = synth.render_sub_bass(chord_freqs[0], beat_dur * 0.75, velocity=0.6)
            add_clip(master, bass, int(t_beat * SAMPLE_RATE))
            
            # Percussive acoustic strums on beats 2 and 4
            if beat in [1, 3]:
                for f in chord_freqs[1:]:
                    plk = synth.render_pluck(f, beat_dur * 0.9, velocity=0.48, pan=(beat - 2) * 0.3)
                    add_clip(master, plk, int(t_beat * SAMPLE_RATE))
                    
        curr_time += chord_dur
    return master

def compose_act8_thirty_second_hour(synth, duration=48.0):
    """Act VIII: The 32nd Hour (Year 7) - Quiet solidarity, morning light, renewed determination."""
    bpm = 80.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Gmaj7 -> Em9 -> Cmaj9 -> D(add9)
    chords = [
        ["G2", "D3", "B3", "F#4"],
        ["E2", "B2", "G3", "D4"],
        ["C3", "G3", "E4", "B4"],
        ["D3", "A3", "F#4", "E5"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Warm golden pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.15, velocity=0.24, cutoff=1300.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Grounded bass
        bass = synth.render_sub_bass(chord_freqs[0], chord_dur * 0.9, velocity=0.48)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        # Dual acoustic picking
        for step in range(8):
            t_note = curr_time + step * (beat_dur / 2.0)
            if t_note >= duration:
                break
            idx = [0, 1, 2, 3, 2, 1, 2, 3][step]
            f = chord_freqs[idx]
            pan = -0.35 if step % 2 == 0 else 0.35
            plk = synth.render_pluck(f, beat_dur * 1.5, velocity=0.42, pan=pan)
            add_clip(master, plk, int(t_note * SAMPLE_RATE))
            
        curr_time += chord_dur
    return master

def compose_act9_human_baseline(synth, duration=48.0):
    """Act IX: The Human Baseline (Year 8) - Triumphant catharsis, enduring dignity, full resolution."""
    bpm = 76.0
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # Progression: Dmaj7 -> A/C# -> Bm7 -> Gmaj7(add9)
    chords = [
        ["D3", "A3", "F#4", "C#5"],
        ["C#3", "A3", "E4", "A4"],
        ["B2", "F#3", "D4", "A4"],
        ["G2", "D3", "B3", "A4"]
    ]
    chord_dur = 4 * beat_dur
    n_chords = len(chords)
    
    curr_time = 0.0
    while curr_time < duration:
        bar_idx = int(curr_time / chord_dur)
        chord = chords[bar_idx % n_chords]
        chord_freqs = [note_to_freq(n) for n in chord]
        
        # Rich, warm, expansive string pad
        pad = synth.render_pad(chord_freqs, chord_dur * 1.2, velocity=0.26, cutoff=1800.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Warm acoustic guitar picking
        for step in range(8):
            t_note = curr_time + step * (beat_dur / 2.0)
            if t_note >= duration:
                break
            f = chord_freqs[[0, 2, 1, 3, 2, 1, 3, 2][step]]
            plk = synth.render_pluck(f, beat_dur * 1.6, velocity=0.45, pan=-0.3 if step % 2 == 0 else 0.3)
            add_clip(master, plk, int(t_note * SAMPLE_RATE))
            
        # Gentle chime / Rhodes accents
        for b in [0, 2]:
            t_b = curr_time + b * beat_dur
            if t_b >= duration:
                break
            rh = synth.render_rhodes(chord_freqs[3] * 1.0, beat_dur * 2.0, velocity=0.36, pan=0.0)
            add_clip(master, rh, int(t_b * SAMPLE_RATE))
            
        # Grounded bass
        bass = synth.render_sub_bass(chord_freqs[0] * 0.5, chord_dur * 0.9, velocity=0.5)
        add_clip(master, bass, int(curr_time * SAMPLE_RATE))
        
        curr_time += chord_dur
    return master

def compose_title_human_baseline(synth, duration=48.0):
    """Title Theme: The Human Baseline
    Poignant, warm, resilient. Anchored by a resting heartbeat pulse (~60 BPM)
    functioning as both the organic rhythmic foundation and the musical base note.
    """
    bpm = 60.0  # 1 beat per second = human resting heart rate
    beat_dur = 60.0 / bpm
    total_samples = int(SAMPLE_RATE * duration)
    master = np.zeros((total_samples, 2))
    
    # 12 bars (4 seconds per bar at 60 BPM) = 48.0s
    progression = [
        {"chord": ["D3", "A3", "F#4", "C#5", "E5"], "root": "D2", "bars": 2},
        {"chord": ["B2", "F#3", "D4", "A4", "C#5"],  "root": "B1", "bars": 2},
        {"chord": ["G2", "D3", "B3", "F#4", "D5"],   "root": "G1", "bars": 2},
        {"chord": ["A2", "E3", "A3", "D4", "B4"],    "root": "A1", "bars": 2},
        {"chord": ["F#2", "C#3", "A3", "E4", "C#5"], "root": "F#1", "bars": 2},
        {"chord": ["G2", "B3", "D4", "F#4", "A4"],   "root": "D2", "bars": 2},
    ]
    
    # 1. Layer the underlying biological heartbeat pulse continuously throughout
    # Resting heart rate: exactly every 1.0 second (60 BPM)
    num_beats = int(duration / beat_dur)
    for b in range(num_beats):
        t_beat = b * beat_dur
        # Dynamic variation: slightly stronger on downbeats (b % 4 == 0 or 2), softer on offbeats
        if b % 4 == 0:
            v_hb = 0.38
        elif b % 2 == 0:
            v_hb = 0.32
        else:
            v_hb = 0.26
        hb = synth.render_heartbeat_pulse(duration=1.0, velocity=v_hb, interval=0.28)
        add_clip(master, hb, int(t_beat * SAMPLE_RATE))
        
    # 2. Render each chord section
    curr_time = 0.0
    for section in progression:
        chord_names = section["chord"]
        root_name = section["root"]
        bars = section["bars"]
        sec_dur = bars * 4.0 * beat_dur
        
        chord_freqs = [note_to_freq(n) for n in chord_names]
        root_freq = note_to_freq(root_name)
        
        # Warm analog pad swell across the section
        pad = synth.render_pad(chord_freqs, sec_dur, velocity=0.38, cutoff=1100.0)
        add_clip(master, pad, int(curr_time * SAMPLE_RATE))
        
        # Heartbeat Base Note: triggers on beat 1 and beat 3 of each bar
        for bar in range(bars):
            t_bar = curr_time + bar * 4.0 * beat_dur
            # Beat 1 (root note)
            b1 = synth.render_heartbeat_base_note(root_freq, 2.0 * beat_dur, velocity=0.58)
            add_clip(master, b1, int(t_bar * SAMPLE_RATE))
            # Beat 3 (fifth or root)
            fifth_freq = root_freq * 1.5
            b3 = synth.render_heartbeat_base_note(fifth_freq if bar % 2 == 1 else root_freq, 2.0 * beat_dur, velocity=0.48)
            add_clip(master, b3, int((t_bar + 2.0 * beat_dur) * SAMPLE_RATE))
            
            # Rhodes tine chords on beat 1 & 3
            rh1 = synth.render_rhodes(chord_freqs[2], 2.8, velocity=0.42, pan=-0.2)
            add_clip(master, rh1, int(t_bar * SAMPLE_RATE))
            rh2 = synth.render_rhodes(chord_freqs[3], 2.4, velocity=0.36, pan=0.2)
            add_clip(master, rh2, int((t_bar + 2.0 * beat_dur) * SAMPLE_RATE))
            
            # Acoustic picking pattern (8 fingerpicked notes per bar, 0.5s per note)
            picking_pattern = [0, 2, 1, 3, 2, 4, 3, 1]
            for step, pick_idx in enumerate(picking_pattern):
                t_pick = t_bar + step * 0.5 * beat_dur
                if t_pick >= duration:
                    break
                f_pick = chord_freqs[pick_idx % len(chord_freqs)]
                # Humanize velocity slightly
                v_pick = 0.44 + 0.08 * math.sin(step * 1.2)
                pan_pick = -0.35 if step % 2 == 0 else 0.35
                plk = synth.render_pluck(f_pick, 1.4, velocity=v_pick, pan=pan_pick)
                add_clip(master, plk, int(t_pick * SAMPLE_RATE))
                
        curr_time += sec_dur
        
    return master

# ==============================================================================
# MAIN GENERATOR
# ==============================================================================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    music_dir = os.path.join(project_root, "app", "src", "main", "assets", "audio", "music")
    os.makedirs(music_dir, exist_ok=True)
    
    synth = SynthEngine(SAMPLE_RATE)
    
    tracks = [
        ("bgm_title.ogg", compose_title_human_baseline, 48.0),
        ("bgm_act1_warm_engine.ogg", compose_act1_warm_engine, 46.0),
        ("bgm_act2_first_tremors.ogg", compose_act2_first_tremors, 46.0),
        ("bgm_act3_severed_ladder.ogg", compose_act3_severed_ladder, 46.0),
        ("bgm_act4_commuter_drain.ogg", compose_act4_commuter_drain, 46.0),
        ("bgm_act5_middle_age_squeeze.ogg", compose_act5_middle_age_squeeze, 46.0),
        ("bgm_act6_caregiving_crucible.ogg", compose_act6_caregiving_crucible, 46.0),
        ("bgm_act7_breaking_point.ogg", compose_act7_breaking_point, 46.0),
        ("bgm_act8_thirty_second_hour.ogg", compose_act8_thirty_second_hour, 46.0),
        ("bgm_act9_human_baseline.ogg", compose_act9_human_baseline, 46.0),
    ]
    
    # Filter if arguments passed
    if len(sys.argv) > 1:
        wanted = sys.argv[1:]
        tracks = [t for t in tracks if any(w in t[0] for w in wanted)]
        
    print(f"Generating Soundtrack into {music_dir}...")
    for filename, composer_fn, duration in tracks:
        out_path = os.path.join(music_dir, filename)
        print(f"Synthesizing {filename} ({duration:.1f}s)...")
        raw_audio = composer_fn(synth, duration=duration)
        render_track_to_ogg(raw_audio, out_path, synth)
        
    print("\nSoundtrack generated successfully!")

if __name__ == "__main__":
    main()
