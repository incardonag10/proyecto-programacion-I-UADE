saldo = 1000
def jugar_blackjack(nombre, apellido, banco):
    import random

    def crear_mazo():
        mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        random.shuffle(mazo)
        return mazo

    mazo = crear_mazo()
    pos = 0

    #al momento de sacar un a carta, chequea si ya esta en la ultima carta para mezclarlo de vuelta y volver el principio
    def sacar_carta():
        nonlocal mazo, pos #nonlocal para poder manipular datos ajenos a la funcion

        if pos >= len(mazo):
            mazo = crear_mazo()
            pos = 0
            print("Se mezclo un mazo nuevo")

        carta = mazo[pos]
        pos += 1
        return carta
    
    print()
    print("===="*10)
    print("BLACKJACK".center(40))
    print("===="*10)
    print()

    blackjack = True
    print("Bienvenido a BLACKJACK, ", nombre, apellido)
    print(f"Fondos: ${banco}")
    print()

    respuesta = input("ENTER para jugar o 0 para volver al menu: ")

    if respuesta == "0":
        return int(banco)


    while blackjack:
        jugador_as = False
        blackjack_jugador = False
        casa_as = False
        casa_blackjack = False
        apuesta_as = False
        confir = False
        apuesta = float(input("Elija monto a apostar: $"))
        while apuesta <= 0 or apuesta > banco:
            apuesta = int(input("Apuesta no valida, ingrese otra: $"))
        
        carta_jugador_1 = sacar_carta()
        carta_casa_1 = sacar_carta()
        carta_jugador_2 = sacar_carta()
        carta_casa_2 = sacar_carta()

        print(f"\nPrimer carta del jugador: {carta_jugador_1}")
        print(f"Primer carta de la casa: {carta_casa_1}")
        print(f"Segunda carta del jugador: {carta_jugador_2}")

        total_jugador = carta_jugador_1 + carta_jugador_2
        total_casa = carta_casa_1 + carta_casa_2

        #si sale un as se activa x_as, mas adelante se usa para salvar al jugador o la maquina si se pasan
        #caso jugador_as
        if carta_jugador_1 == 1 and carta_jugador_2 == 1:
            total_jugador = 12
            jugador_as = True
        elif carta_jugador_1 == 1:
            carta_jugador_1 = 11
            jugador_as = True
            total_jugador = carta_jugador_1 + carta_jugador_2
        elif carta_jugador_2 == 1:
            carta_jugador_2 = 11
            jugador_as = True
            total_jugador = carta_jugador_1 + carta_jugador_2  
        
        #caso casa_as
        if carta_casa_1 == 1 and carta_casa_2 == 1:
            total_casa = 12
            casa_as = True
            apuesta_as = True
        elif carta_casa_1 == 1:
            carta_casa_1 = 11
            casa_as = True
            apuesta_as = True
            total_casa = carta_casa_1 + carta_casa_2
        elif carta_casa_2 == 1:
            carta_casa_2 = 11
            casa_as = True
            total_casa = carta_casa_1 + carta_casa_2
        #si a la casa le sale un as en la primer tirada, se activa apuesta_as, que posteriormente habilita otra apuesta
        

        print(f"Total del jugador: {total_jugador}")

        #retomamos apuesta_as, si se decide apostar a que sale un 10, se resta la mitad de la apuesta para actuar como una especie de seguro
        #si se pierde la apuesta principal y ganas el seguro, quedas en 0, caso contrario de perder ambas perdes un 150% de la apuesta
        if apuesta_as:
            print("Le salio un as a la casa...")
            sale_10 = input("Apostas a que sale un 10? (si o no) ").lower()
            while sale_10 != "si" and sale_10 != "no":
                print("Respuesta inválida. Ingrese solo si o no.")
                sale_10 = input("Quiere apostar a que sale un 10? (si o no): ").lower()
            if sale_10 == "si":
                if banco - apuesta < (apuesta / 2):
                    print("No hay fondos necesarios para volver a apostar") #no podes apostar si no tenes los fondos necesarios
                else:
                    confir = True
                    segunda_apuesta = apuesta / 2
                    print(f"apostaste ${segunda_apuesta}")

        if total_jugador == 21:
            print("BLACKJACK")
            blackjack_jugador = True
            apuesta = apuesta * 1.5

        decision = input("\nQuiere pedir otra carta? (si o no): ").lower()
        while decision != "si" and decision != "no":
                print("Respuesta inválida. Ingrese solo si o no.")
                decision = input("Quiere pedir otra carta? (si o no): ").lower()

        #una vez se elije si sacar o no otra carta, se crea un ciclo en el cual si se pasa de 21 se corta
        while decision == "si" and total_jugador < 22:
            print("Sacas otra carta...")
            nueva_carta = sacar_carta()
            print(f"+{nueva_carta}")
            if total_jugador >= 11 and nueva_carta == 1:
                nueva_carta = 1
            elif nueva_carta == 1 and total_jugador < 11:
                jugador_as = True
                nueva_carta = 11
            total_jugador += nueva_carta

            print(f"Total: {total_jugador}")

            if total_jugador >= 22:
                if jugador_as == True:
                    total_jugador = total_jugador - 10
                    print("se resto el as anterior")
                    print("nuevo total: ", total_jugador)
                    jugador_as = False
                else:
                    break
            decision = input("\nQuiere pedir otra carta? ").lower()
            while decision != "si" and decision != "no":
                print("Respuesta inválida. Ingrese solo si o no.")
                decision = input("Quiere pedir otra carta? (si o no): ").lower()

        if total_jugador > 21:
            print("TE PASASTE, MANO PERDIDA")
            banco -= apuesta
            print(f"Fondos: ${banco}")
            print(f"\nSegunda carta de la casa: {carta_casa_2}")
            print(f"Total de la casa: {total_casa}")
            if confir and carta_casa_2 == 10:
                print("\nSalio un 10, ganas la segunda apuesta")
                banco += segunda_apuesta 
            elif confir and carta_casa_2 != 10:
                print("No salio un 10, perdes la segunda apuesta")
                banco -= segunda_apuesta
        else:
            print(f"\nSegunda carta de la casa: {carta_casa_2}")
            print(f"Total de la casa: {total_casa}")
            if confir and carta_casa_2 == 10:
                print("\nSalio un 10, ganas la segunda apuesta")
                banco += segunda_apuesta 
            elif confir and carta_casa_2 != 10:
                print("No salio un 10, perdes la segunda apuesta")
                banco -= segunda_apuesta

            if total_casa == 21:
                print("\nBLACKJACK DE LA CASA\n")
                casa_blackjack = True
            
            while total_casa < 17:
                print("\nLa casa saca otra carta...")
                nueva_carta_casa = sacar_carta()
                print(f"+{nueva_carta_casa}")
                if nueva_carta_casa == 1:
                    if total_casa >= 11:
                        nueva_carta_casa = 1
                    else:
                        nueva_carta_casa = 11
                        casa_as = True
                total_casa += nueva_carta_casa
                if total_casa > 21 and casa_as:
                    casa_as = False
                    total_casa -= 10
                    print("La casa se salva por el as")

                print(f"Total de la casa: {total_casa}")

            if total_casa > 21:
                print("\nMANO GANADA")
                banco += apuesta
                print(f"fondos: ${banco}")
            elif total_casa < total_jugador:
                print("\nMANO GANADA")
                banco += apuesta
                print(f"fondos: ${banco}")
            elif total_casa > total_jugador:
                print("\nMANO PERDIDA")
                banco -= apuesta
                print(f"fondos: ${banco}")
            elif total_casa == total_jugador and blackjack_jugador and not casa_blackjack:
                print("\nGanas por hacer blackjack")
                banco += apuesta
                print(f"Fondos: ${banco}")
            elif total_casa == total_jugador and casa_blackjack and not blackjack_jugador:
                print("\nPerdes porque la casa hizo blackjack")
                banco -= apuesta
                print(f"Fondos: ${banco}")
            else:
                print("\nEMPATE")
                print(f"Fondos: ${banco}")

        if banco <= 0:
            print("\nSe ha quedado sin fondos")
            print("Fin del juego")
            blackjack = False
        else:
            revancha = input("\nQuiere jugar otra ronda? (si o no): ").lower()
            while revancha != "si" and revancha != "no":
                print("Respuesta inválida. Ingrese solo si o no.")
                revancha = input("Quiere jugar otra ronda? (si o no): ").lower()

            if revancha == "no":
                blackjack = False
                print("Adios")
        print("-----------------------")
    return int(banco)

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    jugar_blackjack(nombre, apellido, saldo)






