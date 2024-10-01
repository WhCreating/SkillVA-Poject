import llama
import synthesis
import voicer
import asyncio

while True:
    b = asyncio.run(llama.chat(voicer.recording('C:\skillva\skillva\models\small_model_ru', 2)))
    synthesis.synthes(b)
    print(b)