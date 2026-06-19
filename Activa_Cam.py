import tkinter as tk
import pygame

pygame.mixer.init()
edad = int(input("Que edad tienes: "))
if edad >= 18:
    print("Eres mayor")
elif edad == 14:
    pygame.mixer.music.load("Audio.mp3")
    pygame.mixer.music.play()
    ventana = tk.Tk()
    ventana.title("Tienes 14 activa cam")
    ventana.geometry("800x500")
    
    imagen_tk = tk.PhotoImage(file="14.png")
    etiqueta = tk.Label(ventana, image=imagen_tk)
    etiqueta.pack(pady=20)
    
    ventana.mainloop()
else:
    print("Eres joven")