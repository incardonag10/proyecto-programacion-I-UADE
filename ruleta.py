import random
import time
import os

#funciones

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
    print("\n🎡 Girando la ruleta...")
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


#programa

def jugar_ruleta():
    saldo = 1000

    while saldo > 0:
        limpiar_pantalla()
        print("🎰 RULETA 🎰")
        print(f"💰 Saldo: {saldo}")

        mostrar_menu()

        try:
            try:
                opcion = int(input("\nElegí una opción: "))
            except ValueError:
                print("❌ Ingresá un número válido")
                time.sleep(1.5)
                continue

            if opcion not in [1, 2, 3, 4, 5, 6]:
                print("❌ Opción inválida")
                time.sleep(1.5)
                continue

            apuesta = int(input("¿Cuánto querés apostar?: "))

            if apuesta <= 0 or apuesta > saldo:
                print("❌ Apuesta inválida")
                time.sleep(1.5)
                continue

            #eleccion

            if opcion == 1:
                eleccion = int(input("Elegí un número (0-36): "))
                if eleccion < 0 or eleccion > 36:
                    print("❌ Número inválido")
                    time.sleep(1.5)
                    continue

            elif opcion == 2:
                eleccion = input("Elegí color (rojo/negro): ").lower()

            elif opcion == 3:
                eleccion = input("Elegí (par/impar): ").lower()

            elif opcion == 4:
                eleccion = input("Elegí (bajo/alto): ").lower()

            elif opcion == 5:
                eleccion = int(input("Elegí docena (1:1-12 / 2:13-24 / 3:25-36): "))

            elif opcion == 6:
                eleccion = int(input("Elegí columna (1 / 2 / 3): "))

            #resultado

            numero, color = girar_ruleta()
            print(f"\n🎯 Salió: {numero} ({color})")

            gano = False

            #numero exacto
            if opcion == 1 and eleccion == numero:
                if numero == 0:
                    saldo += apuesta * 36
                else:
                    saldo += apuesta * 35
                gano = True

            #color
            elif opcion == 2 and eleccion == color:
                saldo += apuesta
                gano = True

            #par e impar
            elif opcion == 3 and numero != 0:
                if eleccion == "par" and numero % 2 == 0:
                    saldo += apuesta
                    gano = True
                elif eleccion == "impar" and numero % 2 != 0:
                    saldo += apuesta
                    gano = True

            #bajo y alto
            elif opcion == 4:
                if eleccion == "bajo" and 1 <= numero <= 18:
                    saldo += apuesta
                    gano = True
                elif eleccion == "alto" and 19 <= numero <= 36:
                    saldo += apuesta
                    gano = True

            #docenas
            elif opcion == 5:
                if eleccion == 1 and 1 <= numero <= 12:
                    saldo += apuesta * 2
                    gano = True
                elif eleccion == 2 and 13 <= numero <= 24:
                    saldo += apuesta * 2
                    gano = True
                elif eleccion == 3 and 25 <= numero <= 36:
                    saldo += apuesta * 2
                    gano = True

            #columnas
            elif opcion == 6 and numero != 0:
                if eleccion == 1 and numero % 3 == 1:
                    saldo += apuesta * 2
                    gano = True
                elif eleccion == 2 and numero % 3 == 2:
                    saldo += apuesta * 2
                    gano = True
                elif eleccion == 3 and numero % 3 == 0:
                    saldo += apuesta * 2
                    gano = True

            if gano:
                print("🎉 Ganaste!")
            else:
                saldo -= apuesta
                print("💸 Perdiste")

            input("\nPresioná ENTER para continuar...")

        except ValueError:
            print("❌ Error: ingresá valores válidos")
            time.sleep(1.5)

    
    limpiar_pantalla()
    print("=" * 40)
    print("💀 FIN DEL JUEGO 💀".center(40))
    print("=" * 40)
    print(f"\nSaldo final: {saldo}")
    print("\nTe quedaste sin dinero.")
    print("\nGracias por jugar 🎰")

    input("\nPresioná ENTER para salir...")


#ejecucion

if __name__ == "__main__":
    jugar_ruleta()