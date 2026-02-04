from archivo1 import Alumno, Grupo #Esto es para llamar a una clase la cual esta en la misma carpeta pero otro archivo
# el * llama todas las clases
#cls en la terminal limpia todo

alumno1 = Alumno("Caro Sanchez", 12345)
alumno2 = Alumno("Ali Lopez", 54321)
alumno3 = Alumno("Richi Malo", 66666)
alumno4 = Alumno("Pequeño Leo", 69123)
alumno5 = Alumno("Poter Harry", 77777)

alumno1.agregar_calificacion(9.5)
alumno1.agregar_calificacion(8)
alumno1.agregar_calificacion(8.5)

alumno2.agregar_calificacion(10)
alumno2.agregar_calificacion(10)

alumno3.agregar_calificacion(6)
alumno3.agregar_calificacion(6)
alumno3.agregar_calificacion(6)
alumno3.agregar_calificacion(6)

alumno4.agregar_calificacion(8)
alumno4.agregar_calificacion(6)
alumno4.agregar_calificacion(5)

alumno5.agregar_calificacion(7)
alumno5.agregar_calificacion(9)
alumno5.agregar_calificacion(10)

lista_enunciado = [alumno1, alumno2, alumno3, alumno4, alumno5]

for enunciado in lista_enunciado:
    print(f"El alumno {enunciado.nombre} tiene promedio de: {enunciado.calcular_promedio():.2f} y esta {enunciado.estado_final()}")


grupo1 = Grupo("Progra")
grupo1.agregar_alumnos(alumno1)
grupo1.agregar_alumnos(alumno2)
grupo1.agregar_alumnos(alumno3)
grupo1.agregar_alumnos(alumno4)
grupo1.agregar_alumnos(alumno5)

print(grupo1.mostrar_promedio())
print(grupo1.mejor_alumno())