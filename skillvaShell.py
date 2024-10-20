import llama
import synthesis
import voicer
import asyncio
from config import conf

def shell(model='C:\skillva\skillva\models\small_model_ru', micros=2):  
    while True:
        c = voicer.recording(model, micros)
        print(c)
        if "бот" in c:
            b = asyncio.run(llama.chat(c))
            synthesis.synthes(b)
            print(b)
        else :
            c = c.split()
            c.append('')
            
            if c[0] in conf:
                conf[c[0]][c[1]]()
            else :
                synthesis.synthes('Такой команды нет!')
    
    
if __name__ == '__main__':
    shell()