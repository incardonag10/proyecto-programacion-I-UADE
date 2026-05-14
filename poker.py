import random

estado = {"banco": float(input("Ingrese monto a depositar en el banco: $"))}


arranque = input("Desea jugar Snicker´s poker? (si o no): ")

def main():
    apuesta = float(input("Elija monto a apostar: $"))
    while apuesta > estado["banco"]:
        print(f"No hay fondos suficientes, tenes ${estado['banco']} en el banco")
        apuesta = float(input("Elija monto a apostar: $"))
    estado["banco"] -= apuesta


    cartas = generar_cartas()
    cartas_jugador = repartir_cartas(cartas, 2)
    cartas_en_mesa = cartas_en_la_mesa(cartas)
    cartas_bot = repartir_cartas(cartas, 2)

    print("---------------------------------------------------------------------" )
    print(f"            Cartas del jugador: {cartas_jugador}")
    print(f"            Mesa inicial: {cartas_en_mesa}")



    print("---------------------------------------------------------------------" )
    cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)
    print(f"            Mesa ronda 1: {cartas_en_mesa}")



    print("---------------------------------------------------------------------" )
    cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)
    print(f"            Mesa ronda 2: {cartas_en_mesa}")

    print("---------------------------------------------------------------------" )

    print(f"El otro jugador tira sus cartas y tiene:\n\n{cartas_bot}")
    print("---------------------------------------------------------------------" )
    print(f"            Clasificacion rival: {clasificacion_cartas(cartas_en_mesa, cartas_bot)}")
    print("---------------------------------------------------------------------" )
    print(f"            Clasificación tuya: {clasificacion_cartas(cartas_en_mesa, cartas_jugador)}")
    print("---------------------------------------------------------------------" )
    print(ganador(cartas_en_mesa, cartas_jugador, cartas_bot,estado,apuesta))
    print("---------------------------------------------------------------------" )
    print("---------------------------------------------------------------------" )
    Devuelta = input("Desea jugar otra partida? (si o no):  ")

    if Devuelta == "si":
        main()

    elif Devuelta == "no":
        print(f"Desea añadir mas fondos al banco? Actualmente tenes ${estado['banco']} en el banco")
        respuesta_banco = input("Ingrese si o no: ")

        if respuesta_banco == "si":
            ok = False
            while not ok:
                try: 
                    monto = float(input("Ingrese monto a depositar en el banco: $"))
                    if monto > 0:
                        estado["banco"] += monto
                        ok = True
                        main()
                    else:
                        print("El monto debe ser mayor a 0.")
                except:
                    print("Entrada inválida. Ingrese un número.")
        else:
            print("Gracias por jugar Snicker´s poker! Vuelva pronto!")


        
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
    todas_cartas_jugador = cartas_en_mesa + cartas_jugador
    valores = [carta[0] for carta in todas_cartas_jugador]
    palos = [carta[1] for carta in todas_cartas_jugador]
    orden = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    max_rep = 0
    segunda_rep = 0
    for valor in valores:
        rep = valores.count(valor)
        if rep > max_rep:
            segunda_rep = max_rep
            max_rep = rep
        elif rep != max_rep and rep > segunda_rep:
            segunda_rep = rep

    es_color = False
    for palo in palos:
        if palos.count(palo) >= 5:
            es_color = True

    es_escalera = False
    todas_cartas_jugador_ordenadas = []
    for carta in orden:
        if carta in valores:
            todas_cartas_jugador_ordenadas.append(carta)
    consecutivos = 1
    for i in range(len(todas_cartas_jugador_ordenadas) - 1):
        if orden.index(todas_cartas_jugador_ordenadas[i+1]) - orden.index(todas_cartas_jugador_ordenadas[i]) == 1:
            consecutivos += 1
            if consecutivos >= 5:
                es_escalera = True
        else:
            consecutivos = 1
            es_escalera = False

 
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
    elif max_rep == 2 and segunda_rep == 2:
        return "Doble pareja"
    elif max_rep == 2:
        return "Pareja"
    else:
        return "Carta alta"

#Toma la cartas de la mesa y los jugadores para ver cual es la mas alta en caso de empate se usa esta funcion 
def desempate(cartas_en_mesa, cartas_jugador, cartas_bot,estado,apuesta):
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
        estado["banco"] += apuesta*2
        return f"            Gana el jugador Fondos restantes en el banco: $ {estado['banco']}"
    elif desempate == 2:
        return f"            Gana el bot  Fondos restantes en el banco: $ {estado['banco']}"
    else:
        estado["banco"] += apuesta
        return f"            Empate por la carta mas alta Fondos restantes en el banco: $ {estado['banco']}"
    

#Ponemos una lista del orden de clasificacion y segun las posiciones de ese orden va a dar si es mayor o menor q las otras
def ganador(cartas_en_mesa, cartas_jugador, cartas_bot, estado,     apuesta):
    clasificacion_jugador = clasificacion_cartas(cartas_en_mesa, cartas_jugador)
    clasificacion_bot = clasificacion_cartas(cartas_en_mesa, cartas_bot)

    orden_clasificaciones = ["Carta alta", "Pareja", "Doble pareja", "Triple", "Escalera", "Color", "Full House", "Poker"]
    if orden_clasificaciones.index(clasificacion_jugador) > orden_clasificaciones.index(clasificacion_bot):
        estado["banco"] += apuesta*2 
        return f"            Gana el jugador Fondos restantes en el banco: $ {estado['banco']}"
    elif orden_clasificaciones.index(clasificacion_jugador) < orden_clasificaciones.index(clasificacion_bot):
        return f"            Gana el bot  Fondos restantes en el banco: $ {estado['banco']}"
    else:
        return desempate(cartas_en_mesa, cartas_jugador, cartas_bot,estado,apuesta)


if arranque == "si":
    main()