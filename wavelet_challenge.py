import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.io import loadmat
import scipy.signal as signal

# load the file
matfile = loadmat('wavelet_codeChallenge.mat')


signalOriginal = matfile['signal']
signalFIR = matfile['signalFIR']
signalMW = matfile['signalMW']  # signal with morlet wavelet applied
srate = matfile['srate'][0][0]
plt.figure(0)
plt.plot(signalOriginal)
plt.figure(1)
plt.plot(signalMW)




npnts = len(signalOriginal)

# centered time vector
timevec = np.arange(0,npnts)/srate
timevec = timevec - np.mean(timevec)

# for power spectrum
hz = np.linspace(0,srate/2,int(np.floor(npnts/2)+1))

## Morlet wavelet

# parameters
freq = 4 # peak frequency
csw  = np.cos(2*np.pi*freq*timevec) # cosine wave
fwhm = .5 # full-width at half-maximum in seconds
gaussian = np.exp( -(4*np.log(2)*timevec**2) / fwhm**2 ) # Gaussian

# Morlet wavelet
MorletWavelet = csw * gaussian

# amplitude spectrum
MorletWaveletPow = np.abs(scipy.fft(MorletWavelet)/npnts)


# time-domain plotting
plt.subplot(211)
plt.plot(timevec,MorletWavelet,'k')
plt.xlabel('Time (sec.)')
plt.title('Morlet wavelet in time domain')
plt.show()


# frequency-domain plotting
plt.subplot(212)
plt.plot(hz,MorletWaveletPow[:len(hz)],'k')
plt.xlim([0,freq*3])
plt.xlabel('Frequency (Hz)')
plt.title('Morlet wavelet in frequency domain')
plt.show()

# -----------------------------
# signal
signal1 = scipy.signal.detrend(np.cumsum(signalOriginal))
# convolve signal with different wavelets
morewav = np.convolve(signal1,MorletWavelet,'same')

# amplitude spectra
morewaveAmp = np.abs(scipy.fft(morewav)/npnts)




### plotting
# the signal
plt.plot(timevec,signal1,'k')
plt.title('Signal')
plt.xlabel('Time (s)')
plt.show()

# the convolved signals
plt.subplot(211)
plt.plot(timevec,morewav,label='Morlet')
plt.title('Time domain')
plt.legend()


# spectra of convolved signals
plt.subplot(212)
plt.plot(hz,morewaveAmp[:len(hz)],label='Morlet')
plt.yscale('log')
plt.xlim([0,40])
plt.legend()
plt.xlabel('Frequency (Hz.)')
plt.show()

