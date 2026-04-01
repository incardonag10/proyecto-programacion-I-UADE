import random
import time
import os

# funciones

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def obtener_color(numero):
    if numero == 0:
        return "verde"
    elif numero % 2 == 0:
        return "negro"
    else:
        return "rojo"


def girar_ruleta():
    print("\nGirando la ruleta...")
    time.sleep(1)

    numero = random.randint(0, 36)
    color = obtener_color(numero)

    return numero, color


def mostrar_menu():
    print("\n--- TIPOS DE APUESTA ---")
    print("1. Número exacto (x36 si es 0, x35 resto)")
    print("2. Color (rojo/negro) (x2)")
    print("3. Par / Impar (x2)")
    print("4. Bajo (1-18) / Alto (19-36) (x2)")
    print("5. Docenas (1-12 / 13-24 / 25-36) (x3)")
    print("6. Columnas (1 / 2 / 3) (x3)")
    print("0. Girar ruleta")
    print("9. Volver al menú principal")


def pedir_eleccion(opcion):
    if opcion == 1:
        eleccion = int(input("Elegí un número (0-36): "))
        if eleccion < 0 or eleccion > 36:
            print("Número inválido")
            return None

    elif opcion == 2:
        eleccion = input("Elegí color (rojo/negro): ").lower()
        if eleccion not in ["rojo", "negro"]:
            print("Color inválido")
            return None

    elif opcion == 3:
        eleccion = input("Elegí (par/impar): ").lower()
        if eleccion not in ["par", "impar"]:
            print("Opción inválida")
            return None

    elif opcion == 4:
        eleccion = input("Elegí (bajo/alto): ").lower()
        if eleccion not in ["bajo", "alto"]:
            print("Opción inválida")
            return None

    elif opcion == 5:
        eleccion = int(input("Elegí docena (1:1-12 / 2:13-24 / 3:25-36): "))
        if eleccion not in [1, 2, 3]:
            print("Docena inválida")
            return None

    elif opcion == 6:
        eleccion = int(input("Elegí columna (1 / 2 / 3): "))
        if eleccion not in [1, 2, 3]:
            print("Columna inválida")
            return None

    return eleccion


def calcular_ganancia(opcion, eleccion, numero, color, apuesta):
    if opcion == 1:
        if eleccion == numero:
            if numero == 0:
                return apuesta * 36
            else:
                return apuesta * 35

    elif opcion == 2:
        if eleccion == color:
            return apuesta

    elif opcion == 3 and numero != 0:
        if eleccion == "par" and numero % 2 == 0:
            return apuesta
        elif eleccion == "impar" and numero % 2 != 0:
            return apuesta

    elif opcion == 4:
        if eleccion == "bajo" and 1 <= numero <= 18:
            return apuesta
        elif eleccion == "alto" and 19 <= numero <= 36:
            return apuesta

    elif opcion == 5:
        if eleccion == 1 and 1 <= numero <= 12:
            return apuesta * 2
        elif eleccion == 2 and 13 <= numero <= 24:
            return apuesta * 2
        elif eleccion == 3 and 25 <= numero <= 36:
            return apuesta * 2

    elif opcion == 6 and numero != 0:
        if eleccion == 1 and numero % 3 == 1:
            return apuesta * 2
        elif eleccion == 2 and numero % 3 == 2:
            return apuesta * 2
        elif eleccion == 3 and numero % 3 == 0:
            return apuesta * 2

    return 0


# programa

def jugar_ruleta(nombre, apellido, saldo):
    while saldo > 0:
        limpiar_pantalla()
        print("== RULETA ==")
        print(f"Jugador: {nombre} {apellido}")
        print(f"Saldo: {saldo}")

        apuestas = []
        total_apostado = 0

        while True:
            mostrar_menu()

            try:
                opcion = int(input("\nElegí una opción (0 para girar, 9 para salir): "))
            except ValueError:
                print("Error: Ingresá un número válido")
                time.sleep(1.5)
                continue

            if opcion == 9:
                print("Volviendo al menú principal...")
                time.sleep(1)
                return saldo

            if opcion == 0:
                if len(apuestas) == 0:
                    print("Primero tenés que hacer al menos una apuesta")
                    time.sleep(1.5)
                    continue
                break

            if opcion not in [1, 2, 3, 4, 5, 6]:
                print("Error: Opción inválida")
                time.sleep(1.5)
                continue

            try:
                apuesta = int(input("¿Cuánto querés apostar?: "))
            except ValueError:
                print("Error: ingresá un monto válido")
                time.sleep(1.5)
                continue

            if apuesta <= 0:
                print("Apuesta inválida")
                time.sleep(1.5)
                continue

            if total_apostado + apuesta > saldo:
                print("No tenés saldo suficiente para esa apuesta")
                time.sleep(1.5)
                continue

            try:
                eleccion = pedir_eleccion(opcion)
            except ValueError:
                print("Error: ingresá valores válidos")
                time.sleep(1.5)
                continue

            if eleccion is None:
                time.sleep(1.5)
                continue

            apuestas.append([opcion, apuesta, eleccion])
            total_apostado += apuesta

            print("\nApuesta agregada correctamente")
            print(f"Total apostado en esta ronda: {total_apostado}")
            print(f"Saldo disponible restante: {saldo - total_apostado}")
            time.sleep(1.5)

        numero, color = girar_ruleta()
        print(f"\nSalió: {numero} ({color})")

        ganancia_total = 0

        for apuesta_actual in apuestas:
            opcion = apuesta_actual[0]
            monto = apuesta_actual[1]
            eleccion = apuesta_actual[2]

            ganancia = calcular_ganancia(opcion, eleccion, numero, color, monto)

            if ganancia > 0:
                print(f"Ganaste una apuesta de {monto}. Premio: {ganancia}")
                ganancia_total += ganancia
            else:
                print(f"Perdiste una apuesta de {monto}")

        saldo = saldo - total_apostado + ganancia_total

        print(f"\nTotal apostado: {total_apostado}")
        print(f"Total ganado: {ganancia_total}")
        print(f"Saldo actual: {saldo}")

        input("\nPresioná ENTER para continuar...")

    limpiar_pantalla()
    print("=" * 40)
    print(" FIN DEL JUEGO ".center(40))
    print("=" * 40)
    print(f"\nSaldo final: {saldo}")
    print("\nTe quedaste sin dinero.")
    print("\nGracias por jugar a la ruleta!")

    input("\nPresioná ENTER para volver al menú...")

    return saldo


# ejecucion

if __name__ == "__main__":
    jugar_ruleta("Invitado", "Local", 1000)