<p align="center">
  <a href="https://ko-fi.com/todd0042">
    <img src="https://raw.githubusercontent.com/Todd0042/creator-assets/main/banners/todd_creator_banner_v1.0.png" alt="Support Todd on Ko-fi" width="100%" />
  </a>
</p>

---

# 🔧 The Human Baseline: An Audio-First Narrative of Working Life

[![Version](https://img.shields.io/badge/Version-1.5.1-ff2a85.svg)](https://github.com/Todd0042/the-human-baseline/releases)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-00f0ff.svg)](LICENSE)
[![Platform: Android 8.0+](https://img.shields.io/badge/Platform-Android%208.0%2B%20(API%2026%2B)-3DDC84.svg?logo=android&logoColor=white)](https://developer.android.com)
[![16 KB Page Size](https://img.shields.io/badge/16%20KB-Compatible-success.svg)](https://developer.android.com/16kb-page-size)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0.21-7F52FF.svg?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![UI: Jetpack Compose](https://img.shields.io/badge/UI-Jetpack%20Compose%202024.10.01-4285F4.svg?logo=jetpackcompose&logoColor=white)](https://developer.android.com/jetpack/compose)
[![Speech Synthesis: On-Device Multi-Voice](https://img.shields.io/badge/Speech%20Synthesis-On--Device%20Multi--Voice-orange.svg)](https://developer.android.com/reference/android/speech/tts/TextToSpeech)
[![Audio DSP: Dynamic Ducking](https://img.shields.io/badge/Audio%20DSP-Dynamic%20Ducking%20(-13.1dB)-green.svg)](app/src/main/java/com/voicerpg/engine/audio/MusicManager.kt)
[![NLP: Phonetic Normalization](https://img.shields.io/badge/NLP-Phonetic%20Normalization-blueviolet.svg)](app/src/main/java/com/voicerpg/engine/audio/StoryNarrator.kt)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-Passing-39ff14.svg)](app/src/test/java/com/voicerpg/engine/)
[![Engine: Visual Novel Engine](https://img.shields.io/badge/Engine-Visual%20Novel%20Engine%20v1.5.0-teal.svg)](https://github.com/Todd0042/visualnovel-engine)
[![Support on Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20Creator-F16061?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/todd0042)

> **A grounded, emotionally resonant native Android visual novel about blue-collar labor, eldercare, and the creeping obsolescence of everyday work. Built on the [Visual Novel Engine](https://github.com/Todd0042/visualnovel-engine), featuring a 9-act working-class chronicle, multi-voice on-device Android Text-to-Speech character narration, acoustic-ambient soundtracks with real-time speech ducking (-13.1 dB), phonetic NLP normalization, 3-slot atomic persistence, and edge-to-edge Jetpack Compose presentation.**

```
       _________________________________________________________________________
      |  PETE                                   [ ACT I: THE WARM ENGINE ]     |
      |  "You listen to the valves ticking before you plug the scanner in.     |
      |   A sensor will tell you what failed, but your ears will tell you      |
      |   why."                                                                |
      |_________________________________________________________________________|
      |  [▶ AUTO-PLAY]  [⏸ PAUSE]  [◀ PREV]  [▶ NEXT]  [📜 BACKLOG]  [⚙ OPTIONS] |
      |  VOICE: ON-DEVICE TTS >>> AMBIENT BGM: bgm_act1_warm_engine.ogg        |
      |  DSP DUCK: -13.1 dB (ACTIVE) >>> BLUETOOTH PIPELINE: PERSISTENT        |
      |_________________________________________________________________________|
```

---

## 📖 Table of Contents

* **Part 1 — Consumer Overview & Narrative Experience**
  * [🔧 What Is The Human Baseline?](#-what-is-the-human-baseline)
  * [📦 The Premise: Working Life, Caregiving, and the Shift](#-the-premise-working-life-caregiving-and-the-shift)
  * [🎭 The 9-Act Chronicle & Character Cast](#-the-9-act-chronicle--character-cast)
  * [🎧 Audio Drama & Reading Modes](#-audio-drama--reading-modes)
  * [🚀 Quick Download & Installation (Android APK)](#-quick-download--installation-android-apk)
* **Part 2 — Consolidated Technical Documentation & Architecture Reference**
  * [1. System Architecture & Visual Novel Engine Core (`com.voicerpg.engine`)](#1-system-architecture--visual-novel-engine-core)
  * [2. Decoupled Content Packaging & Manifest Specification (`assets/game/`)](#2-decoupled-content-packaging--manifest-specification)
  * [3. Speech Synthesis & On-Device Voice Allocation (`StoryNarrator.kt`)](#3-speech-synthesis--on-device-voice-allocation)
  * [4. NLP & Phonetic Normalization Engine](#4-nlp--phonetic-normalization-engine)
  * [5. Real-Time Audio DSP & Dynamic Ambient Ducking Pipeline (`MusicManager.kt`)](#5-real-time-audio-dsp--dynamic-ambient-ducking-pipeline)
  * [6. Atomic Persistence & 3-Slot Save Management (`SaveManager.kt`)](#6-atomic-persistence--3-slot-save-management)
  * [7. Automated Verification Suite (`app/src/test/`)](#7-automated-verification-suite)
  * [8. Provenance & Non-Commercial Licensing](#8-provenance--non-commercial-licensing)

---

# Part 1 — Consumer Overview & Narrative Experience

## 🔧 What Is The Human Baseline?

**The Human Baseline** is an intimate, realistic narrative visual novel that captures the quiet dignity, physical exhaustion, and unspoken burdens of working-class American life.

- **Pure Grounded Fiction**: No fantasy tropes, no space battles, no RPG combat systems. Just the rhythm of shop wrenches, retail inventory pallets, late-night hospital corridors, and the delicate balance between family responsibility and automated workplace displacement.
- **Full-Cast Audio Drama**: Voiced entirely using Android's built-in Text-To-Speech engine, assigning distinct physical voices, intonations, and vocal pitches to 12 authentic characters.
- **100% Offline & Private**: Zero network dependencies, zero telemetry tracking, and zero in-app purchases.

---

## 📦 The Premise: Working Life, Caregiving, and the Shift

In an aging Midwestern suburb, Todd splits his weeks between automotive repair at Pete's diagnostic garage and managing retail logistics at an independent grocery annex alongside Adriana.

Across nine chapters spanning twenty years, the characters experience the gradual transformation of the workplace:
- Diagnostic telemetry replacing hands-on mechanical intuition.
- Algorithmic scheduling and automated logistics whittling away shift flexibility.
- The grueling reality of caring for aging parents while juggling split shifts.
- The search for human connection, self-worth, and dignity in an economy that measures value purely by efficiency.

---

## 🎭 The 9-Act Chronicle & Character Cast

### The 9-Act Narrative Arc

1. **Act I: The Warm Engine (Year 0)** — Pete's auto shop and Friday retail delivery routines.
2. **Act II: First Tremors (Year 2)** — The introduction of telematics scanners and algorithmic time tracking.
3. **Act III: The Severed Ladder (Year 5)** — Corporate buyouts, shifting wage tiers, and family obligations.
4. **Act IV: The Commuter Drain (Year 8)** — Longer transit routes, vehicle wear, and fatigue.
5. **Act V: The Middle-Age Squeeze (Year 11)** — Balances between kids growing up and parents needing full-time care.
6. **Act VI: The Caregiving Crucible (Year 14)** — Memory care facilities, medical bills, and silent companionship.
7. **Act VII: The Breaking Point (Year 17)** — System shutdowns, severance negotiations, and honest conversations.
8. **Act VIII: The Thirty-Second Hour (Year 19)** — Quiet mornings, independent repair work, and community resilience.
9. **Act IX: The Human Baseline (Year 20)** — A legacy defined not by machines or productivity charts, but by human presence.

### Character Profiles & Vocal Cast

| Character | Role & Archetype | Vocal Pitch | Assigned Gender | Voice Region |
| :--- | :--- | :--- | :--- | :--- |
| **Todd** | Pragmatic mechanic and delivery driver | `1.00` | Male | `US` |
| **Adriana** | Retail manager and anchor of the family | `1.05` | Female | `US` |
| **Pete** | Veteran master diagnostic shop technician | `0.85` | Male | `US` |
| **Kendra** | Younger technician wrestling with gig schedules | `1.15` | Female | `US` |
| **Carlos / Sam** | Warehouse clerk managing automated logistics | `0.95` | Male | `US` |
| **Elena** | Elder care specialist and visiting nurse | `1.08` | Female | `US` |
| **Chloe** | High school student observing generational shift | `1.20` | Female | `US` |
| **Marcus** | Corporate district auditor focused on KPIs | `0.90` | Male | `US` |
| **Senator Vance** | Public policy representative on labor hearings | `0.88` | Male | `US` |
| **News Anchor** | Broadcast radio narrator tracking regional economics | `1.02` | Neutral | `US` |
| **Narrator** | Descriptive stage directions and internal monologue | `0.98` | Neutral | `US` |

---

## 🎧 Audio Drama & Reading Modes

- **Auto-Play Mode (Default)**: Plays continuously like an audiobook. Dialogue automatically paces speech, ducks music during narration, and pauses naturally between character exchanges.
- **Tactile Manual Reading**: Advance line by line with a tap, or step backward to re-listen to previous lines.
- **Dialogue Backlog**: Access the top-right history drawer anytime to review full conversational transcripts with character color tags.
- **3-Slot Save Management**: Save your progress across three independent slots with chapter indicators and timestamps.

---

## 🚀 Quick Download & Installation (Android APK)

Download the signed APK from [GitHub Releases](https://github.com/Todd0042/the-human-baseline/releases) and install it on any device running **Android 8.0 (API 26) or higher**:

```bash
adb install -r the-human-baseline-v1.5.1.apk
```

---

# Part 2 — Consolidated Technical Documentation & Architecture Reference

## 1. System Architecture & Visual Novel Engine Core

*The Human Baseline* is built upon the open-source **[Visual Novel Engine](https://github.com/Todd0042/visualnovel-engine)** (`com.voicerpg.engine`), an ultra-lean, content-agnostic Android framework designed for voice-narrated visual novels:

```
+-----------------------------------------------------------------------+
|                       THE HUMAN BASELINE CLIENT                       |
|           (Jetpack Compose UI, Material 3, Dialogue History)          |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                      VISUAL NOVEL CORE ENGINE                         |
|  +--------------------+  +--------------------+  +-----------------+  |
|  |    StoryNarrator   |  |    MusicManager    |  |   SaveManager   |  |
|  |  (Multi-Voice TTS) |  |   (DSP Ducking)    |  |  (3-Slot State) |  |
|  +--------------------+  +--------------------+  +-----------------+  |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                       GAME CONTENT DATA (JSON)                        |
|  manifest.json | characters/*.json | story/scenes.json, nodes.json    |
+-----------------------------------------------------------------------+
```

Core framework guarantees:
- **100% On-Device & Private**: Zero network permissions required.
- **16 KB Page Alignment**: Fully compliant with Android 15's 16 KB page-size architecture requirements.

---

## 2. Decoupled Content Packaging & Manifest Specification

The entire game configuration is declared in `app/src/main/assets/game/manifest.json`:

```json
{
  "_doc": "The Human Baseline - Visual Novel Story Manifest.",
  "gameTitle": "The Human Baseline",
  "gameSubtitle": "A Realistic Socio-Economic Visual Novel",
  "worldName": "The Rust & Glass Corridor",
  "initialSceneId": "scene_act1_garage",
  "initialNodeId": "act1_node_01",
  "titleBackgroundAsset": "story/title_background.jpg"
}
```

The game content pack provides:
- **12 Character Definitions** (`characters/*.json`): Binding portraits, theme accent colors, and TTS pitch modulation.
- **Scene Backdrops** (`story/scenes.json`): Binding realistic photography backdrops and custom ambient audio tracks.
- **Dialogue Graphs** (`story/nodes.json`): Master story script covering the complete 9-act chronicle.

---

## 3. Speech Synthesis & On-Device Voice Allocation

On-device TTS bindings dynamically allocate system voices based on character metadata via [`StoryNarrator.kt`](app/src/main/java/com/voicerpg/engine/audio/StoryNarrator.kt):

### Vocal Pitch Modulation

Fundamental vocal frequencies are modulated per character using:

$$F_{\text{voice}} = F_{\text{base}} \times \text{ttsPitch}$$

Where $\text{ttsPitch} \in [0.85, 1.20]$.

### Utterance Progress Synchronization

```
  +--------------+   Speak Request    +-------------------+
  |     IDLE     | -----------------> |    TTS_PLAYING    |
  +--------------+                    +-------------------+
         ^                                      |
         | Next Line Auto-Trigger               | onDone() Callback
         +--------------------------------------+
```

- **Locale Filtering**: Matches character regions against `DEFAULT_ALLOWED_VOICE_REGIONS = ["US", "CA", "GB", "AU", "IE", "ZA"]`.
- **Gender Selection**: Dynamically scans installed system voices to match character gender properties (`male`, `female`).

---

## 4. NLP & Phonetic Normalization Engine

Before sending script lines to the Android TTS synthesizer, [`StoryNarrator.kt`](app/src/main/java/com/voicerpg/engine/audio/StoryNarrator.kt) runs text through an automated NLP phonetic normalization pipeline:

1. **Stage Direction Stripping**: Removes stage direction formatting asterisks (`*sighs*`, `*clears throat*`).
2. **Technical Acronym Expansion**:
   $$\text{"OBD"} \longrightarrow \text{"O.B.D."}, \quad \text{"ECU"} \longrightarrow \text{"E.C.U."}, \quad \text{"KPI"} \longrightarrow \text{"K.P.I."}$$
3. **Phonetic Pronunciation Maps**:
   $$\text{"Pete"} \longrightarrow \text{"Peet"}, \quad \text{"Adriana"} \longrightarrow \text{"Ah-dree-ah-na"}$$
4. **Abbreviation Disambiguation**: Converts title abbreviations using regex:
   $$\text{Regex}(\backslash\text{bSt}\backslash.?\backslash\text{s}+([A-Z])) \longrightarrow \text{"Saint " } + \$1$$

---

## 5. Real-Time Audio DSP & Dynamic Ambient Ducking Pipeline

*The Human Baseline* features dedicated original ambient soundscapes crafted for each chapter of the narrative. Ambient audio is routed via [`MusicManager.kt`](app/src/main/java/com/voicerpg/engine/audio/MusicManager.kt) with real-time speech ducking:

$$V_{\text{bgm}}(t) = V_{\text{base}} \cdot \Big(1 - (1 - d) \cdot \mathbb{I}_{\text{speaking}}(t)\Big)$$

Where:
- $V_{\text{base}}$ is the configured master ambient volume.
- $d = 0.22$ is the ducking ratio, smoothly reducing ambient background music to **$-13.1\text{ dB}$** during character narration.
- $\mathbb{I}_{\text{speaking}}(t) \in \{0, 1\}$ is the boolean speech indicator provided by the TTS utterance listener.

### 9-Act Ambient Soundtrack Pipeline

| Act & Title | Theme Asset | Mood & Acoustic Profile |
| :--- | :--- | :--- |
| **Act I: The Warm Engine** | `bgm_act1_warm_engine.ogg` | Low-frequency mechanical drone, acoustic guitar |
| **Act II: First Tremors** | `bgm_act2_first_tremors.ogg` | Subtle electronic sub-bass, cold reverb |
| **Act III: The Severed Ladder** | `bgm_act3_severed_ladder.ogg` | Muted piano, industrial tape delay |
| **Act IV: The Commuter Drain** | `bgm_act4_commuter_drain.ogg` | Rhythmic highway hum, rain ambiance |
| **Act V: The Middle-Age Squeeze** | `bgm_act5_middle_age_squeeze.ogg` | Warm acoustic strings, reflective cadence |
| **Act VI: The Caregiving Crucible** | `bgm_act6_caregiving_crucible.ogg` | Minimalist felt piano, quiet stillness |
| **Act VII: The Breaking Point** | `bgm_act7_breaking_point.ogg` | Tense drone, gradual harmonic crescendo |
| **Act VIII: The Thirty-Second Hour** | `bgm_act8_thirty_second_hour.ogg` | Early morning porch ambient, gentle picking |
| **Act IX: The Human Baseline** | `bgm_act9_human_baseline.ogg` | Full harmonic resolution, grounded cello |

### Bluetooth Audio Focus Keep-Alive

`MusicManager` maintains continuous media focus using `AudioAttributes.USAGE_MEDIA` and `AudioManager.AUDIOFOCUS_GAIN`, keeping vehicle Bluetooth sinks active to prevent audio hardware clipping on speech beginnings.

---

## 6. Atomic Persistence & 3-Slot Save Management

State preservation is handled by [`SaveManager.kt`](app/src/main/java/com/voicerpg/engine/engine/SaveManager.kt):
- **3 Independent Save Slots**: Each records active scene ID, node ID, elapsed reading time, and date timestamp.
- **Atomic Two-Phase Writes**: Writes state to temporary `.tmp` file before renaming, preventing corrupted saves during unexpected device power loss.

---

## 7. Automated Verification Suite

Headless JVM tests validate that every asset, character portrait, and story node referenced in the script exists and resolves cleanly:

```bash
# Run unit test suite:
./gradlew testDebugUnitTest

# Assemble debug APK:
./gradlew assembleDebug
```

Verification includes:
- 100% of character portraits, scene backdrops, and music tracks resolve from assets.
- Complete dialogue graph reachability (zero dead-end orphan nodes).
- Save and load serialization integrity across all 3 slots.

---

## 8. Provenance & Non-Commercial Licensing

- **Original Narrative Work**: All characters, scripts, dialogue, and narrative arcs in *The Human Baseline* are original creative works.
- **PolyForm Noncommercial 1.0.0**: Free for personal, recreational, educational, and hobbyist reading. For commercial inquiries, contact **[Todd.0042.git@gmail.com](mailto:Todd.0042.git@gmail.com)**.

---

<p align="center">
  If you appreciate The Human Baseline, consider supporting open-source development:<br/><br/>
  <a href="https://ko-fi.com/todd0042" target="_blank">
    <img src="https://img.shields.io/badge/☕_Support_on_Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support on Ko-fi">
  </a>
</p>

---

<p align="center">
  <a href="https://ko-fi.com/todd0042">
    <img src="https://raw.githubusercontent.com/Todd0042/creator-assets/main/banners/todd_creator_banner_v2.0.png" alt="Support Todd on Ko-fi" width="100%" />
  </a>
</p>
