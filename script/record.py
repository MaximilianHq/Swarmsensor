import pyaudio, numpy as np

p = pyaudio.PyAudio()

CHANNELS = 1 #number of audio channels (mono)
CHUNK = 1024*2 #frames per buffer
FORMAT = pyaudio.paInt16 #sample size (2 bytes)
SAMPLE_RATE = 1024 #sample frequency

def recordSample(rec_len:int):
    stream = p.open(
        channels = CHANNELS,
        format = FORMAT,
        rate = SAMPLE_RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK
        )

    print("recording")
    print((SAMPLE_RATE/CHUNK)*rec_len)
    chunks = list()
    for i in range(0, int((SAMPLE_RATE/CHUNK)*rec_len)):
        data = stream.read(CHUNK)
        samples = np.frombuffer(data, dtype=np.int16)
        chunks.append(samples)

    print("recording done!")

    stream.stop_stream()
    stream.close()
    p.terminate() #close PyAudio

    signal = np.concatenate(chunks)
    return signal

    #obj = wave.open(f"{path}{audio_sample_name}.wav", "wb")
    #obj.setnchannels(CHANNELS)
    #obj.setsampwidth(p.get_sample_size(FORMAT))
    #obj.setframerate(SAMPLE_RATE)
    #obj.writeframes(b"".join(frames))
    #obj.close