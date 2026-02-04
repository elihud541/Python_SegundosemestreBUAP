from atributos import *

per1 = Nombre("Richi", 69,"Mister sex")
per2 = Nombre("Leo", 8,"Zootecnia")
per3 = Nombre("Melca", 18,"Mister sex")

print(str(per1))
print(repr(per2))
print(per1+per2)
print(per2*per3)

print(per1==per3)
print(per1==per2)