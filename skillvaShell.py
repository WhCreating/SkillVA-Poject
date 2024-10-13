import llama
import synthesis
import voicer
import asyncio

def shell(model='C:\skillva\skillva\models\model_ru', micros=2):  
    while True:
        c = voicer.recording(model, micros)
        print(c)
        if "бот" in c:
            b = asyncio.run(llama.chat(c))
            synthesis.synthes(b)
            print(b)
        else :
            synthesis.synthes("Укажите голосовую команду!")
    
    
if __name__ == '__main__':
    shell()