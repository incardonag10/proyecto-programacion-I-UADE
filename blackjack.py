def jugar_blackjack():

    import random

    def crear_mazo():
        mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        random.shuffle(mazo)
        return mazo

    mazo = crear_mazo()
    pos = 0

    #al momento de sacar un a carta, chequea si ya esta en la ultima carta para mezclarlo de vuelta y volver el prinvipio
    def sacar_carta():
        global mazo, pos

        if pos >= len(mazo):
            mazo = crear_mazo()
            pos = 0
            print("Se mezclo un mazo nuevo")

        carta = mazo[pos]
        pos += 1
        return carta


    arranque = input("Desea jugar Snicker´s blackjack? (si o no): ")
    blackjack = False
    if arranque == "si":
        blackjack = True

    banco = int(input("Ingrese monto a depositar en el banco: $"))

    while blackjack:
        apuesta = float(input("Elija monto a apostar: $"))
        while apuesta > banco:
            print("No hay fondos suficientes")
            apuesta = float(input("Elija monto a apostar: $"))
        
        carta_jugador_1 = sacar_carta()
        carta_casa_1 = sacar_carta()
        carta_jugador_2 = sacar_carta()
        carta_casa_2 = sacar_carta()

        print(f"Primer carta del jugador: {carta_jugador_1}")
        print(f"Primer carta de la casa: {carta_casa_1}")
        print(f"Segunda carta del jugador: {carta_jugador_2}")

        if carta_jugador_1 == 1:
            carta_jugador_1 = 11
        elif carta_jugador_2 == 1:
            carta_jugador_2 = 11
        elif carta_jugador_1 == 1 and carta_jugador_2 == 1:
            total_jugador = 12

        total_jugador = carta_jugador_1 + carta_jugador_2

        if total_jugador == 21:
            print("BLACKJACK")
            apuesta = apuesta + (apuesta * 0.5)

        print(f"Total del jugador: {total_jugador}")

        total_casa = carta_casa_1 + carta_casa_2

        decision = int(input("Escriba 0 para quedarse o 1 para pedir otra carta: "))

        #una vez se elije si sacar o no otra carta, se crea un ciclo en el cual si se pasa de 21 se corta
        while decision == 1 and total_jugador < 22:
            nueva_carta = sacar_carta()
            print(nueva_carta)
            if total_jugador < 11 and nueva_carta == 1:
                nueva_carta = int(input("Salio un as, prefiere que valga 1 o 11? "))
                while nueva_carta != 1 and nueva_carta != 11:
                    nueva_carta = int(input("Numero no valido, 1 o 11: "))
            total_jugador += nueva_carta
            print(f"Total: {total_jugador}")
            if total_jugador >= 22:
                break
            decision = int(input("Escriba 0 para quedarse o 1 para pedir otra carta: "))


        if total_jugador > 21:
            print("MANO PERDIDA")
            banco -= apuesta
            print(f"Fondos: ${banco}")
        else:
            print(f"Total de la casa: {total_casa}")
            if total_casa < total_jugador:
                while total_casa < total_jugador and total_casa < 22:
                    nueva_carta_casa = sacar_carta()
                    print(nueva_carta_casa)
                    total_casa += nueva_carta_casa
                    print(f"Total de la casa: {total_casa}")

            if total_casa > 21:
                print("MANO GANADA")
                banco += apuesta
                print(f"fondos: ${banco}")
            elif total_casa < total_jugador:
                print("MANO GANADA")
                banco += apuesta
                print(f"fondos: ${banco}")
            elif total_casa > total_jugador:
                print("MANO PERDIDA")
                banco -= apuesta
                print(f"fondos: ${banco}")
            else:
                print("EMPATE")
                print(f"Fondos: ${banco}")

        if banco <= 0:
            print("Se ha quedado sin fondos")
            print("GAME OVER")
            blackjack = False
        else:
            revancha = input("Quiere jugar otra ronda? (si o no)")
            if revancha == "no":
                blackjack = False

if __name__ == "__main__":
    jugar_blackjack()

            
            







