from pyo import *

s = Server().boot()
s.start()

# Control parameters
num_voices = 3
morph = 0.5 # 0=sine, 1=saw, 2=square, 3=triangle (continuous)
detune = 0.05
pitch = 220 # Hz
cutoff = 1000 # For moogLP
chorus_depth = 0.3
drive = 0.7

# Detuner, shifts index of middle voice to 0 and detunes other voices around it by the detune parameter
freqs = [pitch * (1 + detune * (i - num_voices//2)) for i in range(num_voices)]
oscillators = [Sine(freq=f, mul=0.1) for f in freqs] # Add morphing soon
mix = Mix(oscillators, voices = 1)

LPfilt = MoogLP(mix, freq=cutoff, res=0.8)
chor = Chorus(LPfilt, depth=chorus_depth, feedback=0.25, bal=0.5)
dist = Disto(chor, drive=drive, slope=0.7, mul=0.5).out()

s.gui(locals())