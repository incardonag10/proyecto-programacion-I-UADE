import os

from blackjack import jugar_blackjack
from generala_v4 import jugargenerala
from poker import jugar_poker
from ruleta import jugar_ruleta


def registrar_jugador():

    print("======================================")
    print("           LOGIN DEL CASINO           ")
    print("======================================")
    print()

    errores = 0

    while errores < 3:

        nombre = input("Ingrese su nombre: ")

        if nombre == "":
            print("El nombre no puede estar vacio")
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
            print("El apellido no puede estar vacio")
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
                print("Edad invalida")
                errores += 1

            elif edad < 18:
                print("Acceso denegado. Debe ser mayor de 18 años.")
                return None, None, None, None

            else:
                break

        except ValueError:
            print("Edad invalida")
            errores += 1

    if errores == 3:
        print("Lo siento agoto los intentos. No puede jugar.")
        return None, None, None, None

    saldo = 1000
    existe = False
    lineas = []

    if os.path.exists("jugadores.txt"):

        archivo = open("jugadores.txt", "r")

        lineas = archivo.readlines()

        archivo.close()

        for linea in lineas:

            datos = linea.strip().split(" | ")

            nom = datos[0].split(": ")[1]
            ape = datos[1].split(": ")[1]

            if nom == nombre and ape == apellido:

                edad = int(datos[2].split(": ")[1])
                saldo = int(datos[3].split(": ")[1])

                existe = True
                break

    if not existe:

        archivo = open("jugadores.txt", "a")

        archivo.write("Nombre: " + nombre +
                      " | Apellido: " + apellido +
                      " | Edad: " + str(edad) +
                      " | Saldo: " + str(saldo) + "\n")

        archivo.close()

        print("Registro exitoso")
        print("Bienvenido", nombre, apellido)

    else:

        print()
        print("Bienvenido nuevamente", nombre, apellido)

    return nombre, apellido, edad, saldo


def menu():

    nombre, apellido, edad, saldo = registrar_jugador()

    if nombre != None:

        while True:

            print()
            print("========================================")
            print("                CASINO                  ")
            print("========================================")
            print()
            print(f"Jugador: {nombre} {apellido}")
            print(f"Edad: {edad}")
            print(f"Saldo general: ${saldo}")

            print("1. Ruleta")
            print("2. Blackjack")
            print("3. Generala")
            print("4. Poker")
            print("0. Salir")

            opcion = input("Elegi una opcion: ")

            if opcion == "1":
                saldo = jugar_ruleta(nombre, apellido, saldo)

            elif opcion == "2":
                saldo = jugar_blackjack(nombre, apellido, saldo)

            elif opcion == "3":
                saldo = jugargenerala(nombre, apellido, saldo)

            elif opcion == "4":
                saldo = jugar_poker(nombre, apellido, saldo)

            elif opcion == "0":

                if os.path.exists("jugadores.txt"):

                    archivo = open("jugadores.txt", "r")

                    lineas = archivo.readlines()

                    archivo.close()

                    archivo = open("jugadores.txt", "w")

                    for linea in lineas:

                        datos = linea.strip().split(" | ")

                        nom = datos[0].split(": ")[1]
                        ape = datos[1].split(": ")[1]

                        if nom == nombre and ape == apellido:

                            archivo.write("Nombre: " + nombre +
                                          " | Apellido: " + apellido +
                                          " | Edad: " + str(edad) +
                                          " | Saldo: " + str(saldo) + "\n")

                        else:

                            archivo.write(linea)

                    archivo.close()

                print("Gracias por jugar!")
                break

            else:

                print("Opcion invalida")
                input("Presiona ENTER para continuar...")


if __name__ == "__main__":
    menu()