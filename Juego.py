import tkinter as tk
import random
from PIL import Image, ImageTk
from Personaje import Personaje
from Proyectil import Proyectil

# ---------------- VENTANA ----------------
ventana = tk.Tk()
ventana.title("Juego Bacteria")
ventana.geometry("768x512")

escenario_canvas = tk.Canvas(ventana, width=768, height=512)
escenario_canvas.pack(fill=tk.BOTH, expand=True)

# Fondo
imagen_original = Image.open("Assets/ImgFondo.png")
imagen_redimensionada = imagen_original.resize((768, 512))
fondo_img = ImageTk.PhotoImage(imagen_redimensionada)
escenario_canvas.create_image(0, 0, image=fondo_img, anchor="nw")

# Texto de inicio
titulo_inicio = escenario_canvas.create_text(
    384, 180,
    text="JUEGO BACTERIA",
    font=("Arial", 36, "bold"),
    fill="white"
)

texto_inicio = escenario_canvas.create_text(
    384, 240,
    text="Esquiva a los virus.\nUtiliza WASD o ← ↑ ↓ →",
    font=("Arial", 18, "bold"),
    fill="white",
    justify="center"
)

# ---------------- TEMPORIZADOR ----------------
tiempo_juego = 0
texto_tiempo = escenario_canvas.create_text(
    10, 10,
    text=f"Tiempo: {tiempo_juego}s",
    font=("Arial", 16, "bold"),
    fill="white",
    anchor="nw"
)

def actualizar_temporizador():
    global tiempo_juego
    if muerto:
        return
    tiempo_juego += 1
    escenario_canvas.itemconfig(texto_tiempo, text=f"Tiempo: {tiempo_juego}s")
    ventana.after(1000, actualizar_temporizador)

# ---------------- VELOCIDADES ----------------
velocidad = 3  # ms entre cada actualización del personaje
vel_proyectil = 20  # ms entre cada movimiento de proyectiles

# ---------------- BOTÓN INICIAR ----------------
muerto = False

def funcionBotonInicio():
    escenario_canvas.delete(titulo_inicio)
    escenario_canvas.delete(texto_inicio)
    botonInicio.destroy()

    personaje = crear_personaje()
    actualizar_temporizador()
    mover_personaje(personaje)
    proyectiles = []
    mover_proyectiles(proyectiles)
    generar_proyectiles(proyectiles)
    revisar_colisiones(personaje, proyectiles)

botonInicio = tk.Button(
    ventana,
    text="INICIAR",
    font=("Arial", 25, "bold"),
    bg="#ff1800",
    fg="white",
    command=funcionBotonInicio
)

botonInicio.place(relx=0.5, rely=0.65, anchor="center")

# ---------------- PERSONAJE ----------------
def crear_personaje():
    x = 384
    y = 256
    personaje = Personaje(escenario_canvas, x, y)
    personaje.dibujar()
    return personaje

teclas_presionadas = set()

def key_press(event):
    teclas_presionadas.add(event.keysym.lower())

def key_release(event):
    teclas_presionadas.discard(event.keysym.lower())

ventana.bind("<KeyPress>", key_press)
ventana.bind("<KeyRelease>", key_release)

def mover_personaje(personaje):
    if muerto:
        return

    dx = dy = 0
    if ("w" in teclas_presionadas or "up" in teclas_presionadas) and personaje.y > 10:
        dy -= 1
    if ("s" in teclas_presionadas or "down" in teclas_presionadas) and personaje.y < 502:
        dy += 1
    if ("a" in teclas_presionadas or "left" in teclas_presionadas) and personaje.x > 10:
        dx -= 1
    if ("d" in teclas_presionadas or "right" in teclas_presionadas) and personaje.x < 758:
        dx += 1

    if dx or dy:
        personaje.mover(dx, dy)

    ventana.after(velocidad, lambda: mover_personaje(personaje))

# ---------------- PROYECTILES ----------------
def crear_proyectil():
    lado = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    if lado == "arriba":
        x, y, dx, dy = random.randint(0, 768), -20, 0, 2
    elif lado == "abajo":
        x, y, dx, dy = random.randint(0, 768), 532, 0, -2
    elif lado == "izquierda":
        x, y, dx, dy = -20, random.randint(0, 512), 2, 0
    else:
        x, y, dx, dy = 788, random.randint(0, 512), -2, 0

    p = Proyectil(escenario_canvas, x, y)
    p.dibujar()
    return (p, dx, dy)

def mover_proyectiles(proyectiles):
    if muerto:
        return
    for p, dx, dy in proyectiles[:]:
        p.mover(dx, dy)
        if p.x < -30 or p.x > 800 or p.y < -30 or p.y > 550:
            escenario_canvas.delete(p.id_dibujo)
            proyectiles.remove((p, dx, dy))
    ventana.after(vel_proyectil, lambda: mover_proyectiles(proyectiles))

def generar_proyectiles(proyectiles):
    if muerto:
        return
    proyectiles.append(crear_proyectil())
    vel_gen = max(int(300 * (0.975 ** tiempo_juego)), 100)
    ventana.after(vel_gen, lambda: generar_proyectiles(proyectiles))

# ---------------- COLISIONES ----------------
def revisar_colisiones(personaje, proyectiles):
    if muerto:
        return
    for p, _, _ in proyectiles:
        if abs(personaje.x - p.x) < 20 and abs(personaje.y - p.y) < 20:
            pantalla_muerte(personaje, proyectiles)
            return
    ventana.after(velocidad, lambda: revisar_colisiones(personaje, proyectiles))

# ---------------- PANTALLA MUERTE ----------------
def pantalla_muerte(personaje, proyectiles):
    global muerto
    muerto = True
    escenario_canvas.itemconfig(texto_tiempo, state='hidden')

    escenario_canvas.delete(personaje.id_dibujo)
    for p, _, _ in proyectiles:
        escenario_canvas.delete(p.id_dibujo)
    proyectiles.clear()

    texto_muerte = escenario_canvas.create_text(
        384, 220,
        text=f"HAS MUERTO\nTiempo: {tiempo_juego}s",
        font=("Arial", 24, "bold"),
        fill="white",
        justify="center"
    )

    boton_reiniciar = tk.Button(
        ventana,
        text="REINICIAR",
        font=("Arial", 16, "bold"),
        bg="#ff1800",
        fg="white",
        command=lambda: reiniciar(texto_muerte, boton_reiniciar)
    )
    boton_reiniciar.place(relx=0.5, rely=0.65, anchor="center")

# ---------------- REINICIAR ----------------
def reiniciar(texto, boton):
    global muerto, tiempo_juego
    muerto = False
    tiempo_juego = 0
    escenario_canvas.itemconfig(texto_tiempo, text="Tiempo: 0s", state='normal')
    escenario_canvas.delete(texto)
    boton.destroy()

    personaje = crear_personaje()
    actualizar_temporizador()

    proyectiles = []
    mover_proyectiles(proyectiles)
    generar_proyectiles(proyectiles)
    revisar_colisiones(personaje, proyectiles)

    mover_personaje(personaje)

ventana.mainloop()