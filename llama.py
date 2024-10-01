import asyncio
from ollama import AsyncClient
import tensorflow as tf
import gc
from synthesis import synthes
from time import sleep


async def chat(promt):
    global a
    a = ''    
        
    async def chat1():
        gc.collect()


        tf.config.set_visible_devices([dev for dev in tf.config.list_physical_devices('GPU')], 'GPU')

        message = {
            "role": "user",
            "content": f"{promt}"
        }
        
        async for part in await AsyncClient().chat(
            model="llama3", messages=[message], stream=True
        ):
            global a
            a += part['message']['content']
    
    
    await chat1()
    return a
    



if __name__ == '__main__':
    print(asyncio.run(chat('Привет')))

    