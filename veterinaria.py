class Perro():
    tipo = "Perro" #Atributos de clase
    def __init__(self,nombre, color):
        self.nombre=nombre
        self.color = color
    
    def hacer_sonido(self):
        return "Guau guau"

class Gato():
    tipo = "Gato"
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    def hacer_sonido_gato(self):
        return "Miau miau"

class Pez():
    tipo= "Pez"
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    def hacer_sonido_pez(self):
        return "Gloo gloo"
