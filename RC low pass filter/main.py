import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq as fftffreq
from scipy.signal import find_peaks

threshold = 10
clean_signal = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 500))
noise = 0.8 * np.sin(2 * np.pi * 50 * np.linspace(0, 1, 500))

signal = clean_signal + noise
freq = fftffreq(len(signal), d=1/500)
magnitude = np.abs(fft(signal))

plt.plot(np.linspace(0, 1, 500), signal)
plt.title("Frequency Spectrum")
plt.xlabel("Time [s]")
plt.ylabel("Input Signal (V)")
plt.xlim(0, 1)
plt.grid()
plt.show()

peaks, properties = find_peaks(magnitude, height=threshold)
filter = []

for peak in peaks:
    if peak < threshold:
        filter.append(peak)

print("Detected Frequency Peaks Below Threshold: ")
for i in filter:
    print(i)