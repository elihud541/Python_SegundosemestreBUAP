from biblioteca import *

#Objetos
l1 = Libro("01", "Biblia", 1992, True, "Joseph Harrison", "12322193920292", "Historia")
l2 = Libro("02", "Cien años de soledad", 1967, True, "Gabriel Garcia Marquez", "9780307474728", "Realismo Magico")
l3 = Libro("03", "El resplandor", 1977, True, "Stephen King", "9780307743657", "Terror")
l4 = Libro("04", "El Hobbit", 1937, True, "J.R.R. Tolkien", "9780547928227", "Fantasia")
l5 = Libro("05", "1984", 1949, True, "George Orwell", "9780451524935", "Distopia")
l6 = Libro("06", "Don Quijote de la Mancha", 1605, True, "Miguel de Cervantes", "8420667130", "Clasico")
l7 = Libro("07", "El codigo Da Vinci", 2003, True, "Dan Brown", "9780307474278", "Misterio")
l8 = Libro("08", "Orgullo y Prejuicio", 1813, True, "Jane Austen", "9780141439518", "Romance")
l9 = Libro("09", "Crimen y Castigo", 1866, True, "Fiodor Dostoievski", "9788424921262", "Filosofico")
l10 = Libro("10", "El Principito", 1943, True, "Antoine de Saint-Exupéry", "9780156012195", "Infantil")
libros = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]

R1 = Revista("11", "Curiosamente", 2013, True, 150, "Mensual")
R2 = Revista("12", "National Geographic", 1888, True, 500, "Mensual")
R3 = Revista("13", "Muy Interesante", 1981, True, 450, "Mensual")
R4 = Revista("14", "Proceso", 1976, True, 2400, "Semanal")
R5 = Revista("15", "Scientific American", 1845, True, 120, "Mensual")
R6 = Revista("16", "Time", 1923, True, 5300, "Semanal")
R7 = Revista("17", "Forbes", 1917, True, 110, "Quincenal")
R8 = Revista("18", "Vogue", 1892, True, 980, "Mensual")
R9 = Revista("19", "Rolling Stone", 1967, True, 1300, "Mensual")
R10 = Revista("20", "PC World", 1983, True, 300, "Trimestral")
revistas=[R1,R2,R3,R4,R5,R6,R7,R8,R9,R10]

MD1 = Materialdigital("21", "Proyecto X", 2008, True, "PDF", "https://www.proyectox.com", 500.0)
MD2 = Materialdigital("22", "Curso Python Pro", 2024, True, "MP4", "https://biblioteca.edu/python", 1200.5)
MD3 = Materialdigital("23", "Ebook Redes", 2019, True, "EPUB", "https://descargas.net/redes", 15.2)
MD4 = Materialdigital("24", "Documental IA", 2023, True, "MKV", "https://ia-world.org/video", 4500.0)
MD5 = Materialdigital("25", "Tesis Ingenieria", 2022, True, "PDF", "https://buap.mx/tesis/101", 8.5)
MD6 = Materialdigital("26", "Podcast Tech", 2025, True, "MP3", "https://spotify.com/tech-daily", 60.0)
MD7 = Materialdigital("27", "Manual SQL", 2015, True, "PDF", "https://db-masters.com/manual", 12.4)
MD8 = Materialdigital("28", "Libro Cocina Digital", 2020, True, "AZW3", "https://amazon.com/cook-e", 25.0)
MD9 = Materialdigital("29", "Guia de Git", 2021, True, "PDF", "https://github.com/training/guide", 5.5)
MD10 = Materialdigital("30", "Charla TED: Futuro", 2026, True, "MP4", "https://ted.com/talks/future", 800.0)
digitales=[MD1,MD2,MD3,MD4,MD5,MD6,MD7,MD8,MD9,MD10]

U1 = Usuario("U01", "Daniel", 5) 
U2 = Usuario("U02", "Alejandro", 3)
U3 = Usuario("U03", "Mariana", 4)
U4 = Usuario("U04", "Roberto", 2)
U5 = Usuario("U05", "Fernanda", 6)
U6 = Usuario("U06", "Carlos", 3)
U7 = Usuario("U07", "Ximena", 5)
U8 = Usuario("U08", "Ricardo", 4)
U9 = Usuario("U09", "Sofía", 2)
U10 = Usuario("U10", "Mauricio", 7)
usuarios=[U1,U2,U3,U4,U5,U6,U7,U8,U9,U10]

B1 = Bibliotecario("B01", "Richi")
B2 = Bibliotecario("B02", "Ana")
B3 = Bibliotecario("B03", "Beto")
B4 = Bibliotecario("B04", "Clara")
B5 = Bibliotecario("B05", "David")
B6 = Bibliotecario("B06", "Elena")
B7 = Bibliotecario("B07", "Fernando")
B8 = Bibliotecario("B08", "Gaby")
B9 = Bibliotecario("B09", "Hugo")
B10 = Bibliotecario("B10", "Isabel")
bibliotecarios=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10]

S1 = Sucursal("S01", "Richi CU2")
S2 = Sucursal("S02", "Biblioteca Central")
S3 = Sucursal("S03", "Facultad de Computacion")
S4 = Sucursal("S04", "Area de Salud")
S5 = Sucursal("S05", "Sede Centro")
S6 = Sucursal("S06", "Complejo Cultural")
S7 = Sucursal("S07", "Prepa Benito Juarez")
S8 = Sucursal("S08", "Facultad de Ingenieria")
S9 = Sucursal("S09", "Sede Tehuacan")
S10 = Sucursal("S10", "Sede Atlixco")
sucursales=[S1,S2,S3,S4,S5,S6,S7,S8,S9,S10]

#Impresion de objetos
print("------------------ Instanciación de objetos ------------------")

print("\nLIBROS")
for x in libros:
   print(x.mostrarObjeto())

print("\nREVISTAS")
for x in revistas:
   print(x.mostrarObjeto())

print("\nMATERIAL DIGITAL")
for x in digitales:
   print(x.mostrarObjeto())

print("\nUSUARIOS")
for x in usuarios:
   print(x.mostrarObjeto())

print("\nBIBLIOTECARIOS")
for x in bibliotecarios:
   print(x.mostrarObjeto())

print("\nSUCURSALES")
for x in sucursales:
   print(x.mostrarObjeto())



#CATALOGO CON LOS OBJETOS YA CREADOS

catalogo_maestro = Catalogo()
catalogo_maestro.listaMaterialesGlobal = libros + revistas + digitales

S1.catalogoLocal = [l1, l2, R1, MD1]
S2.catalogoLocal = [l3, l4, R2, MD2]
S3.catalogoLocal = [l5, l6, R3, MD3]
S4.catalogoLocal = [l7, l8, R4, MD4]
S5.catalogoLocal = [l9, l10, R5, MD5]
S6.catalogoLocal = [R6]
S7.catalogoLocal = [R7]
S8.catalogoLocal = [R8]
S9.catalogoLocal = [R9]
S10.catalogoLocal = [R10]

for s in sucursales:
   s.catalogoLocal += digitales
#next es para buscar un objeto o elemento de un iterator mas o menos como un for
def menu():
    while True:
        print("\n-----------------------------------------------------------------------------")
        print("          SISTEMA BIBLIOTECARIO RichiBUAP")
        print("-----------------------------------------------------------------------------")
        print("1. Buscar Material por Título (En todas las sedes)")
        print("2. Buscar Libros por Autor")
        print("3. Realizar un Préstamo")
        print("4. Ver Préstamos Activos de un Usuario")
        print("5. Penalización (Entrega tardía)")
        print("6. Transferir Material entre Sucursales")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            nombre = input("¿Qué material buscas?: ")
            res = catalogo_maestro.BuscarPorTodasSucursales(nombre, sucursales)
            if res:
                print("\nResultados encontrados:")
                for r in res: print(f" = {r}")
            else:
                print("No se encontró ese material en ninguna sede.")

        elif opcion == "2":
            autor_buscado = input("Nombre del autor: ")
            libros_hallados = catalogo_maestro.BuscarporAutor(autor_buscado)
            if libros_hallados:
                for lib in libros_hallados:
                    print(f" = {lib.mostrarObjeto()}")
            else:
                print("No hay libros de ese autor en el catálogo.")

        elif opcion == "3":
            print("\n--- NUEVO PRÉSTAMO ---")
            id_u = input("ID del Usuario: ")
            id_m = input("ID del Material: ")
            
            usuario_obj = next((u for u in usuarios if u.idpersona == id_u), None)
            material_obj = next((m for m in catalogo_maestro.listaMaterialesGlobal if m.idMaterial == id_m), None)

            if usuario_obj and material_obj:
                B1.gestionarPrestamo(usuario_obj, material_obj, "19/03/2026", "26/03/2026")
            else:
                print("Error: Usuario o Material no encontrado")

        elif opcion == "4":
            id_u = input("ID del Usuario: ")
            usuario_obj = next((u for u in usuarios if u.idpersona == id_u), None)
            if usuario_obj:
                print(f"\nPrestamos de {usuario_obj.nombre}:")
                if not usuario_obj.listaActiva:
                    print("No tiene prestamos pendientes")
                for p in usuario_obj.listaActiva:
                    print(f" - Folio: {p.idPrestamo} | Material: {p.material.titulo} | Entrega: {p.fechaDevolucion}")

        elif opcion == "5":
            print("\n--- SIMULADOR DE MULTAS ---")
            id_u = input("ID del Usuario a multar: ")
            usuario_obj = next((u for u in usuarios if u.idpersona == id_u), None)
            if usuario_obj:
                dias = int(input("Cuantos dias de retraso?: "))
                multa = Penalizacion(0, "Retraso en entrega física")
                monto = multa.calcularMulta(dias)
                print(f"Multa generada: {monto}.00")
                multa.bloquearUsuario(usuario_obj)
            else:
                print("Usuario no encontrado")

        elif opcion == "6":
            print("\n--- TRANSFERENCIA DE MATERIAL ---")
            id_m = input("ID del Material a mover: ")
            #ID de sucursales ej: S01 maestro 
            id_s_origen = input("ID Sucursal Origen: ")
            id_s_destino = input("ID Sucursal Destino: ")

            mat = next((m for m in catalogo_maestro.listaMaterialesGlobal if m.idMaterial == id_m), None)
            orig = next((s for s in sucursales if s.idSucursal == id_s_origen), None)
            dest = next((s for s in sucursales if s.idSucursal == id_s_destino), None)

            if mat and orig and dest:
                B1.transferirMaterial(mat, orig, dest)
            else:
                print("Error material o sucursal no encontrada.")

        elif opcion == "0":
            print("Cerrando sistema... Exito en tu proyecto, BILIOTECARIO RICHI")
            break
        else:
            print("No existe esa funcion.")

menu()


