
# -*- coding: utf-8 -*-
"""Primera pre entrega -- Cumaco -- Poyecto Python Web.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EL91vNFdZp3_FYHroOujDgHpN227MuGM

**Generamos un diccionario vacio, esto con la intención de trasladarlo a un dataset y poder organizar la información recepcionada**
"""

registros_nuevos=[]

"""**Función Registro:**
Generamos la primera función para permitirle al usuario generar su registro, dentro del código solicitamos 3 datos:
- Nombre completo
- Usuario
- Contraseña

La intención es que el código solicite el nombre completo, difiera entre el nombre y el Apellido, de esta forma le permitira generar un saludo personalizado, ya cumpliendo con esta tarea pasara a solicitar usuario y contraseña para generar el registro.

Dentro del nombre completo sumamos un "while" esto con el fin de parametrizar el nombre, solicitando que se ingrese nombre y apellido, ademas de que los caracteres ingresados sean letras y no números, en este caso se utiliza la ayuda de la función "isalpha()"

Al invocar a la función registro procede a generar la solicitud de los datos necesarios para el registro.
"""
import json

def Registro():

#Creación de un while de esta forma parametrizamos la información que ingresa el usuario:
    while True:
        nombre_completo = input("Ingresa tu nombre completo (Nombre y Apellido): ")
        #Debemos dividir en dos el nombre completo ingresado, de esta forma podemos identificar que poseea dos palabras como se solicita.
        palabras = nombre_completo.split()
        #Al generar la partición de las dos palabras, le pedimos a "isalpla" que reconozca si los caracteres son letras.
        if len(palabras) >= 2 and all(palabra.isalpha() for palabra in palabras):
        #Se pasara a separar el nombre como primera palabra, esto para generar un saludo personalizado,
            primer_nombre = palabras[0]
            print(f"Hola, {primer_nombre}! ¡Bienvenido/a a nuestra página!")
            break
        #En caso de que alguno de los parámetros no se cumpla solicitara una nueva oportunidad para ingresar el nombre.
        else:
            print("Por favor, ingresa un nombre completo válido que contenga un nombre y un apellido, ademas de solo letras. Inténtalo de nuevo.")

    #Procedemos a solicitar el ingreso del usuario de logueo
    usuario = input(f"Muy Bien, para iniciar {primer_nombre}, ingresa un usuario: ")

    #Posterior pasamos a solicitar la contraseña, en este punto generamos un len para que sea de 6 digitos mínimo.
    while True:
        contraseña = input(f"Por ultimo {primer_nombre}, ingresa una contraseña, recuerda no debe ser menor de 6 dígitos: ")
        if len(contraseña) >= 6:
            print("Excelente, ¡Bienvenido/a a nuestra pagina!")
            break
   #Si la contraseña no cumple con los parámetros encontes solicitamos que lo intente de nuevo.
        else:
            print("La contraseña debe tener al menos 6 caracteres. Por favor, inténtalo de nuevo.")

    #Por ultimo solicitamos que la información sea sumada a nuestro dataset inicial.
    registros_nuevos.append({
        'nombre_completo': nombre_completo,
        'usuario': usuario,
        'contraseña': contraseña
    })

Registro()

"""**Función verificación de registros:**
En esta función decidi emplear herramientas que poseo en conocimiento para mejorar este aspecto de registro, importando Pandas me permite generar un dataset con los datos que se estan ingresando directamente por el usuario, a futuro esto nos permitira generar una extracción mas limpia de la información, ya clasificada.
"""
import pandas as pd

def Verificacion_de_registros():

    #Definimos una variable para la reación de nuestro dataframe a traves de la lista "registros_nuevos"
    Registros = pd.DataFrame(registros_nuevos)

    # Usamos un print para brindarle contexto a la visualización
    print(Registros)

"""Invocamos a la definición para visualizar el dataset con la información ingresada."""

Verificacion_de_registros()

"""**Función restablecer_contraseña:**

Esta función sera invocada cuando se genere una situación de recupero de contraseña en el proceso de la función Log_In, vamos a solicitarle el nombre completo al usuario como parámetro de seguridad para poder avanzar con el cambio de contraseña.
"""

def restablecer_contraseña(usuario):

  #Generamos un input para solicitar el ingreso del nombre completo, al ser el unico tercer dato que poseemos lo usaremos como parámetro.
    nombre_completo = input("Para restablecer tu contraseña, introduce tu nombre completo registrado: ")
    for registro in registros_nuevos:
      #Se realiza una comparación tanto sobre usuario como sobre registro, esta parte nos permite invocar la función si ademas de no saber el usuario el usuario no recuerda la contraseña.
        if registro['usuario'] == usuario or registro['nombre_completo'] == nombre_completo:
            nueva_contraseña = input("Introduce tu nueva contraseña (mínimo 6 caracteres): ")
            #Mantenemos los parámetros en cuanto al ingreso de la contraseña la misma debe tener 6 o mas carácteres.
            while len(nueva_contraseña) < 6:
                print("La contraseña debe tener al menos 6 caracteres. Inténtalo de nuevo.")
                nueva_contraseña = input("Introduce tu nueva contraseña: ")
            #Si se cumple con el parámetro de ingreso, se procedera a remplazar la anterior con la nueva contraseña.
            registro['contraseña'] = nueva_contraseña
            print("Tu contraseña ha sido actualizada exitosamente.")
            return True
    print("Los datos proporcionados no coinciden con nuestros registros.")
    return False  # Si el nombre completo ingresado no es correcto informara la imposibilidad de seguir.

"""**Función restablecer_usuario:**

En esta función lo que queremos lograr es que en caso de que el usuario olvida de id, recuerde su nombre completo y contraseña, podra imgresar a la pagina, sin embargo de forma automática debera generar un nuevo usuario de ingreso.
"""

def restablecer_usuario(nombre_completo):

  #Le solicitamos al usuario ingresar su nuevo usuario
    nuevo_usuario = input("Introduce tu nuevo usuario: ")

    # Con la creación de este for podremos:
    for registro in registros_nuevos:
      #Generar una comparación con el nombre completo ingresado,
        if registro['nombre_completo'] == nombre_completo:
          #Para posteriormente generar el remplazo del usuario anterior por el nuevo.
            registro['usuario'] = nuevo_usuario
            print("Usuario restablecido con éxito.")
            return True

    print("Lo sentimos, no pudimos encontrar tu nombre completo en nuestros registros.")
    return False

"""**Función Log_In:**

Para esta función quise lograr que no solo nos limitaramos a solicitar el usuario y contraseña, sino que añadimos algunas funciones utiles básicas:

-Permitimos un intento máximo de 3 intentos para el ingreso a la plataforma.

-En caso de no lograr el ingreso procedemos a ofrecer el restablecimiento de la contraseña solicitando el unico dato exento del login, el nombre completo tal cual fue ingresado en el registro.

- Si no se ingresa el usuario de forma correcta, se brindaran 3 oportunidades de ingreso antes de solicitar como parámetro de seguridad el ingreso del nombre completo, esto a su vez le permitira al usuario pasar a usar su nombre completo como puente de ingreso a la contraseña, si recuerda la contraseña podra ingresar, si no la recuerda tendra la oportunidad de generar el recupero de la misma invocando a la definición "restablecer contraseña".
"""

def Log_In():

    #Le brindamos 3 intentos para ingresar el usuario registrado con anterioridad.
    intentos_usuario = 3
    while intentos_usuario > 0:
        usuario = input("Introduce tu usuario: ")
        for registro in registros_nuevos:
            if registro['usuario'] == usuario:
                break
        else:
            intentos_usuario -= 1
            print(f"Usuario incorrecto. Te quedan {intentos_usuario} intentos.")
            continue  # Continuar pidiendo usuario si no se encontró

        # Si dentro de los 3 intentos es ingresado el usuario con exito, pasaremos a solicitar la contraseña con los mismos parámetros, 3 intentos.
        intentos_contraseña = 3
        while intentos_contraseña > 0:
            contraseña = input("Introduce tu contraseña: ")
            if registro['contraseña'] == contraseña:
                print("Ingreso exitoso.")
                return True
            else:
                intentos_contraseña -= 1
                print(f"Contraseña incorrecta. Te quedan {intentos_contraseña} intentos.")

        # Si en este caso no se recuerda la contraaela pasaremos a ofrecer la posibilidad de recuperarla invocando a la función "restablecer_contraseña(usuario)"
        print("Has excedido el número de intentos permitidos.")
        respuesta = input("¿Quieres restablecer tu contraseña? (si/no): ")
        if respuesta.lower() == "si":
            return restablecer_contraseña(usuario)
        #Si se opta por no recuperarla generaremos un mensaje indicando que podra realizarlo en otra oportunidad
        else:
            print("Te extrañamos, recuerda que siempre puedes recuperar tu contraseña o si recuerdas la que tenías, aquí estaremos esperándote.")
            return False  # Retorna False si el usuario no quiere restablecer la contraseña

    # Retomando: Si desde el inicio no se logra el ingreso del usuario dentro de los 3 intentos,
    print("Has excedido el número de intentos para ingresar el usuario.")
    print("Por favor, ingresa tu nombre completo para continuar.")
    #Solicitaremos nuestro parámetro de seguridad para usarlo como puente a la contraseña,
    nombre_completo = input("Nombre completo: ")
    for registro in registros_nuevos:
        if registro['nombre_completo'] == nombre_completo:
            # Si se encuentra el nombre completo, permitimos ingresar la contraseña
            intentos_contraseña = 3
            while intentos_contraseña > 0:
                contraseña = input("Introduce tu contraseña: ")
                #Si la contraseña es correcta podremos ingresar y de forma automatica solicitaremos un nuevo usuario para remplazar el anterior
                if registro['contraseña'] == contraseña:
                    print("Ingreso exitoso.")
                    #Invocamos a la función correspondiente para generar el cambio de usuario
                    return restablecer_usuario(nombre_completo)
                else:
                    intentos_contraseña -= 1
                    print(f"Contraseña incorrecta. Te quedan {intentos_contraseña} intentos.")

            # Si se acaban los intentos de contraseña al ingresar el nombre completo, ofrecemos recuperarla
            print("Has excedido el número de intentos permitidos.")
            respuesta = input("¿Quieres recuperar tu contraseña? (si/no): ")
            if respuesta.lower() == "si":
                return restablecer_contraseña(usuario)  #Invocamos a la función correspondiente.
            else:
                print("Te extrañamos, recuerda que siempre puedes recuperar tu contraseña o si recuerdas la que tenías, aquí estaremos esperándote.")
                return False  # Retorna False si el usuario no quiere recuperar la contraseña
    else:
      print("No tenemos datos registrados con lo ingresado, por favor verifica la información, de otra forma te invitamos a registrarte")
      return Registro()
    

"""
Generamos un codigo para convertir el dataser en diccionario y formato json para su uso, 

"""

 # Convertimos registros_nuevos a un formato de diccionario
datos_nuevos = {'registros_nuevos': registros_nuevos}

# Ahora, supongamos que tu dataset inicial es un diccionario llamado dataset_inicial
# Vamos a agregar los nuevos datos a este dataset inicial
dataset_inicial = {}

# Combinamos el dataset inicial con los nuevos datos
dataset_inicial.update(datos_nuevos)

# Ahora, guardamos el dataset en un archivo JSON
with open("dataset.json", "w") as archivo_json:
    json.dump(dataset_inicial, archivo_json)

print("Datos guardados correctamente en dataset.json")