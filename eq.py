import pyaudio
import audioop
import math

def decb(micro:int):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = micro
    RATE = 44100
    RECORD_SECONDS = 2

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while True:
        data = stream.read(CHUNK, 
                        exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        decibel = 20 * math.log10(rms)
        print(decibel)

    stream.stop_stream()
    stream.close()
    p.terminate()
    
    
if __name__ == '__main__':
    decb(1)