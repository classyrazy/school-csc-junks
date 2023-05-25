# CSC 225 ASSIGNMENT 
# NAME: ADEWALE ABDULRAZAQ OLABIYI
# MATRIC NO: 190806014
# DEPARTMENT: MATHEMATICS
# QUESTION: Develop a program to find the inverse of DFT... of x.

import time
import numpy as np

# Create a random signal of length 2048
signal = np.random.rand(2048)

# Compute the Fast Fourier Transform (FFT) and time it
start_time_fft = time.time()
fft = np.fft.fft(signal)
time_fft = time.time() - start_time_fft

# Compute the Discrete Fourier Transform (DFT) and time it
start_time_dft = time.time()
dft = np.zeros_like(fft)
N = len(signal)
for k in range(N):
    for n in range(N):
        dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
time_dft = time.time() - start_time_dft

# Compare the times
print("Time taken to compute FFT:", time_fft)
print("Time taken to compute DFT:", time_dft)