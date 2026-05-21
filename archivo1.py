from ruleta import jugar_ruleta
from blackjack import jugar_blackjack



def registrar_jugador():
    
    print("======================================")
    print("        REGISTRO DEL CASINO           ")
    print("======================================")

    
    errores = 0

    while errores < 3:

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        
        try:
            edad = int(input("Ingrese su edad: "))
        except ValueError:
            print("Edad inválida")
            errores += 1

        if nombre == "":
            print("El nombre no puede estar vacíos")
            print("Por favor, ingrese un nombre válido")
            errores += 1
        
        elif " " in nombre:
            print("Por favor, ingrese un solo nombre.")
            errores += 1

        elif apellido == "":
            print("El apellido no puede estar vacío")
            print("Por favor, ingrese un apellido válido")
            errores += 1

        elif " " in apellido:
            print("Por favor, ingrese un solo apellido.")
            errores += 1

        elif edad <= 0:
            print("Edad inválida")
            print("Por favor, ingrese una edad válida")
            errores += 1

        elif edad < 18:
            print("Acceso denegado. Debe ser mayor de 18 años.")
            input("Presioná ENTER para salir...")
            exit()

        else:
            nombre = nombre.capitalize()
            apellido = apellido.capitalize()
            print("Registro exitoso")
            print("Bienvenido", nombre, apellido)
            break

            

    if errores == 3:
        print("El usuario agotó los intentos. Lo siento, no puede jugar.")

  
    

    return nombre, apellido, edad


def menu():
    nombre, apellido, edad = registrar_jugador()

    

    saldo = 1000

    while True:
        print("========================================")
        print("                CASINO                  ")
        print("========================================")

        print(f"Jugador: {nombre} {apellido}")
        print(f"Edad: {edad}")
        print(f"Saldo general: ${saldo}")

        print("1. Ruleta")
        print("2. Blackjack")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            saldo = jugar_ruleta(nombre, apellido, saldo)

        elif opcion == "2":
            saldo = jugar_blackjack(nombre, apellido, saldo)

        elif opcion == "0":
            print("Gracias por jugar!")
            break

        else:
            print("Opción inválida")
            input("Presioná ENTER para continuar...")


if __name__ == "__main__":
    menu()