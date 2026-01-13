import random
from Entidad import Entidad

class Proyectil(Entidad):

    def __init__(self, canvas, lado=None):
        if lado is None:
            lado = random.choice(["arriba", "abajo", "izquierda", "derecha"])

        if lado == "arriba":
            x, y = random.randint(0, 768), -20
            dx, dy = 0, 2
        elif lado == "abajo":
            x, y = random.randint(0, 768), 532
            dx, dy = 0, -2
        elif lado == "izquierda":
            x, y = -20, random.randint(0, 512)
            dx, dy = 2, 0
        else:
            x, y = 788, random.randint(0, 512)
            dx, dy = -2, 0

        super().__init__(canvas, x, y, radio=10, color="black")

        self.dx = dx
        self.dy = dy

    def mover(self):
        super().mover(self.dx, self.dy)
