import pyaudio, numpy as np

p = pyaudio.PyAudio()

CHANNELS = 1 #number of audio channels (mono)
CHUNK = 512 #frames per buffer
FORMAT = pyaudio.paInt16

def recordSample(rec_len:int, SAMPLE_RATE:int):
    stream = p.open(
        channels = CHANNELS,
        format = FORMAT,
        rate = SAMPLE_RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK
        )

    print(f"recording sample {rec_len} s")
    chunks = list()
    for i in range(0, (SAMPLE_RATE//CHUNK)*rec_len):
        data = stream.read(CHUNK)
        samples = np.frombuffer(data, dtype=np.int16)
        chunks.append(samples)

    print("recording done!")

    stream.stop_stream()
    stream.close()
    p.terminate() #close PyAudio

    signal = np.concatenate(chunks)
    return signal
