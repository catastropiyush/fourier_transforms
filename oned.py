import numpy as np

signal = np.arange(1,21)
noise = np.random.normal(0, 0.5, size = signal.shape)

observed_sig =  signal + noise

def mydft(signal):
    """
    Compute the Discrete Fourier Transform(DFT) of of the given 1-D signal
    ___
    Input:
    * signal (1D numpy array): Signal to calculate the fourier transform for.

    Output:
    * DFT: Compute the  
    """