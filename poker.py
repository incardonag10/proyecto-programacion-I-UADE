def jugar_poker(nombre,apellido,banco):
    import random

    while True:
            print()
            print("========================================")
            print("                 POKER                  ")
            print("========================================")
            print()
            print(f"Bienvenido a POKER, {nombre} {apellido}")
            print(f"Fondos: ${banco}")
            print()
            arranque = input("Desea jugar? (si o no): ")
            if arranque.lower() == "si" or arranque.lower() == "no":
                break
            else:
                print("Entrada inválida. Ingrese si o no.")

    def main():
        nonlocal banco
        apuesta = cargar_apuesta()
        cartas = generar_cartas()
        cartas_jugador = repartir_cartas(cartas, 2)
        cartas_en_mesa = cartas_en_la_mesa(cartas)
        cartas_bot = repartir_cartas(cartas, 2)

        print("--------------------------------------------------------------------" )
        print("         Cartas del jugador:")
        mostrar_cartas(cartas_jugador)
        print("\nMesa inicial:")
        mostrar_cartas(cartas_en_mesa)

        apuesta2 = input("Desea apostar mas? (si o no): ")
        while apuesta2.lower() != "si" and apuesta2.lower() != "no":
            print("Entrada inválida. Ingrese si o no.")
            apuesta2 = input("Desea apostar mas? (si o no): ")
        if apuesta2.lower() == "si":
            apuesta_extra = cargar_apuesta()
            apuesta += apuesta_extra



        print("---------------------------------------------------------------------" )
        cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)
        print("         Mesa ronda 1:")
        mostrar_cartas(cartas_en_mesa)

        apuesta3 = input("Desea apostar mas? (si o no): ")
        while apuesta3.lower() != "si" and apuesta3.lower() != "no":
            print("Entrada inválida. Ingrese si o no.")
            apuesta3 = input("Desea apostar mas? (si o no): ")
        if apuesta3.lower() == "si":
            apuesta_extra1 = cargar_apuesta()
            apuesta += apuesta_extra1
            


        print("---------------------------------------------------------------------" )
        cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)
        print("         Mesa ronda 2:")
        mostrar_cartas(cartas_en_mesa)

        print("---------------------------------------------------------------------" )


        apuesta4 = input("Desea apostar mas? (si o no): ")
        while apuesta4.lower() != "si" and apuesta4.lower() != "no":
            print("Entrada inválida. Ingrese si o no.")
            apuesta4 = input("Desea apostar mas? (si o no): ")
        if apuesta4.lower() == "si":
            apuesta_extra2 = cargar_apuesta()
            apuesta += apuesta_extra2
            

        print("\nEl otro jugador tira sus cartas y tiene:\n")
        mostrar_cartas(cartas_bot)
        print("---------------------------------------------------------------------" )
        print(f"            Clasificacion rival: {clasificacion_cartas(cartas_en_mesa, cartas_bot)}")
        print("---------------------------------------------------------------------" )
        print(f"            Clasificación tuya: {clasificacion_cartas(cartas_en_mesa, cartas_jugador)}")
        print("---------------------------------------------------------------------" )
        print(ganador(cartas_en_mesa, cartas_jugador, cartas_bot,apuesta))
        print("---------------------------------------------------------------------" )


        Devuelta = input("Desea jugar otra partida? (si o no):  ")


        if Devuelta.lower() == "si":
            main()


    #Funcion para cargar la apuesta hasta q sea valida
    def cargar_apuesta ():
        nonlocal banco
        while True:
            try:
                apuesta = float(input("Elija monto a apostar: $"))
                while apuesta > banco:
                    print(f"No hay fondos suficientes, tenes ${banco} en el banco")
                    apuesta = float(input("Elija monto a apostar: $"))
                banco -= apuesta
                return apuesta
            except:
                print("Entrada inválida. Ingrese un número.")
            else:            return apuesta



            
    #Genera cartas en una lista de tuplas entre la lista de valor y la lista de palos
    def generar_cartas():
        palos = ['corazones', 'treboles', 'diamantes', 'picas']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return [(valor, palo) for palo in palos for valor in valores]

    #mezcla las cartas, las reparte y las saca de la lista con el pop
    def repartir_cartas(cartas, cantidad):
        random.shuffle(cartas)
        return [cartas.pop() for i in range(cantidad)]  

    #mezcla las cartas y saca 3 para la mesa
    def cartas_en_la_mesa(cartas):
        random.shuffle(cartas)
        return [cartas.pop() for i in range(3)]

    #mezcla las cartas, saca 1 y las suma a las otras de la mesa
    def cartas_en_la_mesa_ronda(cartas, cartas_en_mesa):
        random.shuffle(cartas)
        cartas_en_mesa.extend([cartas.pop() for i in range(1)])
        return cartas_en_mesa

    #pone el orden de las cartas y dependiendo de cuantas veces se repite cada valor y/o cada palo se clasifica
    def clasificacion_cartas(cartas_en_mesa, cartas_jugador):
        todas_cartas = cartas_en_mesa + cartas_jugador
        valores = [carta[0] for carta in todas_cartas]
        palos = [carta[1] for carta in todas_cartas]

        orden = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        max_rep = 0
        segunda_rep = 0

        for valor in valores:
            rep = valores.count(valor)
            if rep > max_rep:
                segunda_rep = max_rep
                max_rep = rep
            elif rep > segunda_rep and rep != max_rep:
                segunda_rep = rep

        es_color = False
        for palo in palos:
            if palos.count(palo) >= 5:
                es_color = True

        valores_unicos = []
        for i in valores:
            if i in orden and i not in valores_unicos:
                valores_unicos.append(i)

        valores_unicos.sort(key=lambda x: orden.index(x))

        consecutivos = 1
        es_escalera = False

        for i in range(len(valores_unicos) - 1):
            if orden.index(valores_unicos[i+1]) - orden.index(valores_unicos[i]) == 1:
                consecutivos += 1
                if consecutivos >= 5:
                    es_escalera = True
            else:
                consecutivos = 1
        

        pares = 0
        vistos = []

        for i in valores:
            if i not in vistos:
                if valores.count(i) == 2:
                    pares += 1
                vistos.append(i)


        if max_rep == 4:
            return "Poker"
        elif max_rep == 3 and segunda_rep == 2:
            return "Full House"
        elif es_color:
            return "Color"
        elif es_escalera:
            return "Escalera"
        elif max_rep == 3:
            return "Triple"
        elif pares == 2:
            return "Doble pareja"
        elif pares == 1:
            return "Pareja"
        else:
            return "Carta alta"
        
        
    #Toma la cartas de la mesa y los jugadores para ver cual es la mas alta en caso de empate se usa esta funcion 
    def desempate(cartas_en_mesa, cartas_jugador, cartas_bot,apuesta):
        nonlocal banco
        todas_las_cartas_jugador = cartas_en_mesa + cartas_jugador
        todas_las_cartas_bot = cartas_en_mesa + cartas_bot
        carta_mayor_jugador = max(todas_las_cartas_jugador)
        carta_mayor_bot = max(todas_las_cartas_bot)
        if carta_mayor_jugador > carta_mayor_bot:
            desempate=1
        elif carta_mayor_jugador < carta_mayor_bot:
            desempate=2
        else:
            desempate=0

        if desempate == 1:
            banco += apuesta*2
            return f"            Gana el jugador Fondos restantes en el banco: $ {banco}"
        elif desempate == 2:
            return f"            Gana el bot  Fondos restantes en el banco: $ {banco}"
        else:
            banco += apuesta
            return f"            Empate por la carta mas alta Fondos restantes en el banco: $ {banco}"
        

    #asigna cada simbolo escirto a el simbolo en si
    def simbolo_palo(palo):
        simbolos = {
            "corazones": "♥",
            "diamantes": "♦",
            "treboles": "♣",
            "picas": "♠"
        }
        return simbolos[palo]

    #pone la carta en forma de carta
    def mostrar_carta(carta):

        valor, palo = carta
        simbolo = simbolo_palo(palo)

        return [
            "┌─────┐",
            f"│{valor:<2}   │",
            f"│  {simbolo}  │",
            f"│   {valor:>2}│",
            "└─────┘"
        ]

    #hace q las cartas esten bien mostradas al mismo tiempo y que no esten mezcladas entre si
    def mostrar_cartas(cartas):

        cartas_dibujadas = [mostrar_carta(carta) for carta in cartas]

        for linea in range(5):

            fila = ""

            for carta in cartas_dibujadas:
                fila += carta[linea] + "  "

            print(fila)


    #Ponemos una lista del orden de clasificacion y segun las posiciones de ese orden va a dar si es mayor o menor q las otras
    def ganador(cartas_en_mesa, cartas_jugador, cartas_bot, apuesta):
        nonlocal banco
        clasificacion_jugador = clasificacion_cartas(cartas_en_mesa, cartas_jugador)
        clasificacion_bot = clasificacion_cartas(cartas_en_mesa, cartas_bot)

        orden_clasificaciones = ["Carta alta", "Pareja", "Doble pareja", "Triple", "Escalera", "Color", "Full House", "Poker"]
        if orden_clasificaciones.index(clasificacion_jugador) > orden_clasificaciones.index(clasificacion_bot):
            banco += apuesta*2 
            return f"            Gana el jugador Fondos restantes en el banco: $ {banco}"
        elif orden_clasificaciones.index(clasificacion_jugador) < orden_clasificaciones.index(clasificacion_bot):
            return f"            Gana el bot  Fondos restantes en el banco: $ {banco}"
        else:
            return desempate(cartas_en_mesa, cartas_jugador, cartas_bot,apuesta)


    if arranque == "si":
        main()
    
    return banco
    


if __name__ == "__main__":
    jugar_poker()
