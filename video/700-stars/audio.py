"""Synthesizes the soundtrack for the 700-star video from timeline.json.

    python3 audio.py   -> out/soundtrack.wav (44.1 kHz stereo)

Everything is generated here (no samples), so the music and effects line up
exactly with the scene times in timeline.json. Needs numpy and scipy.
"""
import json
import wave
from pathlib import Path

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

HERE = Path(__file__).parent
TL = json.loads((HERE / "timeline.json").read_text())
SR = 44100
N = int(TL["duration"] * SR)
rng = np.random.default_rng(700)

dry = np.zeros((N, 2))
wet_send = np.zeros((N, 2))  # goes through the reverb


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def env(n, a, r, curve=4.0):
    """attack seconds, then exponential decay over the rest"""
    e = np.ones(n)
    na = max(1, int(a * SR))
    e[:na] = np.linspace(0, 1, na)
    tail = n - na
    if tail > 0:
        e[na:] = np.exp(-curve * np.linspace(0, 1, tail) * (n / SR) / max(r, 1e-3))
    return e


def place(sig, t, pan=0.0, gain=1.0, reverb=0.3):
    i = int(t * SR)
    if i >= N:
        return
    sig = sig[: N - i] * gain
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    st = np.stack([sig * l, sig * r], axis=1) * np.sqrt(2)
    dry[i : i + len(sig)] += st
    wet_send[i : i + len(sig)] += st * reverb


def tt(dur):
    return np.arange(int(dur * SR)) / SR


def lowpass(x, f, order=2):
    return sosfilt(butter(order, f, "low", fs=SR, output="sos"), x)


def highpass(x, f, order=2):
    return sosfilt(butter(order, f, "high", fs=SR, output="sos"), x)


def bandpass(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)


# ---------- instruments ----------
def bell(midi, dur=2.0):
    t = tt(dur)
    f = hz(midi)
    s = (np.sin(2 * np.pi * f * t) * env(len(t), 0.004, dur * 0.9)
         + 0.35 * np.sin(2 * np.pi * f * 2.01 * t) * env(len(t), 0.002, dur * 0.45)
         + 0.12 * np.sin(2 * np.pi * f * 3.98 * t) * env(len(t), 0.001, dur * 0.2))
    return s


def pluck(midi, dur=0.6):
    t = tt(dur)
    f = hz(midi)
    s = np.sign(np.sin(2 * np.pi * f * t)) * 0.3 + np.sin(2 * np.pi * f * t)
    return lowpass(s * env(len(t), 0.003, dur * 0.5), 2600)


def pad(midis, dur, level=1.0):
    t = tt(dur)
    s = np.zeros(len(t))
    for m in midis:
        for d in (-0.08, 0.0, 0.08):  # detuned saws
            ph = (hz(m + d) * t) % 1.0
            s += 2 * ph - 1
    s = lowpass(s / (3 * len(midis)), 900, 2)
    e = np.minimum(1, t / 0.9) * np.minimum(1, (dur - t) / 1.1).clip(0)
    return s * e * level


def noise(dur):
    return rng.uniform(-1, 1, int(dur * SR))


def kick():
    t = tt(0.45)
    f = 45 + 90 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), 0.002, 0.25)


def shaker():
    return highpass(noise(0.07), 6000) * env(int(0.07 * SR), 0.004, 0.03)


def click():
    return bandpass(noise(0.018), 2000, 7000) * env(int(0.018 * SR), 0.001, 0.008)


def send_sound():  # quick upward blip
    t = tt(0.16)
    f = 600 + 900 * t / 0.16
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), 0.004, 0.08)


def receive_sound():  # two-note ding
    return np.concatenate([bell(88, 0.12)[: int(0.09 * SR)], bell(93, 0.7)])


def whoosh(dur=0.5, lo=400, hi=4000):
    n = noise(dur)
    t = tt(dur)
    shape = np.sin(np.pi * t / dur) ** 2
    return bandpass(n, lo, hi) * shape


def riser(dur):
    t = tt(dur)
    f = 110 * (4 ** (t / dur))
    ph = np.cumsum(f) / SR
    saw = 2 * (ph % 1.0) - 1
    s = lowpass(saw, 2500) * (t / dur) ** 2
    return s + highpass(noise(dur), 3000) * (t / dur) ** 3 * 0.6


def boom():
    t = tt(1.4)
    f = 38 + 60 * np.exp(-t * 8)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), 0.003, 0.9)
    return body + lowpass(noise(1.4), 400) * env(len(t), 0.002, 0.35) * 0.9


def crackle(t0, dur, count, gain, seed):
    r = np.random.default_rng(seed)
    for _ in range(count):
        place(bandpass(noise(0.03), 2500, 9000) * env(int(0.03 * SR), 0.001, 0.01),
              t0 + r.uniform(0, dur), pan=r.uniform(-0.8, 0.8), gain=gain * r.uniform(0.3, 1), reverb=0.5)


# ---------- score ----------
A, F_, C, G, Dm, Em = [57, 60, 64], [53, 57, 60], [48, 55, 64], [55, 59, 62], [50, 57, 62], [52, 55, 59]

# Act 1–2: late night chat and the first captions (Am F C G)
for i, ch in enumerate([A, F_, C, G]):
    place(pad(ch, 3.4, 0.9), i * 2.8, gain=0.16, reverb=0.6)
    place(np.sin(2 * np.pi * hz(ch[0] - 12) * tt(3.0)) * env(int(3.0 * SR), 0.6, 2.5), i * 2.8, gain=0.08)

for m in TL["chat1"]["messages"] + TL["chat2"]["messages"]:
    place(send_sound() if m["from"] == "user" else receive_sound(), m["t"], pan=0.3 if m["from"] == "user" else -0.3,
          gain=0.22 if m["from"] == "user" else 0.12, reverb=0.25)
for a, b in TL["chat1"]["typing"] + TL["chat2"]["typing"]:
    r = np.random.default_rng(int(a * 100))
    x = a + 0.1
    while x < b - 0.1:
        place(click(), x, pan=-0.3, gain=0.10 * r.uniform(0.5, 1), reverb=0.1)
        x += r.uniform(0.07, 0.19)

# first star
place(bell(96, 2.5), TL["firstStar"], gain=0.12, reverb=0.8)

# Act 3: counting to 700. A tick every 10 stars, so ticks speed up with the count.
c0, c1 = TL["count"]
place(pad([53, 60, 65, 69], 3.3), c0, gain=0.14, reverb=0.6)
place(pad([55, 62, 67, 71], 3.0), c0 + 3.0, gain=0.16, reverb=0.6)
penta = [0, 2, 4, 7, 9]
last = -1
for k in range(1, 71):
    p = (k * 10 / 700) ** (1 / 1.7)
    at = c0 + p * (c1 - c0)
    if at - last < 0.045:
        continue
    last = at
    step = k // 5
    midi = 72 + penta[step % 5] + 12 * (step // 5) // 2
    place(pluck(min(midi, 100), 0.18), at, pan=np.sin(k) * 0.6, gain=0.09, reverb=0.35)

# Act 4: gather, burst, fireworks
g0, g1 = TL["gather"]
place(riser(g1 - g0), g0, gain=0.14, reverb=0.4)
bt = TL["burst"]
place(boom(), bt, gain=0.55, reverb=0.3)
for i, m in enumerate([60, 64, 67, 72, 76, 79, 84]):
    place(bell(m, 3.2), bt + 0.04 + i * 0.07, pan=(i - 3) * 0.2, gain=0.10, reverb=0.7)
place(pad([48, 55, 60, 64, 67], 3.4), bt, gain=0.18, reverb=0.7)
crackle(bt + 0.2, 1.8, 45, 0.18, 1)
for i, (at, fx, _) in enumerate(TL["fireworks"]):
    place(boom()[: int(0.6 * SR)], at, pan=fx * 2 - 1, gain=0.18, reverb=0.4)
    place(bell([79, 84, 76, 88][i], 1.5), at + 0.05, pan=fx * 2 - 1, gain=0.08, reverb=0.7)
    crackle(at + 0.1, 0.9, 14, 0.12, 10 + i)

# Overview wall: every entry in the list counts up
wl = TL.get("wall")
if wl:
    w0, w1 = wl["count"]
    for i, ch in enumerate([F_, G, A, C]):
        place(pad([m + 12 for m in ch], 1.9), wl["in"] + i * 1.6, gain=0.13, reverb=0.6)
    place(whoosh(0.8, 300, 3500), wl["in"] - 0.3, gain=0.16, reverb=0.3)
    total = json.loads((HERE / "wall.json").read_text())["total"]
    steps = 36
    for k in range(steps):
        p = k / (steps - 1)
        at = w0 + p * (w1 - w0)
        place(pluck(72 + penta[k % 5] + 12 * ((k // 5) % 2), 0.2), at, pan=np.sin(k * 1.7) * 0.7, gain=0.06, reverb=0.4)
    place(bell(84, 2.2), w1, gain=0.10, reverb=0.7)
    place(bell(88, 2.0), w1 + 0.05, gain=0.07, reverb=0.7)
    crackle(w1 + 0.3, 1.0, 16, 0.06, 7)

# September title
st0, st1 = TL["septTitle"]
place(whoosh(0.7, 300, 3000), st0 - 0.25, gain=0.18, reverb=0.3)
place(pad([53, 57, 60, 64], st1 - st0 + 0.8), st0 - 0.2, gain=0.16, reverb=0.6)
place(bell(81, 2.0), st0 + 0.1, gain=0.08, reverb=0.7)

# Act 5: eleven projects on a light groove (75 bpm, one project every two beats)
s0, step = TL["items"]["start"], TL["items"]["step"]
n_items = len(TL["projects"])
end5 = s0 + step * n_items
prog = [C, G, A, F_]
beat = step / 2
n_beats = int(round((end5 - s0) / beat))
for b in range(n_beats):
    at = s0 + b * beat
    ch = prog[(b // 4) % 4]
    place(kick(), at, gain=0.30 if b % 2 == 0 else 0.18, reverb=0.05)
    place(shaker(), at + beat / 2, pan=0.4, gain=0.08, reverb=0.1)
    place(shaker(), at + beat / 4 * 3, pan=-0.4, gain=0.04, reverb=0.1)
    notes = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[1] + 24]
    for k in range(4):  # 16th-note arpeggio
        place(pluck(notes[k], 0.35), at + k * beat / 4, pan=(k - 1.5) * 0.25, gain=0.055, reverb=0.35)
    if b % 4 == 0:
        place(pad(ch, beat * 4 + 0.6), at, gain=0.10, reverb=0.5)
        place(np.sin(2 * np.pi * hz(ch[0] - 12) * tt(beat * 4)) * env(int(beat * 4 * SR), 0.01, 2.0), at, gain=0.12)
melody = [76, 79, 81, 84, 81, 79, 76, 79, 81, 86, 88]
for i in range(n_items):
    at = s0 + i * step
    place(bell(melody[i], 1.4), at, pan=-0.2 if i % 2 else 0.2, gain=0.11, reverb=0.6)
    place(whoosh(0.35, 800, 6000), at - 0.18, gain=0.06, reverb=0.2)

# Thanks to the authors: warm chords and a bell as each avatar appears
th = TL.get("thanks_authors")
if th:
    for i, ch in enumerate([F_, C, G]):
        place(pad(ch, 2.3), th["in"] + i * 1.9, gain=0.15, reverb=0.6)
    for i in range(len(TL["authors"])):
        at = th["in"] + 0.6 + i * 0.28
        place(bell(72 + penta[i % 5] + 12 * (i // 5), 1.3), at, pan=(i - 3) * 0.2, gain=0.09, reverb=0.6)
    place(bell(79, 2.4), th["in"] + 2.9, gain=0.08, reverb=0.8)
    place(bell(84, 2.4), th["in"] + 3.0, gain=0.06, reverb=0.8)

# Act 6: back in the chat, soft chords (F G C)
c2 = TL["chat2"]["in"][0]
for i, ch in enumerate([F_, G, C]):
    place(pad(ch, 2.3), c2 + i * 1.9, gain=0.15, reverb=0.6)

# Act 7: end card
e = TL["end"]
for i, m in enumerate([60, 64, 67, 71, 74, 79]):
    place(bell(m, 4.0), e["in"] + i * 0.12, pan=(i - 2.5) * 0.25, gain=0.09, reverb=0.8)
place(pad([48, 55, 59, 62, 64], TL["duration"] - e["in"]), e["in"], gain=0.18, reverb=0.7)
place(bell(91, 3.0), e["cta"], gain=0.09, reverb=0.9)
crackle(e["cta"], 1.2, 20, 0.08, 99)

# ---------- mix ----------
ir_t = tt(2.2)
ir = np.stack([rng.normal(size=len(ir_t)), rng.normal(size=len(ir_t))], axis=1) * np.exp(-ir_t * 3.2)[:, None]
ir = np.stack([lowpass(ir[:, 0], 6000), lowpass(ir[:, 1], 6000)], axis=1)
ir /= np.sqrt((ir ** 2).sum(axis=0))
wet = np.stack([fftconvolve(wet_send[:, c], ir[:, c])[:N] for c in range(2)], axis=1)
mix = dry + wet * 0.9
mix = highpass(mix.T, 30).T
fade = TL["end"]["fade"]
t = np.arange(N) / SR
mix *= np.clip((TL["duration"] - t) / (fade[1] - fade[0] + 0.3), 0, 1)[:, None]
rms = np.sqrt((mix ** 2).mean())
mix *= 0.14 / rms                      # rough loudness target for phone speakers
mix = np.tanh(mix * 1.1) / np.tanh(1.1)  # soft limiter
mix *= 0.97 / np.abs(mix).max()

out = HERE / "out"
out.mkdir(exist_ok=True)
pcm = (mix * 32767).astype("<i2")
with wave.open(str(out / "soundtrack.wav"), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"wrote out/soundtrack.wav ({N / SR:.1f}s, rms {np.sqrt((mix ** 2).mean()):.3f})")
