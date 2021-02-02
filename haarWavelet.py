import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
## Haar wavelet
## Daubechie wavelet is haar wavelet with higher level of composition
# https://en.wikipedia.org/wiki/Daubechies_wavelet
# http://www.numerical-tours.com/matlab/wavelet_3_daubechies1d/


def haarWaveletCreating(samples, fs, freq):
    timevec = np.arange(0, samples) / fs
    timevec = timevec - np.mean(timevec)   # centered time vector

    # for power spectrum
    hz = np.linspace(0, fs / 2, int(np.floor(samples / 2) + 1))
    HaarWavelet = np.zeros(samples)
    HaarWavelet[np.argmin(timevec ** 2): np.argmin((timevec - .5) ** 2)] = 1
    HaarWavelet[np.argmin((timevec - .5) ** 2): np.argmin((timevec - 1 - 1 / fs) ** 2)] = -1

    # amplitude spectrum
    HaarWaveletPow = np.abs(scipy.fftpack.fft(HaarWavelet) / samples)

    # time-domain plotting
    plt.subplot(211)
    plt.plot(timevec, HaarWavelet, 'k')
    plt.xlabel('Time (sec.)')
    plt.title('Haar wavelet in time domain')

    # frequency-domain plotting
    plt.subplot(212)
    plt.plot(hz, HaarWaveletPow[:len(hz)], 'k')
    plt.xlim([0, freq * 3])
    plt.xlabel('Frequency (Hz)')
    plt.title('Haar wavelet in frequency domain')
    plt.show()


if __name__=="__main__":
    fs = 1024
    samp = fs * 5  # 5 seconds
    freq = 6  # peak frequency
    haarWaveletCreating(samp, fs, freq)