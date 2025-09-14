# MediaPipe Synth

A hand-tracked, Serum-inspired synth prototype built with Python, MediaPipe, and Pyo.
Built for synth sound design without the need for the various dials/controls on common synths such as Serum.

---

## Features

### Right Hand
- Size of expanded hand → controls the number of voices (polyphony)
- Hand rotation → smoothly morphs waveform (sine → saw → square → triangle)
- Side-to-side palm tilt → sets detune amount between voices

### Left Hand
- Thumb–Index distance → controls lowpass filter cutoff (Moog LP style)
- Thumb–Middle distance → sets chorus depth
- Index–Middle distance → controls distortion drive
- Hand rotation → sets the pitch of oscillators

---

## Tech Stack
- MediaPipe → hand landmark detection
- OpenCV → webcam input + image processing
- Pyo → audio synthesis & effects
- Python 3.11+

---

## Getting Started

### 1) Clone the repo
```bash
git clone https://github.com/minjunminji/mediapipesynth.git
cd mediapipesynth
```

### 2) Create a virtual environment
```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the synth
```bash
python vision.py
```
This opens your webcam feed, tracks your hands, and sends control values into the synth engine.

---

## Demo
- Coming soon

---

## Project Structure
```
.
├── synth.py      # Audio engine (oscillators, filter, chorus, distortion)
├── vision.py     # Hand tracking & parameter mapping
├── requirements.txt
└── README.md
```

---

## Roadmap
- Add more waveforms & advanced morphing
- Add envelope control (ADSR)
- Add reverb effect
- Build a simple UI to tweak ranges & mappings

---

## Acknowledgments
Inspired by Xfer Serum and motion-controlled synth concepts.
Built using MediaPipe, OpenCV, and Pyo.

---

## Disclaimer
This is a prototype built for experimentation. Latency and stability may vary depending on your system.

