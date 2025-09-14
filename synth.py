from pyo import *

s = Server().boot()
s.start()

# Control parameters
num_voices = 3
detune = 0.05
pitch = 220  # Hz
cutoff = 1000  # For MoogLP
chorus_depth = 0.3
drive = 0.7

# Morph control (0.0 .. 1.0). Expose as Sig so other modules can update it.
# 0.0 -> sine/square blend side, 1.0 -> saw/triangle blend side.
morph = Sig(0.0)

# --- Waveshape tables ---
sine_tbl = HarmTable([1])
saw_tbl = SawTable()
square_tbl = SquareTable()
# Simple triangle approximation (can be improved by more harmonics if desired)
tri_tbl = HarmTable([0, 1, 0, 0, 0, 0, 0])

# --- Build detuned voices with morphing ---
freqs = [pitch * (1 + detune * (i - num_voices // 2)) for i in range(num_voices)]

voices = []
per_voice_gain = 0.2 / max(1, num_voices)
for f in freqs:
    # Four parallel oscillators per voice
    o_sine = Osc(sine_tbl, freq=f, mul=per_voice_gain)
    o_saw = Osc(saw_tbl, freq=f, mul=per_voice_gain)
    o_square = Osc(square_tbl, freq=f, mul=per_voice_gain)
    o_tri = Osc(tri_tbl, freq=f, mul=per_voice_gain)

    # Crossfade sine↔saw and square↔triangle, then crossfade the blends
    blend1 = Interp(o_sine, o_saw, morph)
    blend2 = Interp(o_square, o_tri, morph)
    final = Interp(blend1, blend2, morph)
    voices.append(final)

# Mix all voices down to mono (or set voices=2 for stereo if desired)
mix = Mix(voices, voices = 1)

# Effects chain
LPfilt = MoogLP(mix, freq=cutoff, res=0.8)
chor = Chorus(LPfilt, depth=chorus_depth, feedback=0.25, bal=0.5)
dist = Disto(chor, drive=drive, slope=0.7, mul=0.5).out()

s.gui(locals())
