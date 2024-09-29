
import datetime as dt
import os, math, platform

so = platform.system()
print(f"\nOS : {so}\n")
if so == "Windows":
    comando_limpa_tela = "cls"
else:
    comando_limpa_tela = "clear"

# PYGAME

import pyautogui as pyg
import pygame.mixer

pygame.init()

som_fim_estudo = pygame.mixer.Sound('MP3/fim_estudo.mp3')
som_fim_pausa = pygame.mixer.Sound('MP3/fim_pausa.mp3')
pygame.mixer.music.set_volume(0.5) # 0.0 - 1.0

# INPUTS 

tempo_e = int(input("TEMPO EM MINUTOS DE ESTUDO: "))
tempo_p = int(input("TEMPO EM MINUTOS DE PAUSA: "))
count = 1

while True:
    for s in range(1,tempo_e * 60,1):
        os.system(comando_limpa_tela)
        print(f"    POMODOR {tempo_e}/{tempo_p}\n")
        print("       ,--./,-.  ")
        print("      / #      \\")
        print("     |          |")
        print("      \\        /")
        print("       `._,._,'  ")
        tempo_falta_estudo = tempo_e * 60 - s
        min_e = math.floor(tempo_falta_estudo/60)
        tempo_falta_pausa = tempo_p * 60
        min_p = math.floor(tempo_falta_pausa / 60)
        print(f"\n--- ROUND {count}\n--- ESTUDO {min_e}:{tempo_falta_estudo - (min_e * 60)}\n--- PAUSA  {min_p}:{tempo_falta_pausa - (min_p * 60)}\n--- EXIT CTRL-C / CTRL-Z")
        pyg.sleep(1)
    som_fim_estudo.play()
    rangeP = tempo_p * 60
    for h in range(1,rangeP ,1):
        os.system(comando_limpa_tela)
        print(f"    POMODOR {tempo_e}/{tempo_p}\n")
        print("       ,--./,-.  ")
        print("      / #      \\")
        print("     |          |")
        print("      \\        /")
        print("       `._,._,'  ")
        tempo_falta_pausa = tempo_p * 60 - h
        min_p = math.floor(tempo_falta_pausa / 60)
        print(f"\n--- ROUND {count}\n--- ESTUDO {min_e}:{tempo_falta_estudo - (min_e * 60)}\n--- PAUSA  {min_p}:{tempo_falta_pausa - (min_p * 60)}\n--- EXIT CTRL-C / CTRL-Z")
        pyg.sleep(1)
    som_fim_pausa.play()
    count += 1

pygame.quit()