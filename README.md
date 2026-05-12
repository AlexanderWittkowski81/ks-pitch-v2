# KS Pitch Deck — Modulare Struktur

## Warum modular?

Vorher: 1× index.html mit 436KB → Edits frassen jede Chat-Session den Kontext.

Jetzt: 17 Slide-Files à 2-8KB (Slide 1 ist 333KB wegen eingebettetem Cover-Bild).
Bei einem Edit muss nur der betroffene Slide-File angefasst werden.

## Struktur

```
ks-pitch-modular/
├── shared/
│   ├── header.html      ← <head>, <body>, CSS, Login-Form (14KB)
│   └── footer.html      ← </body></html> (0,6KB)
├── slides/
│   ├── 01-cover.html              (333KB — enthält Audi-Bild als Base64)
│   ├── 02-smart-seed.html         (2,5KB)
│   ├── 03-warum-ihr.html          (5,8KB)
│   ├── 04-einfuehrung.html        (2,7KB)
│   ├── 05-lage-mai-2026.html      (5,1KB)
│   ├── 06-umsatz-vergleich.html   (4,4KB)
│   ├── 07-umsatz-2025.html        (4,6KB)
│   ├── 08-forecast-2026.html      (6,5KB)
│   ├── 09-northstar-2030.html     (8,0KB)
│   ├── 10-pnl-2026.html           (7,2KB)
│   ├── 11-gmbh-wandlung.html      (4,3KB)
│   ├── 12-team.html               (7,8KB)
│   ├── 13-tiers.html              (6,7KB)
│   ├── 14-investorenrechte.html   (3,9KB)
│   ├── 15-cap-table.html          (8,2KB)
│   ├── 16-risiken.html            (6,4KB)
│   └── 17-abschluss.html          (4,0KB)
├── build.py             ← Build-Script
└── index.html           ← Generiert durch build.py
```

## Workflow

### 1. Slide bearbeiten

```bash
# Edit nur die relevante Slide-Datei
$EDITOR slides/10-pnl-2026.html
```

### 2. Neu bauen

```bash
python3 build.py
```

### 3. Lokal testen

```bash
open index.html
# Passwort: kuestenshuttle2026
```

### 4. Deployen

GitHub-Push triggert Netlify Auto-Deploy.

## Edit-Regeln

- **Niemals** Slide-Boundary-Marker (`<!-- ============= ... ============= -->`) verändern
- **Niemals** die `<section class="slide">` Wrapper umschreiben — sonst bricht das Slide-System
- **shared/header.html anfassen** nur für globales CSS / Login-Logik
- **shared/footer.html anfassen** nur für `</body></html>` (sollte nie nötig sein)

## Globaler Edit über alle Slides

Wenn z.B. ein Begriff überall ersetzt werden muss:

```bash
# In allen Slide-Files das gleiche ersetzen
grep -rln "alter_begriff" slides/
sed -i 's/alter_begriff/neuer_begriff/g' slides/*.html
python3 build.py
```

## Passwort

`kuestenshuttle2026` — SHA256-Hash in shared/header.html eingebaut.

## Aktueller Stand

- Datum: 12.05.2026
- Bewertung: 250k Pre-Money Cap
- Round: 60k (Smart Seed)
- Empfehlung: Beide Tier 3 (30k+30k)
- Northstar: 2030 Autonomous (OEM-Pilot VW/BMW)
- Floor-Fälligkeit Tier 3: Mai 2029
