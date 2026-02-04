from veterinaria import Perro, Gato, Pez

perropug = Perro("Frida", "cafe")
perro2 = Perro("Leo", "negro")
perro3 = Perro("Richi", "gris")

lista_perro = [perropug, perro2, perro3]

for enun in lista_perro:
    print(f"Ese perro se llama {enun.nombre} y su color es {enun.color}, {enun.hacer_sonido()}")

gato1 = Gato("Nodal","amarillo")
gato2 = Gato("Belinda","cafe")
gato3 = Gato("Nata","miel")

lista_gato = [gato1, gato2, gato3]
for enun_gato in lista_gato:
    print(f"Ese gato se llama {enun_gato.nombre} y su color es {enun_gato.color}, {enun_gato.hacer_sonido_gato()}")

pez1 = Pez("GOLD","verde marino")
pez2 = Pez("Cabezon","plata silver")
pez3 = Pez("Pelotin","rojo almendrado")

lista_pez = [pez1,pez2,pez3]
for enun_pez in lista_pez:
    print(f"Ese pez se llama {enun_pez.nombre} y su color es {enun_pez.color}, {enun_pez.hacer_sonido_pez()}")
    

print(perro2.tipo)
print(gato1.tipo)
print(pez1.tipo)