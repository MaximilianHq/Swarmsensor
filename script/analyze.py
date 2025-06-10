import matplotlib.pyplot as plt
import scipy
import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(__file__) #absolute dir of script
data_path = os.path.join(script_dir, 'data/20250610/meta_20250610.csv')

def getMaxValueIndex(array) -> int:
    #get index of max value
    max_value_index = np.where(array == max(array))[0][0]
    return max_value_index


meta_data = pd.read_csv(data_path)
data=0

for i, meta in meta_data.iterrows():
    filename = meta['sample id']
    data = np.load(os.path.join(script_dir, f'data/20250610/{filename}'))

    data_transformed = np.fft.fft(data)
    magnitude = np.abs(data_transformed[:len(data)//2])
    freqs = np.fft.fftfreq(len(data), meta['sample rate']**-1)[:len(data)//2]

    peak_index = np.argmax(magnitude)
    peak_freq = freqs[peak_index]

    print(f"Dominerande frekvens: {peak_freq:.1f} Hz")

    plt.figure()
    plt.plot(freqs,magnitude)
    plt.title(meta['sample rate'])

plt.show()