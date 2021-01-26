import numpy as np
import scipy
import matplotlib.pyplot as plt


def morletWavelet(fs, npnts, plot=False):
    """ Morlet wavelet generator:
        fs - sampling frequency [Hz]
        npnts - number of points for signal creation"""

    # centered time vector
    timevec = np.arange(0, npnts) / fs
    timevec = timevec - np.mean(timevec)

    # for power spectrum
    hz = np.linspace(0, fs / 2, int(np.floor(npnts / 2) + 1))

    # parameters
    freq = 4  # peak frequency
    csw = np.cos(2 * np.pi * freq * timevec)  # cosine wave
    fwhm = .5  # full-width at half-maximum in seconds
    gaussian = np.exp(-(4 * np.log(2) * timevec ** 2) / fwhm ** 2)  # Gaussian

    # Morlet wavelet
    MorletWavelet = csw * gaussian

    # amplitude spectrum
    MorletWaveletPow = np.abs(scipy.fft(MorletWavelet) / npnts)

    if plot:
        # time-domain plotting
        plt.subplot(211)
        plt.plot(timevec, MorletWavelet, 'k')
        plt.xlabel('Time (sec.)')
        plt.title('Morlet wavelet in time domain')

        # frequency-domain plotting
        plt.subplot(212)
        plt.plot(hz, MorletWaveletPow[:len(hz)], 'k')
        plt.xlim([0, freq * 3])
        plt.xlabel('Frequency (Hz)')
        plt.title('Morlet wavelet in frequency domain')
        plt.show()


if __name__=="__main__":
    fs = 1024
    npnts = fs * 5  # 5 seconds
    morletWavelet(500, 500, True)