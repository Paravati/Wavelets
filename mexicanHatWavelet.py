## Mexican hat wavelet
import numpy as np
import scipy
import scipy.fftpack
import matplotlib.pyplot as plt


fs = 1024
samples = fs * 5  # 5 seconds
freq = 6
# the wavelet
timevec = np.arange(0, samples) / fs
timevec = timevec - np.mean(timevec)   # centered time vector
# for power spectrum
hz = np.linspace(0, fs / 2, int(np.floor(samples / 2) + 1))
    
s = .4
MexicanWavelet = (2 / (np.sqrt(3 * s) * np.pi ** .25)) * (1 - (timevec ** 2) / (s ** 2)) * np.exp((-timevec ** 2) / (2 * s ** 2))

# amplitude spectrum
MexicanPow = np.abs(scipy.fftpack.fft(MexicanWavelet) / samples)

# time-domain plotting
plt.subplot(211)
plt.plot(timevec, MexicanWavelet, 'k')
plt.xlabel('Time (sec.)')
plt.title('Mexican wavelet in time domain')

# frequency-domain plotting
plt.subplot(212)
plt.plot(hz, MexicanPow[:len(hz)], 'k')
plt.xlim([0, freq * 3])
plt.xlabel('Frequency (Hz)')
plt.title('Mexican wavelet in frequency domain')
plt.show()