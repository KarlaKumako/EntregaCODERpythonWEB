from Clases import *
#from PaqueteFunciones import *

"""
Realizamos un ejemplo con las clases creadas, las funciones y sus atributos. 
"""
if __name__ == "__main__":
    cliente_comun = Cliente("Homero", "Simpson", 30, "donbarredora@springfieldtown.com")
    cliente_vip = ClienteVIP("Cosme", "Fulanito", 28, "quelegancialadefrancia@springfieldtown..com", nivel=2)
    camisa = Ropa("Camisa", 20, "M")
    cliente_comun.hacer_compra(camisa, 2)
    cliente_vip.hacer_compra(camisa, 2)
    cliente_vip.enviar_correo_promocional("¡Ofertas exclusivas para clientes VIP!")


