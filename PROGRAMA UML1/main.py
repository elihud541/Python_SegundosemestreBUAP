from Cine import *

def ejecutar_sistema():
    #Profe puede utilizar empleados o usuarios(Se puede registrar)
    e1 = Empleado.registrar_empleado("E01", "Freedy", "f@cinecu2.com", "101", "EMP01", "Taquillero", "Matutino")
    e2 = Empleado.registrar_empleado("E02", "Erick", "e@cinecu2.com", "102", "EMP02", "Admin", "Completo")
    e3 = Empleado.registrar_empleado("E03", "Pug", "p@cinecu2.com", "103", "EMP03", "Limpieza", "Nocturno")
    e4 = Empleado.registrar_empleado("E04", "Juan", "j@cinecu2.com", "104", "EMP04", "Taquillero", "Vespertino")
    e5 = Empleado.registrar_empleado("E05", "Ponce", "p@cinecu2.com", "105", "EMP05", "Admin", "Matutino")
    e6 = Empleado.registrar_empleado("E06", "Leo", "l@cinecu2.com", "106", "EMP06", "Limpieza", "Matutino")
    e7 = Empleado.registrar_empleado("E07", "Paco", "p@cinecu2.com", "107", "EMP07", "Taquillero", "Nocturno")
    e8 = Empleado.registrar_empleado("E08", "Yamil", "y@cinecu2.com", "108", "EMP08", "Admin", "Vespertino")
    e9 = Empleado.registrar_empleado("E09", "Ali", "a@cinecu2.com", "109", "EMP09", "Limpieza", "Vespertino")
    e10 = Empleado.registrar_empleado("E10", "Richi", "r@cinecu2.com", "110", "EMP10", "Admin", "Completo")

#Numeros del edomex
    u1 = Usuario.registrar_usuario("U01", "Ana", "ana@gmail.com", "55-5555-01", 150, 1)
    u2 = Usuario.registrar_usuario("U02", "Bob", "bob@gmail.com", "55-5554-02", 20, 2)
    u3 = Usuario.registrar_usuario("U03", "Carla", "carla@gmail.com", "55-5565-03", 500, 4)
    u4 = Usuario.registrar_usuario("U04", "Diego", "diego@gmail.com", "55-5585-04", 0, 4)
    u5 = Usuario.registrar_usuario("U05", "Elena", "elena@gmail.com", "55-5525-05", 85, 3)
    u6 = Usuario.registrar_usuario("U06", "Fabio", "fabio@gmail.com", "55-5155-06", 1200,3)
    u7 = Usuario.registrar_usuario("U07", "Gaby", "gaby@gmail.com", "55-5355-07", 300,0)
    u8 = Usuario.registrar_usuario("U08", "Hugo", "hugo@gmail.com", "55-5455-08", 45,9)
    u9 = Usuario.registrar_usuario("U09", "Iris", "iris@gmail.com", "55-5555-09", 10,6)
    u10 = Usuario.registrar_usuario("U10", "Juan", "juan@gmail.com", "55-4555-10", 250,0)

    p1 = Pelicula("Avengers: Endgame", 180, "B", "Acción")
    p2 = Pelicula("Toy Story 4", 90, "A", "Animación")
    p3 = Pelicula("John Wick 4", 169, "C", "Acción")
    p4 = Pelicula("Spider-Man: No Way Home", 148, "B", "Ciencia Ficción")
    p5 = Pelicula("El Conjuro 3", 112, "C", "Terror")
    p6 = Pelicula("Super Mario Bros", 92, "A", "Aventura")
    p7 = Pelicula("Oppenheimer", 180, "B", "Drama")
    p8 = Pelicula("Barbie", 114, "A", "Comedia")
    p9 = Pelicula("Avatar 2", 192, "B", "Ciencia Ficción")
    p10 = Pelicula("Duna: Parte 2", 166, "B", "Épico")

    s1 = Sala("S01", "Mega IMAX", "Piso 1", "IMAX", 100, True)
    s2 = Sala("S02", "General 2D", "Piso 1", "2D", 50, False)
    s3 = Sala("S03", "General 2D", "Piso 1", "2D", 50, False)
    s4 = Sala("S04", "Premium 3D", "Piso 2", "3D", 60, True)
    s5 = Sala("S05", "VIP 3D", "Piso 2", "2D", 30, True)
    s6 = Sala("S06", "IMAX", "Piso 2", "2D", 70, True)
    s7 = Sala("S07", "SUPER PREMIUM RICHI 3D", "Piso 3", "2D", 120, True)
    s8 = Sala("S08", "2D", "Piso 3", "3D", 45, False)
    s9 = Sala("S09", "3D ULTIMATE", "Piso 3", "2D", 20, True)
    s10 = Sala("S10", "2D POBRECITO", "Piso 1", "2D", 25, True)
    
    lista_salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

    f1 = Funcion("F01", p1, s1, "14:00", 150)
    f2 = Funcion("F02", p2, s6, "11:00", 80)
    f3 = Funcion("F03", p3, s8, "22:00", 220)
    f4 = Funcion("F04", p4, s7, "16:00", 130)
    f5 = Funcion("F05", p5, s4, "23:00", 140)
    f6 = Funcion("F06", p6, s2, "10:00", 90)
    f7 = Funcion("F07", p7, s10, "19:00", 110)
    f8 = Funcion("F08", p8, s5, "17:00", 250)
    f9 = Funcion("F09", p9, s1, "20:00", 180)
    f10 = Funcion("F10", p10, s9, "18:30", 120)
    
    lista_funciones = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

    dict_comida = {
        "Palomitas RICHIENDES": 90, "Palomitas MediCapinas": 70, "Refresco RICHIXL": 60,
        "Hot Dog Doble": 85, "Nachos con Queso": 75, "Combo Pareja CAPI": 250,
        "Chocolate Barra": 40, "Agua Embotellada Erick": 35, "Ice Cereza": 55, "Dulces Gomitas": 45
    }
    zona_comida = Zona_Comida("ZC01", "RichiSnacks", "Piso 2", list(dict_comida.keys()), dict_comida)

    pr1 = Promocion("CINE10", "10% dto en Boletos", 0.10, "2026-12-31")
    pr2 = Promocion("ESTUDIANTE_CU2", "15% dto Estudiantes", 0.15, "2026-06-30")
    pr3 = Promocion("SOCIO_val", "20% dto Socios VIP", 0.20, "2026-12-31")
    pr4 = Promocion("LUNES_Carnitas", "Lunes de 2x1 (50% dto)", 0.50, "2026-12-31")
    pr5 = Promocion("CUMPLE_Paco", "Regalo Cumpleaños 30% dto", 0.30, "2026-12-31")
    pr6 = Promocion("MAÑANA_Fria", "Funciones Matutinas 25% dto", 0.25, "2026-05-01")
    pr7 = Promocion("SNACK5_Capi", "5% dto extra en snacks", 0.05, "2026-12-31")
    pr8 = Promocion("RECARGA_AL_MIL", "12% dto recarga puntos", 0.12, "2026-12-31")
    pr9 = Promocion("FESTIVO_RICHIER", "Día Festivo 18% dto", 0.18, "2026-12-31")
    pr10 = Promocion("ULTRA_MEGA_PESADO", "Pase Ultra 40% dto", 0.40, "2026-12-31")
    
    lista_promociones = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]

#Aqui esta la instancia que usted pide maestro

    print("----------- Imprimir los objetos del programa (Evidencia de Instanciación). ------------")
    print("EMPLEADOS:")
    for e in [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]:
        print(e.mostrar_detalle())

    print("\nUSUARIOS:")
    for u in [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]:
        print(u.mostrar_detalle())

    print("\nPELICULAS:")
    for p in [p1,p2, p3, p4, p5, p6,p7,p8,p9,p10]:
        print(p.mostrar_detalle())

    print("\nSALAS:")
    for s in[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]:
        print(s.mostrar_detalle())

    print("\nFUNCIONES:")
    for f in [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]:
        print(f.mostrar_detalle())

    print("\nPROMOCIONES:")
    for pr in [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9,pr10]:
        print(pr.mostrar_detalle())

    while True:
        print("**********************************")
        print("   SISTEMA DEL CINE RICHIXCAPI")
        print("**********************************")
        print("1. Nuevo Registro (Cliente)")
        print("2. Nuevo Registro (Empleado)")
        print("3. Iniciar Sesión")
        print("4. Cerrar todo")
        
        op = input("\nElige una opción: ")

        if op == "4":
            print("\nSaliendo del sistema... ¡Nos vemos CAPI!")
            break

        if op == "1":
            print("\n--- Registro Cliente ---")
            id_u = input("ID: ")
            if any(str(p.id_persona) == str(id_u) for p in Persona.listas_personas):
                print("Ese ID ya existe.")
            else:
                nom = input("Nombre: "); em = input("Email: "); tl = input("Tel: ")
                Usuario.registrar_usuario(id_u, nom, em, tl, 0, [])
                print("Listo, usuario creado.")
            input("Presiona ENTER...")

        elif op == "2":
            print("\n--- Registro Empleado ---")
            id_u = input("ID Persona: ")
            if any(str(p.id_persona) == str(id_u) for p in Persona.listas_personas):
                print("Ese ID ya existe.")
            else:
                nom = input("Nombre: "); em = input("Email: "); tl = input("Tel: ")
                id_e = input("ID Empleado: "); rol = input("Rol: "); hor = input("Horario: ")
                Empleado.registrar_empleado(id_u, nom, em, tl, id_e, rol, hor)
                print("Empleado registrado.")
            input("ENTER para seguir...")

        elif op == "3":
            print("\n--- LOGIN ---")
            id_log = input("ID: ")
            mail_log = input("Email: ")
            
            user_actual = None
            for persona in Persona.listas_personas:
                if str(persona.id_persona) == str(id_log) and persona.email == mail_log:
                    user_actual = persona
            
            if user_actual is None:
                print("No se encontró el usuario.")
                continue

            if isinstance(user_actual, Empleado):
                while True:
                    print(f"\nMENU EMPLEADO: {user_actual.nombre}")
                    print("1. Marcar entrada", "2. Funciones (Admin)", "3. Gestión de Salas (Aforo/Tipo)", "4. Limpieza","5. Actualizar Mis Datos","6. Gestionar Inventario Comida" ,"7. Salir", sep="\n")
                    sub = input("Opción: ")
                    
                    if sub == "1":
                        user_actual.marcarEntrada()
                    elif sub == "2":
                        if user_actual.rol == "Admin":
                            for f in lista_funciones: print(f"{f.idFuncion}: {f.pelicula.titulo}")
                            f_id = input("ID Función: ")
                            f_sel = next((f for f in lista_funciones if f.idFuncion == f_id), None)
                            if f_sel: user_actual.gestionarFunciones(f_sel, "ajuste de sala")
                        else:
                            print("Solo para Admins.")
                    elif sub == "3":
                        print("\n--- Gestión de Salas ---")
                        for s in lista_salas: print(f"{s.idEspacio}: {s.nombre}")
                        s_id = input("ID de la sala a gestionar: ")
                        s_sel = next((s for s in lista_salas if s.idEspacio == s_id), None)
                        if s_sel:
                            print(f"Sala actual: {s_sel.nombre} | Tipo: {s_sel.obtenerTipoSala()}")
                            nv_aforo = int(input(f"Nuevo aforo (Actual: {s_sel.capacidad}): "))
                            s_sel.ajustarAforo(nv_aforo)
                        else:
                            print("Sala no encontrada.")
                    elif sub == "4":
                        if user_actual.rol in ["Admin", "Limpieza"]:
                            for s in lista_salas: print(f"{s.idEspacio} - {s.nombre} (Limpia: {s.esta_limpio})")
                            s_id = input("ID Sala: ")
                            s_sel = next((s for s in lista_salas if s.idEspacio == s_id), None)
                            if s_sel: s_sel.limpiarEspacio()
                        else:
                            print("Sin permisos.")
                    
                    elif sub == "5":
                        print("\n--- Actualizar Datos --- (Deja en blanco para no cambiar)")
                        n = input("Nuevo Nombre: ")
                        e = input("Nuevo Email: ")
                        t = input("Nuevo Teléfono: ")
                        user_actual.actualizarDatos(n or None, e or None, t or None)
                    elif sub == "6":
                        print("\n--- Inventario de Zona de Comida ---")
                        for prod, cant in zona_comida.stockActual.items():
                            print(f"- {prod}: {cant} unidades")
                        nom_prod = input("\nNombre del producto (ej: Palomitas): ")
                        cant_prod = int(input(f"Cantidad a sumar para '{nom_prod}': "))
                        zona_comida.actualizarInventario(nom_prod, cant_prod)
                    elif sub == "7":
                        user_actual.logout()
                        break
                    input("Presiona ENTER...")

            elif isinstance(user_actual, Usuario):
                while True:
                    print(f"\nMENU CLIENTE: {user_actual.nombre} | Puntos: {user_actual.puntosFidelidad}")
                    print("1. Comprar boletos", "2. Comida", "3. Promos", "4. Mis Reservas","5. Actualizar Mis Datos","6. Cancelar Reservas" ,"7. Salir", sep="\n")
                    sub = input("Opción: ")
                    
                    if sub == "1":
                        print("--- Cartelera y Detalles de Funciones ---")
                        for f in lista_funciones: 
                            detalles = f.obtenerDetallesFuncion()
                            sinopsis = f.pelicula.obtenerSinopsis()
                            apta = "APTA (A)" if f.pelicula.esAptaParaTodoPublico() else "RESTRINGIDA"
                            
                            print(f"- {detalles}")
                            print(f"  Info: {sinopsis} | {apta} | Precio: ${f.precioBase}")
                            print("-" * 50)
                        
                        f_id = input("\nIngresa el ID de la función: ")
                        f_sel = next((f for f in lista_funciones if f.idFuncion == f_id), None)
                        
                        if f_sel:
                            libres = f_sel.calcularAsientosLibres()
                            print(f"Asientos disponibles: {libres}")
                            
                            cant = int(input("¿Cuántos boletos quieres?: "))
                            
                            if cant <= libres:
                                res = Reserva(f"R-{f_id}-{user_actual.id_persona}", user_actual, f_sel, cant)
                                
                                if input("¿Código de Promo? (s/n): ").lower() == 's':
                                    cod = input("Código: ")
                                    pr_sel = next((p for p in lista_promociones if p.codigo == cod), None)
                                    if pr_sel: res.aplicarPromocion(pr_sel)
                                
                                if res.confirmarPago():
                                    user_actual.crearReserva(res)
                                    print(res.generarTicket())
                            else:
                                print(f"¡Error! No hay suficientes asientos. Solo quedan {libres}.")
                        else:
                            print("Esa función no existe, Capi.")
                    elif sub == "2":
                        for prod in zona_comida.stockActual: print(f"- {prod}")
                        zona_comida.venderProducto(input("¿Qué quieres?: "))
                    elif sub == "3":
                        for p in lista_promociones: user_actual.consultarPromocion(p)
                    elif sub == "4":
                        for r in user_actual.historialReservas: print(r.generarTicket())
                    elif sub == "5":
                        print("\n--- Actualizar Datos --- (Deja en blanco para no cambiar)")
                        n = input("Nuevo Nombre: ")
                        e = input("Nuevo Email: ")
                        t = input("Nuevo Teléfono: ")
                        user_actual.actualizarDatos(n or None, e or None, t or None)
                    elif sub == "6":
                        print("\n--- Cancelación de Reservas ---")
                        confirmadas = [r for r in user_actual.historialReservas if r.estado == "Confirmada"]
                        if not confirmadas:
                            print("No tienes las reservas activas para cancelar.")
                        else:
                            for r in confirmadas:
                                print(f"ID: {r.idReserva} | Película: {r.funcion.pelicula.titulo} | Monto: ${r.montoTotal}")
                            id_cancelar = input("\nIngresa el ID de la reserva que deseas cancelar: ")
                            reserva_a_borrar = next((r for r in confirmadas if r.idReserva == id_cancelar), None)
                            if reserva_a_borrar:
                                user_actual.cancelarReserva(reserva_a_borrar)
                            else:
                                print("ID no válido o la reserva no se puede cancelar.")
                    elif sub == "7":
                        user_actual.logout()
                        break
                    input("ENTER...")

#No me repruebe profe porfa
ejecutar_sistema()