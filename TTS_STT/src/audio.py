import pyaudio
import wave
from time import sleep
#from llm import Translate



def Recording():
    FORMAT = pyaudio.paInt16  # Format of audio samples (16-bit signed integers)
    CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100              # Sample rate (samples per second)
    CHUNK = 1024              # Number of frames per buffer
    RECORD_SECONDS = 6        # Duration of recording in seconds



    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    wait = 3

    while True:
        print(f"Começando em {wait}")
        if wait <= 0:
            print("Recording...")
            break
        wait -= 1
        sleep(1)

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()

    stream.stop_stream()
    stream.close()

    WAVE_OUTPUT_FILENAME = "speech.wav"

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Recording saved as", WAVE_OUTPUT_FILENAME)

    p.terminate()
    return WAVE_OUTPUT_FILENAME
