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

    if es_escalera and es_color:
        return "Escalera de color"
    elif max_rep == 4:
        return "Poker"
    elif max_rep == 3 and segunda_rep == 2:
        return "Full House"
    elif es_color:
        return "Color"
    elif es_escalera:
        return "Escalera"
    elif max_rep == 3:
        return "Trio"
    elif max_rep == 2 and segunda_rep == 2:
        return "Doble pareja"
    elif max_rep == 2:
        return "Pareja"
    else:
        return "Carta alta"


cartas = generar_cartas()
cartas_jugador = repartir_cartas(cartas, 2)
cartas_en_mesa = cartas_en_la_mesa(cartas)

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
print(f"            Clasificación: {clasificacion_cartas(cartas_en_mesa, cartas_jugador)}")
print("---------------------------------------------------------------------" )