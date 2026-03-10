class Persona():
    def __init__(self, idpersona, nombre, email):
        self.idpersona=idpersona
        self.nombre=nombre
        self.email=email
         
    def login(self, id_ingresado, email_ingresado):

        if id_ingresado == self.idpersona and email_ingresado == self.email:
            print(f"Login exitoso. Bienvenido, {self.nombre} a la cafeteria Richi.")
            return True
        else:
            print(f"Error de datos. Los datos no han coincidido para {self.nombre}.")
            return False

    def actualizarPerfil(self, nuevo_nombre=None, nuevo_email=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_email:
            self.email = nuevo_email
        print(f"Datos actualizados: {self.nombre} ({self.email})")

class Cliente(Persona):
    def __init__(self, idpersona, nombre, email, puntosFidelidad, historialPedidos):
        super().__init__(idpersona, nombre, email)
        self.puntosFidelidad=puntosFidelidad
        self.historialPedidos=historialPedidos
    
    def mostrar_objetos(self):
        return f"ID: {self.idpersona} | Usuario: {self.nombre} | Correo: {self.email} | Puntos de Fidelidad:{self.puntosFidelidad}| Historial: {self.historialPedidos} |"
      
    def realizarPedido(self, objeto_pedido):
        self.historialPedidos.append(objeto_pedido)
        puntos_ganados = int(objeto_pedido.total / 10)
        self.puntosFidelidad += puntos_ganados
        print(f"Pedido registrado para {self.nombre}. Ganaste {puntos_ganados} puntos.")

    def consultarHistorial(self):
        if not self.historialPedidos:
         print("Aún no tienes pedidos registrados.")
        else:
            for pedido in self.historialPedidos:
                print(f"Pedido ID: {pedido.idPedido} - Total: ${pedido.calcularTotal()}")

    def canjearPuntos(self, costo_puntos):
        if self.puntosFidelidad >= costo_puntos:
            self.puntosFidelidad -= costo_puntos
            print(f"Canje realizado. Puntos restantes: {self.puntosFidelidad}")
            return True
        else:
            print(f"Puntos insuficientes. Te faltan {costo_puntos - self.puntosFidelidad} puntos.")
            return False

class Empleado(Persona):
    def __init__(self, idpersona, nombre, email, idEmpleado, rol):
        super().__init__(idpersona, nombre, email)
        self.idEmpleado= idEmpleado
        self.rol= rol
    
    def mostrar_objetos(self):
        return f"ID: {self.idpersona} | Empleado: {self.nombre} | Correo: {self.email} | idEmpleado:{self.idEmpleado}| Rol: {self.rol} |"

    def actualizarInventario(self, inventario_obj, ingrediente, accion="agregar"):
        if accion == "agregar":
            inventario_obj.ingredientes.append(ingrediente)
            print(f"{self.nombre} agregó {ingrediente} al inventario.")
        elif accion == "quitar":
            if ingrediente in inventario_obj.ingredientes:
                inventario_obj.ingredientes.remove(ingrediente)
                print(f"{self.nombre} retiró {ingrediente} del inventario.")
            else:
                print(f"El ingrediente {ingrediente} no existe en el inventario.")

    def cambiarEstadoPedido(self, pedido_obj, nuevo_estado):
        estado_anterior = pedido_obj.estado
        pedido_obj.estado = nuevo_estado
        print(f"Pedido {pedido_obj.idPedido}: {estado_anterior} -> {nuevo_estado} (Actualizado por {self.nombre})")

class ProductoBase():
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura, modificadores):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=modificadores
    
    def mostrar_objetos(self):
        return f"ID: {self.idProducto} | Bebida: {self.nombre} | Precio base: {self.precioBase} | Tamaño:{self.tamaño}| Temperatura:{self.temperatura} | Modificadores: {self.modificadores} |"
    
    def agregarExtra(self, nuevo_extra):
        self.modificadores.append(nuevo_extra)
        print(f"-> Se agregó '{nuevo_extra}' a tu {self.nombre}.")

    def calcularPrecioFinal(self):
        # Cada modificador en la lista cuesta $10
        total_extras = len(self.modificadores) * 10
        return self.precioBase + total_extras

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten
    
    def mostrar_objetos(self):
        return f"ID: {self.idProducto} | Postre: {self.nombre} | Precio base: {self.precioBase} | Es vegano:{self.esVegano}| Sin gluten:{self.sinGluten} |"

class Pedio():
    def __init__(self, idPedido, productos, estado="Pendiente"):
        self.idPedido = idPedido
        self.productos = productos  
        self.estado = estado       
        self.total = 0             
        self.calcularTotal()    

    def calcularTotal(self):
        self.total = 0
        for p in self.productos:
            if hasattr(p, 'calcularPrecioFinal'):
                self.total += p.calcularPrecioFinal()
            else:
                self.total += p.precioBase
        return self.total

    def validarStock(self, inventario_obj):
        if len(inventario_obj.ingredientes) > 0:
            print(f"Stock verificado para el pedido {self.idPedido}. Hay ingredientes suficientes.")
            return True
        else:
            print(f"Error: No hay stock suficiente para procesar el pedido {self.idPedido}.")
            return False

    def mostrar_objetos(self):
        nombres = [p.nombre for p in self.productos]
        return (f"ORDEN #{self.idPedido} | Estado: {self.estado} | "
                f"Items: {', '.join(nombres)} | Total: ${self.total}")

class Inventario():
    def __init__(self, ingredientes):
        self.ingredientes=ingredientes
    
    def mostrar_objetos(self):
        return f"| Ingredientes: {self.ingredientes}|"

    def reducirStock(self, ingrediente_usado):
        if ingrediente_usado in self.ingredientes:
            self.ingredientes.remove(ingrediente_usado)
            print(f"Stock: Se ha utilizado '{ingrediente_usado}'.")
            return True
        else:
            print(f"Advertencia: No hay '{ingrediente_usado}' en el inventario.")
            return False

    def notificarFaltante(self):
        cantidad = len(self.ingredientes)
        if cantidad == 0:
            return "¡ALERTA CRÍTICA! Inventario totalmente vacío."
        elif cantidad < 3:
            return f"Alerta: Stock bajo. Solo quedan {cantidad} ingredientes."
        else:
            return "Inventario con niveles suficientes."
