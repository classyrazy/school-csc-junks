import time
import numpy as np

# Generate a random signal of length 2048
signal = np.random.rand(2048)

# Compute the FFT and time it
start_time = time.time()
fft = np.fft.fft(signal)
fft_time = time.time() - start_time

# Compute the DFT and time it
start_time = time.time()
dft = np.zeros_like(fft)
N = len(signal)
for k in range(N):
    for n in range(N):
        dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
dft_time = time.time() - start_time

# Compare the times
print("FFT time:", fft_time)
print("DFT time:", dft_time)