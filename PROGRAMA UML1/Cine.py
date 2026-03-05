# Modulo de Personas
class Persona():
    listas_personas = []

    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.esta_logeado = False
    
    @classmethod
    def inicio_sesion(cls, id_p, nombre, email, telefono):
        nueva_persona = cls(id_p, nombre, email, telefono)
        cls.listas_personas.append(nueva_persona)
        return nueva_persona

    def login(self, id_intento, email_intento):
        if str(self.id_persona) == str(id_intento) and self.email == email_intento:
            self.esta_logeado = True
            print(f"Hola {self.nombre}, entraste correctamente al sistema del CINERICHIXCAPI.")
            return True
        print("Los datos no coinciden. Revisa el ID o el correo e intenta de nuevo porfa.")
        return False

    def logout(self):
        self.esta_logeado = False
        print(f"La sesion ha sido terminada {self.nombre}. Nos vemos CAPI.")

    def actualizarDatos(self, nuevo_nombre=None, nuevo_email=None, nuevo_tel=None):
        if nuevo_nombre: self.nombre = nuevo_nombre
        if nuevo_email: self.email = nuevo_email
        if nuevo_tel: self.telefono = nuevo_tel
        print(f"Listo, los datos de {self.nombre} se actualizaron en el sistema de CINERICHIXCAPI.")

class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono, puntosFidelidad, historialReservas):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = historialReservas
    
    def mostrar_detalle(self):
        return f"ID: {self.id_persona} | Usuario: {self.nombre} | Correo: {self.email} | Telefono:{self.telefono}| Puntos: {self.puntosFidelidad} | historialReservas:{self.historialReservas}"

    @classmethod
    def registrar_usuario(cls, id_p, nombre, email, telefono, puntosFidelidad=0, historialReservas=None):
        if historialReservas is None: historialReservas = []
        nuevo_usuario = cls(id_p, nombre, email, telefono, puntosFidelidad, historialReservas)
        cls.listas_personas.append(nuevo_usuario)
        return nuevo_usuario

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)
        print(f"La reserva {reserva.idReserva} ya aparece en el historial de {self.nombre}.")

    def consultarPromocion(self, promocion):
        if promocion.esValida(self):
            print(f"Puedes usar la promo '{promocion.descripcion}', es válida para ti.")
        else:
            print(f"Por ahora no puedes usar la promoción '{promocion.descripcion}'.")
    
    def cancelarReserva(self, reserva):
        if reserva not in self.historialReservas:
            print("Esa reserva no parece ser tuya, no puedes cancelarla.")
            return

        if reserva.estado == "Confirmada":
            reserva.estado = "Cancelada"
            reserva.funcion.asientosLibres += reserva.asientos
            
            puntos_menos = int(reserva.montoTotal / 10)
            self.puntosFidelidad = max(0, self.puntosFidelidad - puntos_menos)
            
            print(f"\nReserva {reserva.idReserva} cancelada.")
            print(f"Liberamos {reserva.asientos} asientos de '{reserva.funcion.pelicula.titulo}'.")
            print(f"Se te descontaron {puntos_menos} puntos de tu cuenta.")
        else:
            print(f"No se pudo cancelar. La reserva {reserva.idReserva} figura como: {reserva.estado}.")

class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(id_persona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario
        
    def mostrar_detalle(self):
        return f"ID: {self.idEmpleado} | Empleado: {self.nombre} | Correo: {self.email} | Telefono:{self.telefono} | IDempleado:{self.idEmpleado} Puesto: {self.rol} | Turno: {self.horario}"
    
    @classmethod
    def registrar_empleado(cls, id_p, nombre, email, telefono, idEmpleado, rol, horario):
        nuevo_empleado = cls(id_p, nombre, email, telefono, idEmpleado, rol, horario)
        cls.listas_personas.append(nuevo_empleado)
        return nuevo_empleado

    def marcarEntrada(self):
        print(f"{self.nombre} ({self.rol}) registró su entrada al turno.")

    def gestionarFunciones(self, funcion, accion):
        if self.rol == "Admin":
            print(f"El administrador {self.nombre} está aplicando '{accion}' en la función {funcion.idFuncion}.")
        else:
            print("No tienes permiso de administrador para hacer cambios aquí.")

# Modulo de infraestructura
class Espacio():
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.esta_disponible = True
        self.esta_limpio = True

    def limpiarEspacio(self):
        if self.esta_limpio:
            print(f"La zona {self.nombre} ya estaba limpia.")
        else:
            self.esta_limpio = True
            print(f"Se terminó de limpiar {self.nombre}.")

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidad, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo 
        self.capacidad = capacidad
        self.aforo_actual = capacidad
        self.esVip = esVip

    def mostrar_detalle(self):
        tipo_sala = "VIP" if self.esVip else "Normal"
        return f"ID de la sala:{self.idEspacio} | Sala: {self.nombre} | Ubicación: {self.ubicacion} | {self.tipo} | Cupo: {self.capacidad} | {tipo_sala} "
    
    def ajustarAforo(self, nuevo_aforo):
        if 0 <= nuevo_aforo <= self.capacidad:
            self.aforo_actual = nuevo_aforo
            print(f"Cambiamos el aforo de la sala {self.nombre} a {nuevo_aforo}.")
        else:
            print("Esa cantidad no es válida para esta sala.")

    def obtenerTipoSala(self):
        categoria = "VIP" if self.esVip else "Estándar"
        return f"Sala {self.tipo} ({categoria}) - Capacidad: {self.capacidad}"

class Zona_Comida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, listaProductos, stockActual):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = listaProductos 
        self.stockActual = stockActual 

    def venderProducto(self, nombre_producto):
        if nombre_producto in self.stockActual and self.stockActual[nombre_producto] > 0:
            self.stockActual[nombre_producto] -= 1
            print(f"Se vendió {nombre_producto}. Quedan {self.stockActual[nombre_producto]} en stock.")
            return True
        else:
            print(f"No hay {nombre_producto} o se nos terminó el stock.")
            return False

    def actualizarInventario(self, nombre_producto, cantidad):
        if nombre_producto in self.stockActual:
            self.stockActual[nombre_producto] += cantidad
        else:
            self.stockActual[nombre_producto] = cantidad
            self.listaProductos.append(nombre_producto)
        print(f"Inventario de {nombre_producto} actualizado. Nuevo total: {self.stockActual[nombre_producto]}.")

# Modulo Logica de funciones y peliculas
class Pelicula():
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion 
        self.clasificacion = clasificacion 
        self.genero = genero
    
    def mostrar_detalle(self):
        return f"Pelicula: {self.titulo} | Duración: {self.duracion} min | Clasificación: {self.clasificacion} | Genero: {self.genero}"
    
    def obtenerSinopsis(self):
        return f"{self.titulo} ({self.genero}), dura {self.duracion} minutos."

    def esAptaParaTodoPublico(self):
        return self.clasificacion == "A"

class Funcion():
    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula 
        self.sala = sala 
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.asientosLibres = sala.capacidad 

    def mostrar_detalle(self):
        return f"ID: {self.idFuncion} | Película: {self.pelicula.titulo} | Sala: {self.sala.nombre} | Hora: {self.horarioInicio} | Precio Base: {self.precioBase}"
    
    def calcularAsientosLibres(self):
        return self.asientosLibres

    def obtenerDetallesFuncion(self):
        return f"La función {self.idFuncion} ({self.pelicula.titulo}) es en la {self.sala.nombre} a las {self.horarioInicio}. Quedan {self.asientosLibres} asientos."
    
    def venderAsientos(self, cantidad):
        if cantidad <= self.asientosLibres:
            self.asientosLibres -= cantidad
            print(f"Venta de {cantidad} asientos para '{self.pelicula.titulo}' completada.")
            return True
        else:
            print(f"No tenemos suficientes lugares. Solo quedan {self.asientosLibres}.")
            return False

# Modulo Gestion Comercial
class Promocion():
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento 
        self.fechaExpiracion = fechaExpiracion
    
    def mostrar_detalle(self):
        return f"Código: {self.codigo} | {self.descripcion} | Descuento: {self.porcentajeDescuento*100}% | Fecha de Expiración: {self.fechaExpiracion}"
    
    def esValida(self, usuario): 
        from datetime import datetime
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        return self.fechaExpiracion >= fecha_hoy

    def aplicarDescuento(self, monto):
        ahorro = monto * self.porcentajeDescuento
        total = monto - ahorro
        print(f"Promo '{self.descripcion}' aplicada. Te ahorraste ${ahorro:.2f}. Total a pagar: ${total:.2f}")
        return total

class Reserva():
    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario 
        self.funcion = funcion 
        self.asientos = asientos 
        self.montoTotal = funcion.precioBase * asientos
        self.estado = "Pendiente" 
    
    def confirmarPago(self):
        if self.funcion.venderAsientos(self.asientos):
            self.estado = "Confirmada"
            puntos_ganados = int(self.montoTotal / 10)
            self.usuario.puntosFidelidad += puntos_ganados
            print(f"Pago de la reserva {self.idReserva} confirmado. Sumaste {puntos_ganados} puntos.")
            return True
        else:
            print(f"No se pudo pagar la reserva {self.idReserva}. No hay lugares disponibles.")
            return False

    def generarTicket(self):
        if self.estado == "Confirmada":
            ticket = (
                f"\n--- Ticket de Compra ---\n"
                f"ID Reserva: {self.idReserva}\n"
                f"Nombre: {self.usuario.nombre}\n"
                f"Pelicula: {self.funcion.pelicula.titulo}\n"
                f"Sala: {self.funcion.sala.nombre}\n"
                f"Asientos: {self.asientos}\n"
                f"Total: ${self.montoTotal:.2f}\n"
                f"------------------------\n"
            )
            return ticket
        else:
            return "No hay ticket, la reserva todavía no está confirmada."

    def aplicarPromocion(self, promo):
        if self.estado == "Pendiente" and promo.esValida(self.usuario):
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)
            print("Se aplicó la promoción a tu cuenta.")
        else:
            print("No se pudo aplicar el descuento en esta ocasión.")