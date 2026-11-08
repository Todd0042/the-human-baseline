<p align="center">
  <a href="https://ko-fi.com/todd0042">
    <img src="https://raw.githubusercontent.com/Todd0042/creator-assets/main/banners/todd_creator_banner_v1.0.png" alt="Support Todd on Ko-fi" width="100%" />
  </a>
</p>

---

# 🔧 The Human Baseline: An Audio-First Narrative of Working Life

[![Version](https://img.shields.io/badge/Version-1.5.0-ff2a85.svg)](https://github.com/Todd0042/the-human-baseline/releases)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-00f0ff.svg)](LICENSE)
[![Platform: Android 8.0+](https://img.shields.io/badge/Platform-Android%208.0%2B%20(API%2026%2B)-3DDC84.svg?logo=android&logoColor=white)](https://developer.android.com)
[![16 KB Page Size](https://img.shields.io/badge/16%20KB-Compatible-success.svg)](https://developer.android.com/16kb-page-size)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.0.21-7F52FF.svg?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![UI: Jetpack Compose](https://img.shields.io/badge/UI-Jetpack%20Compose%202024.10.01-4285F4.svg?logo=jetpackcompose&logoColor=white)](https://developer.android.com/jetpack/compose)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-5%20Passing-39ff14.svg)](app/src/test/java/com/voicerpg/engine/)
[![Engine: Visual Novel Engine](https://img.shields.io/badge/Engine-Visual%20Novel%20Engine%20v1.5.0-teal.svg)](https://github.com/Todd0042/visualnovel-engine)
[![Support on Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20Creator-F16061?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/todd0042)

> **A grounded, emotionally resonant native Android visual novel about blue-collar labor, eldercare, and the creeping obsolescence of everyday work. Built on the [Visual Novel Engine](https://github.com/Todd0042/visualnovel-engine), featuring a 9-act working-class chronicle, multi-voice on-device Android Text-to-Speech character narration, acoustic-ambient soundtracks with dynamic speech ducking, 3-slot atomic persistence, and edge-to-edge Jetpack Compose presentation.**

```
       _________________________________________________________________________
      |  PETE                                   [ ACT I: THE WARM ENGINE ]     |
      |  "You listen to the valves ticking before you plug the scanner in.     |
      |   A sensor will tell you what failed, but your ears will tell you      |
      |   why."                                                                |
      |_________________________________________________________________________|
      |  [▶ AUTO-PLAY]  [⏸ PAUSE]  [◀ PREV]  [▶ NEXT]  [📜 BACKLOG]  [⚙ OPTIONS] |
      |  VOICE: ON-DEVICE TTS >>> AMBIENT BGM: bgm_act1_warm_engine.ogg        |
      |_________________________________________________________________________|
```

---

## 📖 Table of Contents

* **Part 1 — Consumer Overview & Narrative Experience**
  * [🔧 What Is The Human Baseline?](#-what-is-the-human-baseline)
  * [📦 The Premise: Working Life, Caregiving, and the Shift](#-the-premise-working-life-caregiving-and-the-shift)
  * [🎭 The 9-Act Chronicle & Cast](#-the-9-act-chronicle--cast)
  * [🎧 Audio Drama & Reading Modes](#-audio-drama--reading-modes)
  * [🚀 Quick Download & Installation (Android APK)](#-quick-download--installation-android-apk)
* **Part 2 — Technical Architecture & Engine Integration**
  * [1. Powered by Visual Novel Engine](#1-powered-by-visual-novel-engine)
  * [2. How The Human Baseline Configures the Engine (`manifest.json`, `GameContent.kt`)](#2-how-the-human-baseline-configures-the-engine)
  * [3. 9-Act Ambient Soundtrack Pipeline (`bgm_act1` – `bgm_act9`)](#3-9-act-ambient-soundtrack-pipeline)
  * [4. Character Voice & Phonetic Normalization (`StoryNarrator.kt`)](#4-character-voice--phonetic-normalization)
  * [5. Automated Verification Suite (`app/src/test/`)](#5-automated-verification-suite)
  * [6. License & Creator Support](#6-license--creator-support)

---

# Part 1 — Consumer Overview & Narrative Experience

### 🔧 What Is The Human Baseline?
**The Human Baseline** is an intimate, realistic narrative visual novel that captures the quiet dignity, physical exhaustion, and unspoken burdens of working-class American life.
- **Pure Grounded Fiction**: No magic, no space battles, no RPG combat systems. Just the rhythm of shop wrenches, retail inventory pallets, late-night hospital corridors, and the delicate balance between family responsibility and automated workplace displacement.
- **Full-Cast Audio Drama**: Voiced entirely using Android's built-in Text-To-Speech engine, assigning distinct physical voices, intonations, and vocal pitches to 12 authentic characters.
- **100% Offline & Private**: Zero network dependencies, zero telemetry tracking, and zero in-app purchases.

---

### 📦 The Premise: Working Life, Caregiving, and the Shift
In an aging Midwestern suburb, Todd splits his weeks between automotive repair at Pete's diagnostic garage and managing retail logistics at an independent grocery annex alongside Adriana.

Across nine chapters spanning twenty years, the characters experience the gradual transformation of the workplace:
- Diagnostic telemetry replacing hands-on mechanical intuition.
- Algorithmic scheduling and automated logistics whittling away shift flexibility.
- The grueling reality of caring for aging parents while juggling split shifts.
- The search for human connection, self-worth, and dignity in an economy that measures value purely by efficiency.

---

### 🎭 The 9-Act Chronicle & Cast

1. **Act I: The Warm Engine (Year 0)** — Pete's auto shop and Friday retail delivery routines.
2. **Act II: First Tremors (Year 2)** — The introduction of telematics scanners and algorithmic time tracking.
3. **Act III: The Severed Ladder (Year 5)** — Corporate buyouts, shifting wage tiers, and family obligations.
4. **Act IV: The Commuter Drain (Year 8)** — Longer transit routes, car trouble, and fatigue.
5. **Act V: The Middle-Age Squeeze (Year 11)** — Balances between kids growing up and parents needing full-time care.
6. **Act VI: The Caregiving Crucible (Year 14)** — Memory care facilities, medical bills, and silent companionship.
7. **Act VII: The Breaking Point (Year 17)** — System shutdowns, severance negotiations, and honest conversations.
8. **Act VIII: The Thirty-Second Hour (Year 19)** — Quiet mornings, independent repair work, and community resilience.
9. **Act IX: The Human Baseline (Year 20)** — A legacy defined not by machines or productivity charts, but by human presence.

#### Key Characters:
- **Todd**: Pragmatic mechanic and delivery driver navigating shifting labor systems.
- **Adriana**: Retail manager and anchor of the family, coordinating logistics and caregiving.
- **Pete**: Veteran shop owner with forty years of diagnostic intuition in his fingertips.
- **Kendra & Carlos**: Younger technicians and clerks wrestling with modern gig work and automated schedules.
- **Evelyn**: Elderly mother whose quiet grace grounds the emotional heart of the story.

---

### 🎧 Audio Drama & Reading Modes

- **Auto-Play Mode (Default)**: Plays continuously like an audiobook. Narration automatically paces dialogue, ducks music during speech, and pauses naturally between character exchanges.
- **Tactile Manual Reading**: Advance line by line with a tap, or step backward to re-listen to previous lines.
- **Dialogue Backlog**: Access the top-right history drawer anytime to review full conversational transcripts with character color tags.
- **3-Slot Save Management**: Save your progress across three independent slots with chapter indicators and timestamps.

---

### 🚀 Quick Download & Installation (Android APK)

Download the signed APK from [GitHub Releases](https://github.com/Todd0042/the-human-baseline/releases) and install it on any device running **Android 8.0 (API 26) or higher**:

```bash
adb install -r the-human-baseline-v1.5.0.apk
```

---

# Part 2 — Technical Architecture & Engine Integration

### 1. Powered by Visual Novel Engine
*The Human Baseline* is built on the open-source **[Visual Novel Engine](https://github.com/Todd0042/visualnovel-engine)** (`com.voicerpg.engine`), an ultra-lean, content-agnostic Android framework designed specifically for voice-narrated visual novels. All core rendering, audio playback, TTS voice management, and persistence logic are provided by the engine.

---

### 2. How The Human Baseline Configures the Engine
The entire game configuration is declared in `app/src/main/assets/game/manifest.json`:

```json
{
  "gameTitle": "The Human Baseline",
  "gameSubtitle": "An Audio-First Narrative of Working Life",
  "initialSceneId": "scene_act1_garage",
  "initialNodeId": "act1_node_01",
  "titleBackgroundAsset": "story/bg_garage_interior.jpg",
  "ttsReplacements": {
    "Pete": "Peet",
    "Adriana": "Ah-dree-ah-na",
    "OBD": "O.B.D.",
    "ECU": "E.C.U."
  }
}
```

The game content pack provides:
- **12 Character Definitions** (`characters/*.json`): Binding character portraits, theme accent colors, and TTS pitch modulation.
- **Scene Backdrops** (`story/scenes.json`): Binding realistic photography backdrops and custom ambient audio tracks.
- **Dialogue Graphs** (`story/nodes.json`): Master story script covering the complete 9-act chronicle.

---

### 3. 9-Act Ambient Soundtrack Pipeline
*The Human Baseline* features dedicated original ambient soundscapes crafted for each chapter of the narrative:
- `bgm_act1_warm_engine.ogg`
- `bgm_act2_first_tremors.ogg`
- `bgm_act3_severed_ladder.ogg`
- `bgm_act4_commuter_drain.ogg`
- `bgm_act5_middle_age_squeeze.ogg`
- `bgm_act6_caregiving_crucible.ogg`
- `bgm_act7_breaking_point.ogg`
- `bgm_act8_thirty_second_hour.ogg`
- `bgm_act9_human_baseline.ogg`

The engine's `MusicManager` automatically transitions between these tracks as scenes change, providing dynamic speech ducking during dialogue narration.

---

### 4. Character Voice & Phonetic Normalization (`StoryNarrator.kt`)
On-device TTS bindings dynamically assign voices based on character metadata:
- Realistic gender assignments and pitch shifts (`ttsPitch`: `0.80` to `1.20`) provide vocal clarity.
- Normalization strips formatting asterisks (`*sighs*`) and converts technical automotive abbreviations into spoken equivalents.

---

### 5. Automated Verification Suite (`app/src/test/`)
Headless JVM tests validate that every asset and story node referenced in the script exists and resolves cleanly:
```bash
./gradlew testDebugUnitTest
```
- Validates 100% of character portraits, scene backdrops, and music tracks.
- Asserts graph integrity and save system stability.

---

### 6. License & Creator Support
- **Non-Commercial License**: *The Human Baseline* is licensed under the **[PolyForm Noncommercial License 1.0.0](LICENSE)**. Personal, educational, and non-commercial gameplay is 100% free.
- **Commercial Licensing Inquiries**: For inquiries, contact **[todd.0042.git@gmail.com](mailto:todd.0042.git@gmail.com)**.

---

<p align="center">
  If you enjoy playing The Human Baseline, consider supporting open-source development:<br/><br/>
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
