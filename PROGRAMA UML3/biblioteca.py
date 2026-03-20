#Modulo de materiales
class Material():
    def __init__(self, idMaterial, titulo, añoPublicacion,disponible=True):
        self.idMaterial=idMaterial
        self.titulo=titulo
        self.añoPublicacion=añoPublicacion
        self.disponible=disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor=autor
        self.isbn=isbn
        self.genero=genero
    
    def mostrarObjeto(self):
        return f"|ID:{self.idMaterial}| |Titulo:{self.titulo}| |Año Publi:{self.añoPublicacion}| |Disponible:{self.disponible}| |Autor: {self.autor}| |isbn:{self.isbn}| |Genero:{self.genero}|"

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion=edicion
        self.periodicidad=periodicidad

    def mostrarObjeto(self):
        return f"|ID:{self.idMaterial}| |Titulo:{self.titulo}| |Año Publi:{self.añoPublicacion}| |Disponible:{self.disponible}| |Edicion: {self.edicion}| |Periodicidad:{self.periodicidad}|"

class Materialdigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo=tipoArchivo
        self.urlDescarga=urlDescarga
        self.tamañoMB=tamañoMB
    
    def mostrarObjeto(self):
        return f"|ID:{self.idMaterial}| |Titulo:{self.titulo}| |Año Publi:{self.añoPublicacion}| |Disponible:{self.disponible}| |Tipo Archivo: {self.tipoArchivo}| |URL:{self.urlDescarga}| |Tamaño en MB:{self.tamañoMB}|"

#Modulo usuario y sedes

class Persona():#Le agregue cosas porque en el archivo no tiene atributos y metodos
    def __init__(self, idpersona, nombre):
        self.idpersona=idpersona
        self.nombre=nombre

class Usuario(Persona):
    def __init__(self, idpersona, nombre, limitePrestamos):
        super().__init__(idpersona, nombre)
        self.limitePrestamos=limitePrestamos
        self.listaActiva=[]
    
    def mostrarObjeto(self):
        return f"|ID:{self.idpersona}| |Nombre:{self.nombre}| |Limite de Prestamos:{self.limitePrestamos}|"

class Bibliotecario(Persona):
    def __init__(self, idpersona, nombre):
        super().__init__(idpersona, nombre)

    def mostrarObjeto(self):
        return f"|ID:{self.idpersona}| |Nombre:{self.nombre}|"

    def gestionarPrestamo(self, usuario, item, inicio, fin):
        if not item.disponible:
            print(f"Lo siento, el material '{item.titulo}' no está disponible")
            return None
        
        conteo_prestamos = 0
        for p in usuario.listaActiva:
            conteo_prestamos += 1
        if conteo_prestamos >= usuario.limitePrestamos:
            print(f"El usuario {usuario.nombre} ya tiene el límite de libros")
            return None
        folio = conteo_prestamos + 1
        
        ticket = Prestamo(folio, inicio, fin, usuario, item)
        item.disponible = False
        usuario.listaActiva.append(ticket)
        print(f"Listo '{item.titulo}' prestado a {usuario.nombre}. Folio: {folio}")
        return ticket
    
    def transferirMaterial(self, recurso, origen, destino):#SucursalDestino: Sucursal
        if recurso in origen.catalogoLocal:
            origen.catalogoLocal.remove(recurso)
            destino.catalogoLocal.append(recurso)
            print(f"Movimiento realizado: {recurso.titulo} enviado de {origen.nombre} a {destino.nombre}")
        else:
            print(f"Error: El recurso '{recurso.titulo}' no está registrado en la sede {origen.nombre}")

class Sucursal():
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []
    
    def mostrarObjeto(self):
        return f"|ID:{self.idSucursal}| |Nombre:{self.nombre}|"

#Modulo de gestion prestamo y penalizacion

class Prestamo():
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo=idPrestamo
        self.fechaInicio=fechaInicio
        self.fechaDevolucion=fechaDevolucion
        self.usuario=usuario
        self.material=material

class Penalizacion():
    def __init__(self, monto, motivo, pagada=False):
        self.monto=monto
        self.motivo=motivo
        self.pagada=pagada
    
    def calcularMulta(self, dias_atraso):
        self.monto = dias_atraso * 15
        return self.monto

    def bloquearUsuario(self, usuario):
        if not self.pagada:
            usuario.limitePrestamos = 0
            print(f"Alerta: El usuario {usuario.nombre} ha sido bloqueado por adeudos")

class Catalogo():
    def __init__(self):
        self.listaMaterialesGlobal = []

    def BuscarporAutor(self, autor):
        encontrados = []
        for m in self.listaMaterialesGlobal:
            if isinstance(m, Libro):
                if m.autor.lower() == autor.lower():
                    encontrados.append(m)
        return encontrados
    
    def BuscarPorTodasSucursales(self, nombre_item, sedes):
        resultados = []
        for s in sedes:
            for mat in s.catalogoLocal:
                if nombre_item.lower() in mat.titulo.lower():
                    resultados.append(f"{mat.titulo} (Sede: {s.nombre})")
        return resultados
