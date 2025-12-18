class Proyectil:


#DEFINICION PROYECTIL

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # Atributos encapsulados (datos del objeto)
        self.x = x
        self.y = y
        self.color = "black"  # Color por defecto
        self.id_dibujo = None  # Referencia al dibujo en el canvas


#DIBUJAR PERSONAJE

    def dibujar(self):
        lado = 15
        x1, y1 = self.x - lado, self.y - lado
        x2, y2 = self.x + lado, self.y + lado

        # Dibuja el círculo
        self.id_dibujo = self.canvas.create_square(x1, y1, x2, y2, fill=self.color, outline="black")
        # Dibuja el nombre encima
        self.canvas.create_text(self.x, self.y - 30, font=("Arial", 10, "bold"))


#MOVIMIENTO PERSONAJE

    def mover(self, MovimientoX, MovimientoY):
        self.canvas.move(self.id_dibujo, MovimientoX, MovimientoY)
        self.x = self.x + MovimientoX
        self.y = self.y + MovimientoY

