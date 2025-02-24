import numpy as np
import matplotlib.pyplot as plt

range = np.linspace(1,21, 1000)
signal = 5 + 3* np.cos(4* np.pi* range) - 2* np.cos(2* np.pi* range)
noise = np.random.normal(0, 0.5, size = signal.shape)
observed_sig =  signal + noise

plt.style.use('ggplot')
plt.plot(range, signal)
plt.show()
def mydft_badway(signal:np.ndarray):
    """
    Compute the Discrete Fourier Transform(DFT) of of the given 1-D signal
    ___
    Input:
    * signal (1D numpy array): Signal to calculate the fourier transform for.

    Output:
    * DFT: The Computed DFT array  
    """
    # assert type(signal)
    assert len(signal.shape) ==1, "The signal is not one dimensional! I have been betrayed!"
    N = signal.shape[0]
    w = np.exp( -2*1j*np.pi/N)
    
