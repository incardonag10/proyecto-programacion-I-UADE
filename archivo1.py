from ruleta import jugar_ruleta

import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    limpiar_pantalla()
    while True:
        print("=" * 40)
        print(" CASINO ".center(40))
        print("=" * 40)
        print("1. Ruleta")
        print("2. Blackjack")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            jugar_ruleta()
        
        elif opcion == "0":
            print("Gracias por jugar!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()