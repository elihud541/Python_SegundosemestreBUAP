class Persona():
    lista=[]
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def registrar(self):
        Persona.lista.append(self)
        print(f"La persona {self.nombre} ha sido rgistrada con el correo {self.correo}")
    
    def actualizar_datos(self,nombre,correo):
        self.nombre = nombre
        self.correo = correo
        print(f"Los datos han sido actualizados")

    @classmethod #Va a afectar toda la clase
    def personas_registradas(cls):
        print(f"Pesonas registradas")
        for x in cls.lista:
            print(f"-{x.nombre} - {x.correo}")