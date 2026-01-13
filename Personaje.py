from Entidad import Entidad
from Proyectil import Proyectil

class Personaje(Entidad):

    # ---------------- DEFINICION PERSONAJE ----------------
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y, radio=15, color="gray")

    # ---------------- COLISIONES ----------------
    def colisiona(self, proyectil):
        if not isinstance(proyectil, Proyectil):
            return False

        dx = abs(self.x - proyectil.x)
        dy = abs(self.y - proyectil.y)
        return dx < 25 and dy < 25
