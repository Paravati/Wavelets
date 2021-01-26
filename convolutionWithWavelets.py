import numpy as np
import scipy
from scipy.signal import detrend
from scipy.fftpack import fft
import matplotlib.pyplot as plt


def signalConvolutionWithWavelet():
    fs = 1024
    npnts = fs * 5  # 5 seconds

    # centered time vector
    timevec = np.arange(0, npnts) / fs
    timevec = timevec - np.mean(timevec)

    # for power spectrum
    hz = np.linspace(0, fs / 2, int(np.floor(npnts / 2) + 1))

    ### create wavelets

    # parameters
    freq = 4  # peak frequency
    csw = np.cos(2 * np.pi * freq * timevec)  # cosine wave
    fwhm = .5  # full-width at half-maximum in seconds
    gaussian = np.exp(-(4 * np.log(2) * timevec ** 2) / fwhm ** 2)  # Gaussian

    ## Morlet wavelet
    MorletWavelet = csw * gaussian

    ## Haar wavelet
    HaarWavelet = np.zeros(npnts)
    HaarWavelet[np.argmin(timevec ** 2): np.argmin((timevec - .5) ** 2)] = 1
    HaarWavelet[np.argmin((timevec - .5) ** 2): np.argmin((timevec - 1 - 1 / fs) ** 2)] = -1

    ## Mexican hat wavelet
    s = .4
    MexicanWavelet = (2 / (np.sqrt(3 * s) * np.pi ** .25)) * (1 - (timevec ** 2) / (s ** 2)) * np.exp(
        (-timevec ** 2) / (2 * s ** 2))

    ## convolve with random signal

    # signal
    signal1 = scipy.signal.detrend(np.cumsum(np.random.randn(npnts)))

    # convolve signal with different wavelets
    morewav = np.convolve(signal1, MorletWavelet, 'same')
    haarwav = np.convolve(signal1, HaarWavelet, 'same')
    mexiwav = np.convolve(signal1, MexicanWavelet, 'same')

    # amplitude spectra
    morewaveAmp = np.abs(scipy.fftpack.fft(morewav) / npnts)
    haarwaveAmp = np.abs(scipy.fftpack.fft(haarwav) / npnts)
    mexiwaveAmp = np.abs(scipy.fftpack.fft(mexiwav) / npnts)

    ### plotting
    # the signal
    plt.plot(timevec, signal1, 'k')
    plt.title('Signal')
    plt.xlabel('Time (s)')
    plt.show()

    # the convolved signals
    plt.subplot(211)
    plt.plot(timevec, morewav, label='Morlet')
    plt.plot(timevec, haarwav, label='Haar')
    plt.plot(timevec, mexiwav, label='Mexican')
    plt.title('Time domain')
    plt.legend()

    # spectra of convolved signals
    plt.subplot(212)
    plt.plot(hz, morewaveAmp[:len(hz)], label='Morlet')
    plt.plot(hz, haarwaveAmp[:len(hz)], label='Haar')
    plt.plot(hz, mexiwaveAmp[:len(hz)], label='Mexican')
    plt.yscale('log')
    plt.xlim([0, 40])
    plt.legend()
    plt.xlabel('Frequency (Hz.)')
    plt.show()


def narrowbandFiltering():
    # simulation parameters
    srate = 4352  # hz
    npnts = 8425
    time = np.arange(0, npnts) / srate
    hz = np.linspace(0, srate / 2, int(np.floor(npnts / 2) + 1))

    # pure noise signal
    signal1 = np.exp(.5 * np.random.randn(npnts))

    # let's see what it looks like
    plt.subplot(211)
    plt.plot(time, signal1, 'k')
    plt.xlabel('Time (s)')

    # in the frequency domain
    signalX = 2 * np.abs(scipy.fftpack.fft(signal1))
    plt.subplot(212)
    plt.plot(hz, signalX[:len(hz)], 'k')
    plt.xlim([1, srate / 6])
    plt.ylim([0, 300])
    plt.xlabel('Frequency (Hz)')
    plt.show()

    ## create and inspect the Morlet wavelet

    # wavelet parameters
    ffreq = 34  # filter frequency in Hz
    fwhm = .12  # full-width at half-maximum in seconds
    wavtime = np.arange(-3, 3, 1 / srate)  # wavelet time vector (same sampling rate as signal!)

    # create the wavelet
    morwav = np.cos(2 * np.pi * ffreq * wavtime) * np.exp(-(4 * np.log(2) * wavtime ** 2) / fwhm ** 2)

    # amplitude spectrum of wavelet
    # (note that the wavelet needs its own hz because different length)
    wavehz = np.linspace(0, srate / 2, int(np.floor(len(wavtime) / 2) + 1))
    morwavX = 2 * np.abs(scipy.fftpack.fft(morwav))

    # plot it!
    plt.subplot(211)
    plt.plot(wavtime, morwav, 'k')
    plt.xlim([-.5, .5])
    plt.xlabel('Time (sec.)')

    plt.subplot(212)
    plt.plot(wavehz, morwavX[:len(wavehz)], 'k')
    plt.xlim([0, ffreq * 2])
    plt.xlabel('Frequency (Hz)')
    plt.show()

    ## now for convolution

    convres = scipy.signal.convolve(signal1, morwav, 'same')

    # show in the time domain
    plt.subplot(211)
    plt.plot(time, convres, 'r')

    # and in the frequency domain
    plt.subplot(212)
    convresX = 2 * np.abs(scipy.fftpack.fft(convres))
    plt.plot(hz, convresX[:len(hz)], 'r')
    plt.show()
    ### Time-domain wavelet normalization is... annoying and difficult.
    ### Let's do it in the frequency domain

    ### "manual" convolution

    nConv = npnts + len(wavtime) - 1
    halfw = int(np.floor(len(wavtime) / 2))

    # spectrum of wavelet
    morwavX = scipy.fftpack.fft(morwav, nConv)

    # now normalize in the frequency domain
    morwavX = morwavX / np.max(morwavX)
    # also equivalent:
    morwavX = (np.abs(morwavX) / max(np.abs(morwavX))) * np.exp(1j * np.angle(morwavX))

    # now for the rest of convolution
    convres = scipy.fftpack.ifft(morwavX * scipy.fftpack.fft(signal1, nConv))
    convres = np.real(convres[halfw:-halfw + 1])

    # time domain
    plt.plot(time, signal1, 'k', label='original')
    plt.plot(time, convres, 'b', label='filtered, norm.')
    plt.legend()
    plt.xlabel('Time')

    # frequency domain
    convresX = 2 * np.abs(scipy.fftpack.fft(convres))
    plt.plot(hz, signalX[:len(hz)], 'k', label='original')
    plt.plot(hz, convresX[:len(hz)], 'b', label='filtered, norm.')
    plt.ylim([0, 300])
    plt.xlim([0, 90])

    ## to preserve DC offset, compute and add back
    convres = convres + np.mean(signal1)

    plt.plot(time, signal1, 'k', label='original')
    plt.plot(time, convres, 'm', label='filtered, norm.')
    plt.legend()
    plt.xlabel('Time')

    plt.show()


if __name__ == "__main__":
    narrowbandFiltering()
    signalConvolutionWithWavelet()
