import random
cartas_en_mesa =[]
def generar_cartas():
    palos = ['corazones', 'treboles', 'diamantes', 'picas']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [(valor, palo) for palo in palos for valor in valores]

def repartir_cartas(cartas, cantidad):
    random.shuffle(cartas)
    return [cartas.pop() for i in range(cantidad)]

def cartas_en_la_mesa(cartas):
    random.shuffle(cartas)
    cartas_en_la_mesa = [cartas.pop() for i in range(3)]
    return cartas_en_la_mesa

def cartas_en_la_mesa_ronda1(cartas, cartas_en_mesa):
    random.shuffle(cartas)
    cartas_ronda1 = [cartas.pop() for i in range(1)]
    cartas_en_mesa.extend(cartas_ronda1)
    return cartas_en_mesa

def cartas_en_la_mesa_ronda2(cartas, cartas_en_mesa):
    random.shuffle(cartas)
    cartas_ronda2 = [cartas.pop() for i in range(1)]
    cartas_en_mesa.extend(cartas_ronda2)
    return cartas_en_mesa

cartas_en_mesa = cartas_en_la_mesa(generar_cartas())
print(repartir_cartas(generar_cartas(), 2))
print(f"Las cartas en la mesa son: {cartas_en_mesa}")
print(f"Las cartas en la mesa después de la ronda 1 son: {cartas_en_la_mesa_ronda1(generar_cartas(), cartas_en_mesa)}")
print(f"Las cartas en la mesa después de la ronda 2 son: {cartas_en_la_mesa_ronda2(generar_cartas(), cartas_en_mesa)}")
