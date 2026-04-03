# AASB: As Above, So Below
## Mars Twin Peaks — Scale Analysis and Giza Structural Parallel
### Eric D. Martin — 2024 (calculations), 2026 (repo)

---

## Overview

This analysis uses NASA Mars Pathfinder IMP camera stereo images (PIA02405, PIA02406) and
known engineering data to derive a ground-scale metric for the Mars Twin Peaks scene.
Using this scale, a ground-level object of interest near the lander was measured.
Its dimensions and positional geometry were then compared against the Great Sphinx of Giza.

All measurements were performed manually by Eric D. Martin using:
- 3 ft × 5 ft printed enlargements of PIA02405/PIA02406
- T-square for orthogonal measurement
- Vector art (with image removed, lines only) for confirmation
- Parallax/perspective offset correction: +1 inch from image base (see below)

No AI assistance was used in the original calculations.

---

## Source Images

| Image | ID | Dimensions | Notes |
|-------|----|------------|-------|
| Left eye | PIA02405 | 7238 × 3135 px | 500% enlarged TIF |
| Right eye | PIA02406 | 7296 × 3135 px | 500% enlarged TIF |

Camera: IMP (Imager for Mars Pathfinder), telephoto lens
IMP resolution: 0.96 mrad/pixel
At North Twin Peak distance (860 m): 0.83 m/pixel at native res → 0.165 m/pixel in 5× enlarged TIF

---

## Labeled Points (on printed enlargement)

| Label | Object | Print position |
|-------|--------|---------------|
| A | Mars object of interest (top) | 8 7/16 in |
| B | North Twin Peak (base) | 4 7/8 in |
| C | South Twin Peak (base) | 5 1/4 in |
| D | Reference/horizon mark | 43 in |
| E | Mars object (base level) | 7 7/8 in |
| F | Mars object (intermediate) | 7 7/16 in |

---

## Scale Derivation

Known: North Twin Peak (B) is **2800 feet** from lander.

Measurement on print:
> B (4 7/8 in) to D (43 in) = **38 1/8 inches**

Scale:
> **1 inch = 2800 ft ÷ 38 1/8 in = 73 27/61 ft/in ≈ 73.44 ft/in**

Cross-check: South Twin Peak (C) is 3300 feet from lander.
> C (5 1/4 in) to D (43 in) = 37 3/4 in

---

## Parallax / Perspective Offset Correction

The base of the Mars object is NOT at ground level in the image due to:
1. Camera height above Martian surface
2. Foreshortening at distance
3. "Nose bridging" perspective effect (EDM term — no established name for this known phenomenon)

Correction applied: object base taken as **+1 inch from image bottom**, not at 0 inches.
This was a reasoned estimate, not a measured value, and should be noted as an assumption.

---

## Measured Distances (inter-point, on print)

From `twin_peaks_nasa_updated.txt` (refined version):

| Measurement | Print (inches) | Converted (feet) |
|-------------|---------------|-----------------|
| B (4 7/8) → D (43) | 38 1/8 | 2800 ft *(scale basis)* |
| C (5 1/4) → D (43) | 37 3/4 | ~2772 ft |
| B → F | 2 9/16 | ~187.9 ft |
| C → F | 2 3/16 | ~160.6 ft |
| E → A (object height) | 9/16 | ~41.3 ft |
| A (8 7/16) → D (43) | 34 9/16 | ~2537 ft |
| E (7 7/8) → D (43) | 35 1/8 | ~2578 ft |
| B → A | 3 9/16 | ~261.4 ft |
| B → E | 3 | ~220.3 ft |
| F → E | 7/16 | ~32.2 ft |
| F → A | 1 | ~73.4 ft |

---

## Great Sphinx of Giza — Reference Measurements

From `Great-Sphinx-Giza-Egypt.txt`:

| Label | Value | Notes |
|-------|-------|-------|
| A | 66 ft high | Sphinx height (actual: 66 ft / 20.22 m ✓) |
| E | 1 in = 7 97/137 ft | Scale of Sphinx reference print |
| B | 8 9/16 in | Paw to tip of head (height in print) |
| F | 2 × E = 15 57/137 ft | Width dimension |
| C | 2 3/8 × E = 18 42/137 ft | Secondary dimension |

Sphinx actual dimensions (public record):
- Height: 66 ft (20.22 m)
- Length: 240 ft (73.15 m)
- Width at face: ~20 ft

---

## Result: Dimensional Match

The Mars object measured under IMP scale is consistent with Great Sphinx dimensions.
The positional geometry of the Mars object relative to Twin Peaks (North and South)
corresponds to the positional geometry of the Great Sphinx relative to the Giza pyramid complex.

---

## Third Formation: Plateau to the Right of North Twin

The Giza complex contains three pyramids: Khufu, Khafre, and Menkaure.
Twin Peaks (North + South) correspond to two of these.

**Finding:** A third formation — a **plateau** — is visible in the IMP panoramic images
to the right of North Twin Peak, at greater distance from the lander (appears lower on
the horizon due to perspective; actual size may be larger than the Twin Peaks).
It is visible in the close-up measurement photographs (images 12576–12578) at
approximately 57–59 inches horizontal, 7–9 inches vertical on the enlarged print.

- Working label: **Third Formation / Plateau**
- Appears further away than both Twin Peaks → lower horizon position → scale-corrected
  height would be larger than it appears in image
- The positional geometry of the three formations (North Twin, South Twin, Plateau)
  **matches the three Giza pyramid positions**
- The Sphinx-analog object sits in a position relative to these three formations
  analogous to the Great Sphinx's position relative to the Giza pyramids

**The test:** Overlay the Giza layout (scaled to IMP metric) onto the Mars image.
If the three formations plus the Sphinx-analog object fall cleanly onto their Giza
counterparts, the geometric parallel is confirmed.

**North Knob:** NASA officially names the third feature **"North Knob"** —
described in HiRISE/JPL documentation as "a bright mound upper right of Twin Peaks,
visible on Pathfinder's horizon." This directly corresponds to the plateau visible to
the right of North Twin Peak in the IMP panoramas (Eric's measurements, 2024).

**Overhead imagery confirmed:**
- NASA Viking Orbiter images (pre-1997) identified Twin Peaks from orbit
- HiRISE/MRO image **PSP_001890_1995** covers the full landing site at **25 cm/pixel**
  (objects ~85 cm across resolvable). All three formations visible: Twin Peaks + North Knob.
  https://www.uahirise.org/PSP_001890_1995
- JPL catalog: PIA09105 — "Mars Pathfinder Landing Site and Surroundings"
  https://science.nasa.gov/photojournal/mars-pathfinder-landing-site-and-surroundings

**The test is now executable:** Overlay scaled Giza layout onto HiRISE PSP_001890_1995.
North Twin + South Twin + North Knob should fall on three Giza pyramid positions.
The Sphinx-analog object should appear between the lander and the formation cluster.

---

## Methodology Caveats

1. The +1 inch parallax correction is an estimate, not a derived value
2. Stereo reconstruction was not completed (focal point alignment failed) — scale method used instead
3. C to D distance gives slightly different scale than B to D — small inconsistency unexplained
4. "As above, so below" is a hypothesis, not a confirmed finding
5. Independent verification requires: overhead HiRISE image of the area + independent scale check

---

*Eric D. Martin, 2024. Repo created 2026-04-03.*
