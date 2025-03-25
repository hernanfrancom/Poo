class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad

    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre} vendidas.")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Reabastecimiento realizado: {cantidad} unidades de {self.nombre} añadidas al stock.")


producto = Producto("Laptop", 1200, 10)

print("Verificar disponibilidad de 5 unidades:", producto.verificar_disponibilidad(5))
producto.vender(3)
print("Verificar disponibilidad de 8 unidades:", producto.verificar_disponibilidad(8))
producto.vender(8) 
producto.reabastecer(10)
print("Verificar disponibilidad de 8 unidades:", producto.verificar_disponibilidad(8))
producto.vender(8)