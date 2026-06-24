<<<<<<< HEAD
import os

from blackjack import jugar_blackjack
from generala import jugar_generala
from poker import jugar_poker
=======
from blackjack import jugar_blackjack

>>>>>>> ruleta
from ruleta import jugar_ruleta



def registrar_jugador():
    
    print("======================================")
    print("        REGISTRO DEL CASINO           ")
    print("======================================")
  
    errores = 0

    while errores < 3:

        nombre = input("Ingrese su nombre: ")

        if nombre == "":
            print("El nombre no puede estar vacío")
            errores += 1

        elif " " in nombre:
            print("Ingrese un solo nombre")
            errores += 1

        else:
            nombre = nombre.capitalize()
            break


    while errores < 3:

        apellido = input("Ingrese su apellido: ")

        if apellido == "":
            print("El apellido no puede estar vacío")
            errores += 1

        elif " " in apellido:
            print("Ingrese un solo apellido")
            errores += 1

        else:
            apellido = apellido.capitalize()
            break


    while errores < 3:

        try:
            edad = int(input("Ingrese su edad: "))

            if edad <= 0:
                print("Edad inválida")
                errores += 1

            elif edad < 18:
                print("Acceso denegado. Debe ser mayor de 18 años.")
                return None, None, None

            else:
                break

        except ValueError:
            print("Edad inválida")
            errores += 1


    if errores == 3:
        print("Lo siento agoto los intentos. No puede jugar.")
        return None, None, None

    print("Registro exitoso")
<<<<<<< HEAD
    print("Bienvenido", nombre, apellido)    
    
    archivo = open("jugadores.txt", "a")

    archivo.write("Nombre: " + nombre +
                  " | Apellido: " + apellido +
                  " | Edad: " + str(edad) +
                  " | Saldo: 1000\n")

    archivo.close()



=======
    print("Bienvenido", nombre, apellido)
>>>>>>> ruleta

    return nombre, apellido, edad
def menu():
    
    nombre, apellido, edad = registrar_jugador()

    if nombre != None and apellido != None and edad != None:
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
            print("3. Generala")
            print("4. Poker")
            print("0. Salir")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                saldo = jugar_ruleta (nombre, apellido, saldo)

            elif opcion == "2":
                saldo = jugar_blackjack (nombre, apellido, saldo)

            elif opcion == "3":
                saldo = jugar_generala (nombre, apellido, saldo)

            elif opcion == "4":
                saldo = jugar_poker (nombre, apellido, saldo)

            elif opcion == "0":
                print("Gracias por jugar!")
<<<<<<< HEAD
                archivo = open("jugadores.txt", "a")

                archivo.write("Nombre: " + nombre +
                                " | Apellido: " + apellido +
                                " | Edad: " + str(edad) +
                                " | Saldo Final: " + str(saldo) + "\n")

                archivo.close()
=======
>>>>>>> ruleta
                break

            else:
                print("Opción inválida")
                input("Presioná ENTER para continuar...")

if __name__ == "__main__":
    menu()
