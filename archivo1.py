from ruleta import jugar_ruleta
from blackjack import jugar_blackjack
import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def registrar_jugador():
    limpiar_pantalla()
    print("=" * 40)
    print(" REGISTRO DEL CASINO ".center(40))
    print("=" * 40)

    while True:
        nombre = input("Ingrese su nombre: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío")
            continue

        if " " in nombre:
            print("Ingrese solo un nombre (sin apellido)")
            continue

        if not nombre.isalpha():
            print("El nombre solo debe contener letras")
            continue

        nombre = nombre.capitalize()
        break

    while True:
        apellido = input("Ingrese su apellido: ").strip()

        if apellido == "":
            print("El apellido no puede estar vacío")
            continue

        if " " in apellido:
            print("Ingrese solo un apellido")
            continue

        if not apellido.isalpha():
            print("El apellido solo debe contener letras")
            continue

        apellido = apellido.capitalize()
        break

    while True:
        try:
            edad = int(input("Ingrese su edad: "))

            if edad <= 0:
                print("Edad inválida")
                continue

            break
        except ValueError:
            print("Edad inválida. Ingrese un número.")

    if edad < 18:
        print("\nAcceso denegado. Debe ser mayor de 18 años.")
        input("Presioná ENTER para salir...")
        return None, None, None

    return nombre, apellido, edad


def menu():
    nombre, apellido, edad = registrar_jugador()

    if edad is None:
        return

    saldo = 1000

    while True:
        limpiar_pantalla()
        print("=" * 40)
        print(" CASINO ".center(40))
        print("=" * 40)

        print(f"Jugador: {nombre} {apellido}")
        print(f"Edad: {edad}")
        print(f"Saldo general: ${saldo}")

        print("\n1. Ruleta")
        print("2. Blackjack")
        print("0. Salir")

        opcion = input("\nElegí una opción: ")

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