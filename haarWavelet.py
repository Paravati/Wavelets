## Haar wavelet

# create Haar wavelet
HaarWavelet = np.zeros(npnts)
HaarWavelet[np.argmin(timevec ** 2): np.argmin((timevec - .5) ** 2)] = 1
HaarWavelet[np.argmin((timevec - .5) ** 2): np.argmin((timevec - 1 - 1 / fs) ** 2)] = -1

# amplitude spectrum
HaarWaveletPow = np.abs(scipy.fftpack.fft(HaarWavelet) / npnts)

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