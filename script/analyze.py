import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

def getMaxValueIndex(array) -> int:
    #get index of max value
    max_value_index = np.where(array == max(array))[0][0]
    return max_value_index

def calcFreqPeak(file:str) -> float:
    #read audio sample
    s_rate, signal = wavfile.read(file)

    #get wav amplitude
    FFT = abs(scipy.fft.fft(signal))
    #get wav frequency
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

    range = 1 #range of amplitudes to consider
    index = getMaxValueIndex(FFT)
    peak = freqs[index]
    return peak