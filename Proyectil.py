import random

class Proyectil:

    # ---------------- DEFINICION PROYECTIL ----------------

    def __init__(self, canvas, lado=None):
        self.canvas = canvas
        self.color = "Black"
        self.id_dibujo = None

        if lado is None:
            lado = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        self.lado = lado

        if lado == "arriba":
            self.x = random.randint(0, 768)
            self.y = -20
            self.dx, self.dy = 0, 2
        elif lado == "abajo":
            self.x = random.randint(0, 768)
            self.y = 532
            self.dx, self.dy = 0, -2
        elif lado == "izquierda":
            self.x = -20
            self.y = random.randint(0, 512)
            self.dx, self.dy = 2, 0
        else:  # derecha
            self.x = 788
            self.y = random.randint(0, 512)
            self.dx, self.dy = -2, 0

    # ---------------- DIBUJAR PERSONAJE ----------------

    def dibujar(self):
        radio = 10
        x1, y1 = self.x - radio, self.y - radio
        x2, y2 = self.x + radio, self.y + radio

        self.id_dibujo = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="black")

    # ---------------- MOVIMIENTO PROYECTIL ----------------

    def mover(self):
        self.canvas.move(self.id_dibujo, self.dx, self.dy)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
