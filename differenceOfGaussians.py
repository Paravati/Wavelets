import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
## Difference of Gaussians (DoG)
# (approximation of Laplacian of Gaussian)

# define sigmas
sPos = .1
sNeg = .5

# create the two GAussians
gaus1 = np.exp((-timevec ** 2) / (2 * sPos ** 2)) / (sPos * np.sqrt(2 * np.pi))
gaus2 = np.exp((-timevec ** 2) / (2 * sNeg ** 2)) / (sNeg * np.sqrt(2 * np.pi))

# their difference is the DoG
DoG = gaus1 - gaus2

# amplitude spectrum
DoGPow = np.abs(scipy.fftpack.fft(DoG) / npnts)

# time-domain plotting
plt.subplot(211)
plt.plot(timevec, DoG, 'k')
plt.xlabel('Time (sec.)')
plt.title('DoG wavelet in time domain')

# frequency-domain plotting
plt.subplot(212)
plt.plot(hz, DoGPow[:len(hz)], 'k')
plt.xlim([0, freq * 3])
plt.xlabel('Frequency (Hz)')
plt.title('DoG wavelet in frequency domain')
plt.show()