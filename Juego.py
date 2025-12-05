import tkinter as tk
import random

from Personaje import Personaje

def obtener_posicion_random(self):
    """Genera coordenadas aleatorias dentro del canvas."""
    x = random.randint(50, 450)
    y = random.randint(50, 450)
    return x, y

ventana = tk.Tk() #Creamos la ventana.
ventana.title("Juego") #Le ponemos titulo a la ventana.
ventana.geometry("670x670") #Le damos un tamaño.
frame_control = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
escenario_canvas = tk.Canvas(ventana, width=670, height=620, bg="#2c3e50")
escenario_canvas.pack(fill=tk.BOTH, expand=True) # expand=True permite que crezca si la ventana cambia de tamaño



def crear_personaje():
    x, y = obtener_posicion_random(ventana)
    nuevoPersonaje = Personaje(escenario_canvas, x, y)
    nuevoPersonaje.dibujar()

def funcionBotonInicio():
    botonInicio.pack_forget()   # Oculta el botón
    crear_personaje()

botonInicio = tk.Button(
    frame_control, text="Iniciar", bg="#ff1800", fg="white", command=funcionBotonInicio)
botonInicio.pack(side=tk.TOP, padx=5)

ventana.mainloop() #Que no se cierre la ventana.