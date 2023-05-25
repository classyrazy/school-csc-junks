# CSC 225 ASSIGNMENT 
# NAME: MARTINS-IDOWU FUNKE GODSFAVOUR
# MATRIC NO: 190805053
# DEPARTMENT: COMPUTER SCIENCE
# QUESTION: Develop a program to find the inverse of DFT... of x.

import time
import numpy as np

# Generate a random signal of length 2048
random_signal = np.random.rand(2048)

# Compute the Fast Fourier Transform (FFT) and measure the time it takes
start_time_fft = time.time()
fft = np.fft.fft(random_signal)
elapsed_time_fft = time.time() - start_time_fft

# Compute the Discrete Fourier Transform (DFT) and measure the time it takes
start_time_dft = time.time()
dft = np.zeros_like(fft)
signal_length = len(random_signal)
for frequency in range(signal_length):
    for sample in range(signal_length):
        dft[frequency] += random_signal[sample] * np.exp(-2j * np.pi * frequency * sample / signal_length)
elapsed_time_dft = time.time() - start_time_dft

# Compare the elapsed times between the two transform methods
print("Elapsed time for FFT computation:", elapsed_time_fft)
print("Elapsed time for DFT computation:", elapsed_time_dft)