from humanidad import *

humano1 = Humano("Richi", 17, "Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero)
humano1.caract()
humano1.saludo()

programen1 = Programador("Chente", 19, "Masculino")
print(programen1.nombre)
print(programen1.edad)
print(programen1.genero)
programen1.caract()
programen1.saludo()
programen1.saludo2()

ing1 = Ingeniero("Elihud", 18, "Masculino", "Ciencias de la computación")
print(ing1.nombre)
print(ing1.edad)
print(ing1.genero)
print(ing1.tipo)
ing1.caract()
ing1.saludo()
