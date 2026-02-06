class Articulo():
    def __init__(self, nombre, precio_base, stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock
    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.precio_base *= (1 - porcentaje/100)
            print(f"El nuevo precio es: {self.precio_base}")
        
        else:
            print("El valor del porcentaje de descuento no es valido")
    
    def actualizar_stock(self, cantidad):
        if (self.stock+cantidad)<0:
            print("No hay suficiente stock")
        else:
            self.stock += cantidad
            print(f"La nueva cantidad de {self.nombre}, su stock es:{self.stock}")

class Categoria():
    def __init__(self, nombre_categoria):
        self.nombre=nombre_categoria
        self.lista_producto = []
    
    def agregar_producto(self,producto):
        self.lista_producto.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista.")

    def valor_total_categoria(self):
        suma=0
        for a in self.lista_producto:
            suma+=a.precio_base*a.stock
        print(f"El precio total de la categoria {self.nombre} es: {suma} pesos")

class Pedido():
    def __init__(self, cliente, productos_comprados):
        pass