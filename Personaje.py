class Personaje:

    # ---------------- DEFINICION PERSONAJE ----------------
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = "gray"  # Color por defecto
        self.id_dibujo = None  # Referencia al dibujo en el canvas

    # ---------------- DIBUJAR PERSONAJE ----------------
    def dibujar(self):
        radio = 15
        x1, y1 = self.x - radio, self.y - radio
        x2, y2 = self.x + radio, self.y + radio

        self.id_dibujo = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="black")

    # ---------------- MOVIMIENTO PERSONAJE ----------------
    def mover(self, MovimientoX, MovimientoY):
        self.canvas.move(self.id_dibujo, MovimientoX, MovimientoY)
        self.x = self.x + MovimientoX
        self.y = self.y + MovimientoY

    # ---------------- COLISIONES ----------------
    def colisiona(self, proyectil):
        dx = abs(self.x - proyectil.x)
        dy = abs(self.y - proyectil.y)
        return dx < 25 and dy < 25
