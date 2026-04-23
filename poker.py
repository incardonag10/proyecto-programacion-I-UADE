import random

def generar_cartas():
    palos = ['corazones', 'treboles', 'diamantes', 'picas']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [(valor, palo) for palo in palos for valor in valores]

def repartir_cartas(cartas, cantidad):
    random.shuffle(cartas)
    return [cartas.pop() for i in range(cantidad)]  

def cartas_en_la_mesa(cartas):
    random.shuffle(cartas)
    return [cartas.pop() for i in range(3)]

def cartas_en_la_mesa_ronda1(cartas, cartas_en_mesa):
    random.shuffle(cartas)
    cartas_en_mesa.extend([cartas.pop() for i in range(1)])
    return cartas_en_mesa

def cartas_en_la_mesa_ronda2(cartas, cartas_en_mesa):
    random.shuffle(cartas)
    cartas_en_mesa.extend([cartas.pop() for i in range(1)])
    return cartas_en_mesa

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

    vistos = []
    indices = []
    for valor in valores:
        if valor not in vistos:
            vistos.append(valor)
            indices.append(orden.index(valor))
    indices.sort()
    es_escalera = False
    consecutivos = 1
    for i in range(len(indices) - 1):
        if indices[i+1] - indices[i] == 1:
            consecutivos += 1
            if consecutivos >= 5:
                es_escalera = True
        else:
            consecutivos = 1

 
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

def desempate(cartas_en_mesa, cartas_jugador, cartas_bot):
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
        return "            Gana el jugador por la carta mas alta"
    elif desempate == 2:
        return "            Gana el bot por la carta mas alta"
    else:
        return "            Empate por la carta mas alta"
    
def ganador(cartas_en_mesa, cartas_jugador, cartas_bot):
    clasificacion_jugador = clasificacion_cartas(cartas_en_mesa, cartas_jugador)
    clasificacion_bot = clasificacion_cartas(cartas_en_mesa, cartas_bot)

    orden_clasificaciones = ["Carta alta", "Pareja", "Doble pareja", "Triple", "Escalera", "Color", "Full House", "Poker"]
    if orden_clasificaciones.index(clasificacion_jugador) > orden_clasificaciones.index(clasificacion_bot):
        return "            Gana el jugador"
    elif orden_clasificaciones.index(clasificacion_jugador) < orden_clasificaciones.index(clasificacion_bot):
        return "            Gana el bot"
    else:
        return desempate(cartas_en_mesa, cartas_jugador, cartas_bot)



cartas = generar_cartas()
cartas_jugador = repartir_cartas(cartas, 2)
cartas_en_mesa = cartas_en_la_mesa(cartas)
cartas_bot = repartir_cartas(cartas, 2)

print("---------------------------------------------------------------------" )
print(f"            Cartas del jugador: {cartas_jugador}")
print(f"            Mesa inicial: {cartas_en_mesa}")



print("---------------------------------------------------------------------" )
cartas_en_la_mesa_ronda1(cartas, cartas_en_mesa)
print(f"            Mesa ronda 1: {cartas_en_mesa}")



print("---------------------------------------------------------------------" )
cartas_en_la_mesa_ronda2(cartas, cartas_en_mesa)
print(f"            Mesa ronda 2: {cartas_en_mesa}")

print("---------------------------------------------------------------------" )

print(f"El otro jugador tira sus cartas y tiene:\n\n{cartas_bot}")
print("---------------------------------------------------------------------" )
print(f"            Clasificacion rival: {clasificacion_cartas(cartas_en_mesa, cartas_bot)}")
print("---------------------------------------------------------------------" )
print(f"            Clasificación tuya: {clasificacion_cartas(cartas_en_mesa, cartas_jugador)}")
print("---------------------------------------------------------------------" )
print(ganador(cartas_en_mesa, cartas_jugador, cartas_bot))
