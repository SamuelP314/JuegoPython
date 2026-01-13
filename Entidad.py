class Entidad:

    def __init__(self, canvas, x, y, radio, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.id_dibujo = None

    def dibujar(self):
        x1 = self.x - self.radio
        y1 = self.y - self.radio
        x2 = self.x + self.radio
        y2 = self.y + self.radio
        self.id_dibujo = self.canvas.create_oval(
            x1, y1, x2, y2,
            fill=self.color,
            outline="black"
        )

    def mover(self, dx, dy):
        self.canvas.move(self.id_dibujo, dx, dy)
        self.x += dx
        self.y += dy
