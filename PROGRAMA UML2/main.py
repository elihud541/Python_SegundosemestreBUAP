from cafeteria import *

def ejecutacion_sistema():
    
    c1 = Cliente(1, "Ana García", "2", 150, [])
    c2 = Cliente(2, "Luis Rodríguez", "luis.rod@email.com", 45, [])
    c3 = Cliente(3, "Carla Méndez", "carla.m@email.com", 890, [])
    c4 = Cliente(4, "Diego Torres", "diego.t@email.com", 0, [])
    c5 = Cliente(5, "Elena Santis", "elena.s@email.com", 320, [])
    c6 = Cliente(6, "Fernando Ruiz", "fer.ruiz@email.com", 0, [])
    c7 = Cliente(7, "Gabriela Paz", "gaby.paz@email.com", 1200, [])
    c8 = Cliente(8, "Hugo Villalobos", "hugo.v@email.com", 75, [])
    c9 = Cliente(9, "Isabel Castro", "isa.castro@email.com", 540, [])
    c10 = Cliente(10, "Javier Soto", "javi.soto@email.com", 210, [])
    lista_clientes=[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

    e1 = Empleado(11, "Carlos Ruiz", "1", "EMP001", "Gerente")
    e2 = Empleado(12, "Marta López", "m.lopez@cafe.com", "EMP002", "Barista")
    e3 = Empleado(13, "Juan Pérez", "j.perez@cafe.com", "EMP003", "Mesero")
    e4 = Empleado(14, "Sofía Castro", "s.castro@cafe.com", "EMP004", "Barista")
    e5 = Empleado(15, "Roberto Díaz", "r.diaz@cafe.com", "EMP005", "Mesero")
    e6 = Empleado(16, "Lucía Méndez", "l.mendez@cafe.com", "EMP006", "Mesero")
    e7 = Empleado(17, "Andrés Morales", "a.morales@cafe.com", "EMP007", "Barista")
    e8 = Empleado(18, "Beatriz Soler", "b.soler@cafe.com", "EMP008", "Mesero")
    e9 = Empleado(19, "Tomás Vega", "t.vega@cafe.com", "EMP009", "Barista")
    e10 = Empleado(20, "Laura Rivas", "l.rivas@cafe.com", "EMP010", "Gerente")
    lista_empleados= [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

    b1 = Bebida(101, "Americano", 33.50, "Grande", "Caliente", ["Sin azúcar"])
    b2 = Bebida(102, "Iced Latte", 24.50, "Mediano", "Fría", ["Leche de almendras", "Vainilla"])
    b3 = Bebida(103, "Cappuccino", 34.00, "Pequeño", "Caliente", ["Canela extra"])
    b4 = Bebida(104, "Frappé de Chocolate", 25.50, "Grande", "Fría", ["Crema batida", "Chispas"])
    b5 = Bebida(105, "Té Verde", 23.00, "Mediano", "Caliente", ["Miel"])
    b6 = Bebida(106, "Cold Brew", 14.80, "Grande", "Fría", ["Hielo extra"])
    b7 = Bebida(107, "Espresso", 32.50, "Pequeño", "Caliente", [])
    b8 = Bebida(108, "Mocha Blanco", 25.00, "Mediano", "Caliente", ["Leche deslactosada"])
    b9 = Bebida(109, "Limonada con Menta", 33.80, "Grande", "Fría", ["Stevia"])
    b10 = Bebida(110, "Flat White", 24.20, "Pequeño", "Caliente", ["Shot extra"])

    p1 = Postre(201, "Brownie de Chocolate", 43.50, False, False)
    p2 = Postre(202, "Galleta de Avena", 32.00, True, True)
    p3 = Postre(203, "Cheesecake de Frutos Rojos", 4.50, False, False)
    p4 = Postre(204, "Muffin de Arándanos", 42.80, False, True)
    p5 = Postre(205, "Tarta de Manzana Vegana", 33.20, True, False)
    p6 = Postre(206, "Alfajor de Maicena", 21.50, False, True)
    p7 = Postre(207, "Mousse de Maracuyá", 33.00, False, True)
    p8 = Postre(208, "Budín de Limón y Chía", 24.50, True, False)
    p9 = Postre(209, "Trufas de Dátil y Coco", 41.80, True, True)
    p10 = Postre(210, "Croissant Clásico", 22.20, False, False)

    catalogo_bebidas = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
    catalogo_postres = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

    inv1 = Inventario(["Café en grano", "Leche entera", "Azúcar", "Harina", "Huevos"])
    inv2 = Inventario(["Té verde", "Leche de almendras", "Stevia", "Manzanas", "Canela"])
    inv3 = Inventario(["Cacao en polvo", "Mantequilla", "Levadura", "Sal", "Chocolate amargo"])
    inv4 = Inventario(["Granos Espresso", "Leche deslactosada", "Miel", "Arándanos", "Vainilla"])
    inv5 = Inventario(["Dátiles", "Coco rallado", "Nueces", "Maicena", "Dulce de leche"])
    inv6 = Inventario(["Café Descafeinado", "Crema", "Caramelo", "Frutos rojos", "Queso crema"])
    inv7 = Inventario(["Té Negro", "Chai Mix", "Leche de soya", "Limones", "Semillas de chía"])
    inv8 = Inventario(["Jarabe de Chocolate", "Menta fresca", "Hielo", "Harina de arroz", "Banana"])
    inv9 = Inventario(["Café de especialidad", "Agua purificada", "Avena sin gluten", "Pulpa de maracuyá"])
    inv10 = Inventario(["Polvo de Matcha", "Leche de coco", "Panela", "Claras de huevo", "Aceite de coco"])
    inv_general=[inv1,inv2,inv3,inv4,inv5,inv6,inv7,inv8,inv9,inv10]



    print("---------------- Imprimir los objetos del programa (Evidencia de Instanciación). -----------------")

    print("Clientes:")
    for c in c1, c2, c3, c4, c5, c6, c7, c8, c9, c10:
        print(c.mostrar_objetos()) 
    
    print("\nEmpleados:")
    for c in e1, e2, e3, e4, e5, e6, e7, e8, e9, e10:
        print(c.mostrar_objetos()) 

    print("\nBebidas:")
    for c in b1, b2, b3, b4, b5, b6, b7, b8, b9, b10:
        print(c.mostrar_objetos()) 

    print("\nPostres:")
    for c in p1, p2, p3, p4, p5, p6, p7, p8, p9, p10:
        print(c.mostrar_objetos()) 

    print("\nInventario:")
    for c in inv1, inv2, inv3, inv4, inv5, inv6, inv7, inv8, inv9, inv10:
        print(c.mostrar_objetos()) 

    while True:
        print("\n------------------------------------------")
        print("      BIENVENIDOS A CAFÉ RICHI")
        print("------------------------------------------")
        print("1. Login al sistema")
        print("2. Cerrar Sistema")
        op = input("\nElige una opción: ")

        if op == "1":
            try:
                id_ing = int(input("ID: "))
                email_ing = input("Correo: ")
            except ValueError:
                print("Error: El ID debe ser un número.")
                continue

            usuario_activo = None
            for p in lista_clientes + lista_empleados:
                if p.idpersona == id_ing and p.email == email_ing:
                    if p.login(id_ing, email_ing):
                        usuario_activo = p
                        break
            if usuario_activo:
                if isinstance(usuario_activo, Cliente):
                    while True:
                        print(f"\n--- PANEL DE CLIENTE ---: {usuario_activo.nombre}")
                        print(f"Puntos acumulados: {usuario_activo.puntosFidelidad}")
                        print("-" * 30)
                        print("1. Realizar Pedido")
                        print("2. Consultar Historial")
                        print("3. Canjear Puntos")
                        print("4. Actualizar Perfil")
                        print("5. Cerrar Sesión")
                        op_c = input("Selecciona: ")

                        if op_c == "1":
                            print("\n-- Bebidas --")
                            for i, b in enumerate(catalogo_bebidas): 
                                print(f"{i+1}. {b.nombre} (${b.precioBase})")
                            
                            idx_b = int(input("Bebida #: ")) - 1
                            bebida_seleccionada = catalogo_bebidas[idx_b]
                            
                            extras_disponibles = bebida_seleccionada.modificadores
                            bebida_seleccionada.modificadores = [] 
                            if extras_disponibles:
                                print(f"\nEsta bebida tiene estos extras disponibles ($10 c/u):")
                                for i, ext in enumerate(extras_disponibles):
                                    print(f"{i+1}. {ext}")                               
                                si_extra = input("\n¿Deseas agregar algún extra? (s/n): ").lower()
                                if si_extra == "s":
                                    cual = int(input("¿Cuál número de extra deseas?: ")) - 1
                                    if 0 <= cual < len(extras_disponibles):
                                        bebida_seleccionada.agregarExtra(extras_disponibles[cual])
                            else:
                                print("\n(Esta bebida no tiene extras configurados)")
                            print("\n-- Postres --")
                            for i, p in enumerate(catalogo_postres):
                                etiquetas = []
                                if p.esVegano: etiquetas.append("Vegano")
                                if p.sinGluten: etiquetas.append("Sin Gluten")
                                info = f"({', '.join(etiquetas)})" if etiquetas else ""
                                print(f"{i+1}. {p.nombre} (${p.precioBase}) {info}")
                            
                            idx_p = int(input("Postre #: ")) - 1
                            postre_seleccionado = catalogo_postres[idx_p]
                            precio_b_final = bebida_seleccionada.calcularPrecioFinal()
                            total_pedido = precio_b_final + postre_seleccionado.precioBase

                            print("\n------------------------------------------------" )
                            print(f"TICKET DE VENTA")
                            print("------------------------------------------------")
                            print(f"{bebida_seleccionada.nombre:15} ${bebida_seleccionada.precioBase:>6.2f}")
                            for m in bebida_seleccionada.modificadores:
                                print(f" + {m:13} $ 10.00")
                            print(f"{postre_seleccionado.nombre:15} ${postre_seleccionado.precioBase:>6.2f}")
                            print("------------------------------------------------")
                            print(f"TOTAL FINAL:${total_pedido:>6.2f}")
                            print("------------------------------------------------")

                            import random
                            pedido = Pedio(random.randint(1000, 9999), [bebida_seleccionada, postre_seleccionado])
                            pedido.total = total_pedido
                            
                            if pedido.validarStock(inv_general[0]):
                                usuario_activo.realizarPedido(pedido)

                        elif op_c == "2":
                            print(f"\n--- Historial de {usuario_activo.nombre} ---")
                            usuario_activo.consultarHistorial()
                        
                        elif op_c == "3":
                            print(f"Tienes {usuario_activo.puntosFidelidad} puntos.")
                            try:
                                costo = int(input("¿Cuántos puntos deseas canjear?: "))
                                usuario_activo.canjearPuntos(costo)
                            except ValueError:
                                print("Error: Ingresa una cantidad válida.")

                        elif op_c == "4":
                            nuevo_n = input("Nuevo nombre (Enter para omitir): ")
                            nuevo_e = input("Nuevo email (Enter para omitir): ")
                            usuario_activo.actualizarPerfil(nuevo_n if nuevo_n else None, nuevo_e if nuevo_e else None)
                        elif op_c == "5":
                            break
        if usuario_activo:
            if isinstance(usuario_activo, Empleado):
                while True:
                        print("\n----------------------------------------------------------")
                        print(f"--- PANEL DE EMPLEADO --- {usuario_activo.nombre}")
                        print(f"Rol: {usuario_activo.rol} | ID: {usuario_activo.idEmpleado}")
                        print("----------------------------------------------------------")
                        print("1. Ver Inventario Completo")
                        print("2. Gestionar Stock (Agregar/Quitar)")
                        print("3. Notificar Faltantes")
                        print("4. Cambiar Estado de Pedido")
                        print("5. Actualizar mi Perfil")
                        print("6. Cerrar Sesión")
                        op_e = input("\nSelecciona una opción: ")

                        if op_e == "1":
                            print("\n--- Estado Actual del Inventario ---")
                            print(inv_general[0].mostrar_objetos())
                        
                        elif op_e == "2":
                            ing = input("Nombre del ingrediente: ")
                            acc = input("¿Acción (agregar/quitar)?: ").lower()
                            usuario_activo.actualizarInventario(inv_general[0], ing, acc)
                        
                        elif op_e == "3":
                            print(f"\nReporte: {inv_general[0].notificarFaltante()}")

                        elif op_e == "4":
                            id_p = input("ID del pedido a actualizar: ")
                            nuevo_est = input("Nuevo estado (Preparando/Entregado/Cancelado): ")
                            pedido_temp = Pedio(id_p, []) 
                            usuario_activo.cambiarEstadoPedido(pedido_temp, nuevo_est)
                        
                        elif op_e == "5":
                            print("\n--- Actualización de Datos Personales ---")
                            nuevo_n = input("Nuevo nombre (Enter para omitir): ")
                            nuevo_e = input("Nuevo correo (Enter para omitir): ")
                            usuario_activo.actualizarPerfil(nuevo_n if nuevo_n else None, nuevo_e if nuevo_e else None)
                        
                        elif op_e == "6":
                            print(f"Cerrando sesión de {usuario_activo.nombre}...")
                            break
        elif op == "2":
            print("Saliendo de Café Richi. ¡Buen día!")
            break
ejecutacion_sistema()