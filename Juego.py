import tkinter as tk
import random
from PIL import Image, ImageTk
from Personaje import Personaje


#VENTANA

ventana = tk.Tk()
ventana.title("Juego Bacteria")
ventana.geometry("768x512")
frame_control = tk.Frame(ventana, pady=20, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
escenario_canvas = tk.Canvas(ventana, width=768, height=512, bg="#00a310")
escenario_canvas.pack(fill=tk.BOTH, expand=True)

imagen_original = Image.open("Assets/bocadillo-lomo (1).jpg")
imagen_redimensionada = imagen_original.resize((768, 512))
fondo_img = ImageTk.PhotoImage(imagen_redimensionada)
escenario_canvas.create_image(0, 0, image=fondo_img, anchor="nw")

#PERSONAJE
personaje = None

def obtener_posicion_random():
    x = random.randint(50, 450)
    y = random.randint(50, 450)
    return x, y

def crear_personaje():
    global personaje
    x, y = obtener_posicion_random()
    personaje = Personaje(escenario_canvas, x, y)
    personaje.dibujar()


#BOTON INICIO

def funcionBotonInicio():
    botonInicio.pack_forget()
    frame_control.pack_forget()
    crear_personaje()
    mover_personaje()
    frame_control.config(height=0)


botonInicio = tk.Button(frame_control, text="Iniciar", bg="#ff1800", fg="white", command=funcionBotonInicio)
botonInicio.pack(side=tk.TOP, padx=5)


#MOVIMIENTO
teclas_presionadas = set()

def key_press(event):
    teclas_presionadas.add(event.keysym.lower())

def key_release(event):
    teclas_presionadas.discard(event.keysym.lower())

Velocidad = 3 #Son los ms en los que se recoge el input en ventana.after, cuanto menor es el delay, más rápido va.

def mover_personaje():
    if personaje is None:
        ventana.after(Velocidad, mover_personaje)
        return
    MovimientoX = 0
    MovimientoY = 0

    if ("w" in teclas_presionadas or "up" in teclas_presionadas) and personaje.y != 10:
        MovimientoY = MovimientoY - 1
    if ("s" in teclas_presionadas or "down" in teclas_presionadas) and personaje.y != 502:
        MovimientoY = MovimientoY + 1
    if ("a" in teclas_presionadas or "left" in teclas_presionadas) and personaje.x != 10:
        MovimientoX = MovimientoX - 1
    if ("d" in teclas_presionadas or "right" in teclas_presionadas) and personaje.x != 758:
        MovimientoX = MovimientoX + 1
    if MovimientoX != 0 or MovimientoY != 0:
        personaje.mover(MovimientoX, MovimientoY)
    ventana.after(Velocidad, mover_personaje)

ventana.bind("<KeyPress>", key_press)
ventana.bind("<KeyRelease>", key_release)

ventana.mainloop()