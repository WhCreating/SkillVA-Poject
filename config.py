from config_main import *
from synthesis import synthes

conf = {
    "": lambda: print("Укажите голосовую команду!"),
    "привет": {"":lambda : synthes("Чем могу помочь?")},
    "открой": {'браузер':lambda : opens()}
    
    
    
}




