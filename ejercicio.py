class Animal():
    def __init__(self, nombre, color, patas):
        self.nombre =nombre
        self.color =color
        self.patas =patas

class Conejo(Animal):
    def sonido(self):
        print("Snif snif!")
    
    def caracteristica(self):
        print(f"Mi conejo se llama {self.nombre}, es de color {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animal):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas)
        self.pico =pico
    
    def sonido(self):
        print("Cuak cuak mmmm")
    
    def caracteristicas(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es de color {self.color}, tiene {self.patas} patas y su pico mide {self.pico} cm")

class Dinosaurio(Animal):
    tipo = "Dinosaurio"

    def sonido(self):
        print("RAAAAR RAAAAR!")
    
    def caracteristicas(self):
        print(f"Mi dinosaurio se llama {self.nombre}, es de color {self.color}, tiene {self.patas} patas y es de tipo {Dinosaurio.tipo}")