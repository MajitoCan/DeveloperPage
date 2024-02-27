import pyautogui as pg
import time
import random

for i in range(2500):
    time.sleep(3)
    pg.write(random.choice(["Comerte una pizza", "Correr por el campo", "Hacer algo productivo.", "Intentar","hablar con alguién.", "Socializar en Discord.", "Escuchar musica. (sin saltarte.)", "Hablar con tu hermano.", "Preguntar por tu abuela", "Hablar con tus padres.", "Intentar escribir una historia.", "Mejorar tu fightrole.", "Dormir temprano.", "Ahorarrar para una pc decente."]))
    pg.press("enter")
    