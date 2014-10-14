#-------------------------------------------------------------------------------
# Copyright:   (c)Manejando datos 2014
#-------------------------------------------------------------------------------
miVersion = "Ordenación de objetos con Python - version 0.2.0"

class Ejemplo():
    def __init__(self, campo1, campo2):
        self.campo1 = campo1
        self.campo2 = campo2
    def __str__(self):
        return "%s - %s" % (self.campo1, self.campo2)

    def __cmp__(self, other):
        if self.campo1 == other.campo1:
            return 1 if self.campo2 > other.campo2 else -1
        elif self.campo1 < other.campo1:
            return -1
        else:
            return 1

def lista(vv):
    """ Imprimimos la lista"""
    for v in vv:
        print (v)

# Definimos varios objetos
v1 = Ejemplo("rojo", 10)
v2 = Ejemplo("rojo", 8)
v3 = Ejemplo("rojo", 16)
v4 = Ejemplo("rojo", 11)
v5 = Ejemplo("amarillo", 10)
v6 = Ejemplo("amarillo", 8)
v7 = Ejemplo("verde", 14)
v8 = Ejemplo("verde", 12)
v9 = Ejemplo("verde", 8)

# Creamos la Lista
vv = [v1, v2, v3, v4, v5, v6, v7, v8, v9]
vv2 = sorted(vv, key=lambda objeto: objeto.campo1, reverse=True)
#lista(vv2)
print " -------"
vv3 = sorted(vv)
lista(vv3)
