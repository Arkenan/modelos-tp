# Puntos bidimensionales.
class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def dist(self, otro):
        return abs(otro.x - self.x) + abs(otro.y - self.y)

# Nodo de dos puntos (origen y destino).
class Nodo:
    def __init__(self, cx, cy, dx, dy):
        self.c = Punto(cx, cy)
        self.d = Punto(dx, dy)

    def distancia(self, otro):
        return self.d.dist(otro.c)

    def distanciaInterna(self):
        return self.d.dist(self.c)
