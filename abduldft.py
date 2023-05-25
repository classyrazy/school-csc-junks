# CSC 225 ASSIGNMENT 
# NAME: MUSTAFA ABDULLAHI OLASUNKANMI
# MATRIC NO: 210806503
# DEPARTMENT: MATHEMATICS SCIENCE
# QUESTION: Develop a program to find the inverse of DFT... of x.

import time
import numpy as np

# Generate a random signal of length 2048
random_signal = np.random.rand(2048)

# Compute the FFT and time it
start_time_fft = time.time()
fft = np.fft.fft(random_signal)
fft_time = time.time() - start_time_fft

# Compute the DFT and time it
start_time_dft = time.time()
dft = np.zeros_like(fft)
signal_length = len(random_signal)
for k in range(signal_length):
    for n in range(signal_length):
        dft[k] += random_signal[n] * np.exp(-2j * np.pi * k * n / signal_length)
dft_time = time.time() - start_time_dft

# Compare the times
print("FFT time:", fft_time)
print("DFT time:", dft_time)