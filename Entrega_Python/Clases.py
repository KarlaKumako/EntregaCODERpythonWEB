
"""
Iniciamos la creación de la clase cliente integrando atributos tales como:
Nombre
Apellido
Edad
Email
"""

class Cliente:
    def __init__(self, nombre, apellido, edad, email):  # Define el método de inicialización para la clase Cliente
        self.nombre = nombre  # Asigna el nombre del cliente
        self.apellido = apellido  # Asigna el apellido del cliente
        self.edad = edad  # Asigna la edad del cliente
        self.email = email  # Asigna el correo electrónico del cliente
    """
    Pasamos el uso del metodo __str__ 
    El método __str__ está definido en la clase Cliente. Su propósito es devolver una cadena que represente el nombre completo del cliente. La línea return f"{self.nombre} {self.apellido}" significa que el método devolverá una cadena que contiene el nombre y el apellido del cliente, separados por un espacio.
    """
    def __str__(self):# Define el método especial __str__ para la representación de cadenas de la clase Cliente
        return f"{self.nombre} {self.apellido}"# Devuelve el nombre completo del cliente

    def enviar_correo_promocional(self, promocion):  # Define un método para enviar un correo promocional al cliente
        print(f"Correo promocional enviado a {self.email}: {promocion}")  # Imprime un mensaje simulando el envío de correo promocional

    def hacer_compra(self, producto, cantidad):  # Define un método para que el cliente realice una compra
        if cantidad <= 0:  # Si la cantidad es menor o igual a cero
            print("La cantidad debe ser mayor que cero.")  # Imprime un mensaje de error
            return None # Sale del método
        total = producto.precio * cantidad  # Calcula el total de la compra
        if total <= 0:  # Si el total es menor o igual a cero
            print("El total a pagar debe ser mayor que cero.")  # Imprime un mensaje de error
        return total # Sale del método
     

class ClienteVIP(Cliente):  # Subclase que extiende Cliente
    def __init__(self, nombre, apellido, edad, email, nivel):
        super().__init__(nombre, apellido, edad, email)
        self.nivel = nivel

    def aplicar_descuento(self, total):
        if total > 500:
            return total * 0.85  # Descuento del 15%
        return total

    def hacer_compra(self, producto, cantidad):
        total = super().hacer_compra(producto, cantidad)
        total_con_descuento = self.aplicar_descuento(total)
        print(f"Total con descuento VIP: {total_con_descuento}")
        return total_con_descuento
    
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Ropa(Producto):  # Subclase que extiende Producto
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla
        self.descuento_fijo = 0.05  # Descuento fijo del 5%

    def calcular_precio_descuento(self):
        return self.precio - (self.precio * self.descuento_fijo)


