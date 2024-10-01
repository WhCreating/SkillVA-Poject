import json, pyaudio
from vosk import Model, KaldiRecognizer
#import synthesis
#from llama import chat
import asyncio

def recording(models, micro: int):
	model = Model(models)
	rec = KaldiRecognizer(model, 16000)
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=10000, input_device_index=micro)
	stream.start_stream()

	def listen():
		while True:
			data = stream.read(4000, exception_on_overflow=False)
			if (rec.AcceptWaveform(data)) and (len(data) > 0):
				answer = json.loads(rec.Result())
				if answer['text']:
					yield answer['text']

			
	for text in listen():
		return text




if __name__=="__main__":
	print(recording('C:\\skillva\\skillva\\models\\small_model_ru', 2))