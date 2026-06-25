import random

categorias = [
    "Unos",
    "Doses",
    "Treses",
    "Cuatros",
    "Cincos",
    "Seises",
    "Escalera",
    "Full",
    "Poker",
    "Generala",
    "Doble Generala"
]

def tirar_dados (cantidad = 5): #tirada de dados
    dados = []

    for i in range(cantidad):
        dado = random.randint (1,6)
        dados.append(dado)

    return dados

def reemplazar_dados (guardados, cantidad_nuevos):
    nuevos = tirar_dados (cantidad_nuevos)

    dados_actualizados = guardados + nuevos

    return dados_actualizados

puntaje_numerico = lambda numero, dados: dados.count(numero) * numero

categorias_disponibles = lambda marcador: list(filter(lambda c: marcador[c] is None, categorias))

def sumar_lista_recursiva(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + sumar_lista_recursiva(lista[1:])

def sumar_puntajes(marcador):
    puntajes = []

    for valor in marcador.values():
        if valor is not None:
            puntajes.append(valor)

    return sumar_lista_recursiva(puntajes)

def pedir_categoria (disponibles):
    while True:
        try:
            numero = int(input("Que categoria anotas? Ingresa el numero: "))
            indice = numero - 1

            if indice >= 0 and indice < len(disponibles):
                return disponibles[indice]
            else:
                print ("numero fuera de rango. intenta de nuevo")

        except ValueError:
            print("entrada invalida. proba de nuevo")

def marcador_vacio():
    marcador = {
        "Unos": None,
        "Doses": None,
        "Treses": None,
        "Cuatros": None,
        "Cincos": None,
        "Seises": None,
        "Escalera": None,
        "Full": None,
        "Poker": None,
        "Generala": None,
        "Doble Generala": None
    }

    return marcador

def calcular_puntajes (categoria, dados, servida = False):
    conteo = {}

    for numero in range (1,7):
        conteo[numero] = dados.count(numero)

    valores = sorted(dados)
    max_repetidos = max(conteo.values())

    numericas = {
        "Unos": 1,
        "Doses": 2,
        "Treses": 3,
        "Cuatros": 4,
        "Cincos": 5,
        "Seises": 6
    }

    if categoria in numericas:
        numero = numericas[categoria]
        return puntaje_numerico(numero, dados)
    
    if categoria == "Escalera":
        if valores == [1, 2, 3, 4, 5] or valores == [2, 3, 4, 5, 6] or valores == [1, 3, 4, 5, 6]:
            if servida:
                return 25
            else:
                return 20
        else:
            return 0

    if categoria == "Full":
        if 3 in conteo.values() and 2 in conteo.values():
            if servida:
                return 35
            else:
                return 30
        else:
            return 0

    if categoria == "Poker":
        if max_repetidos >= 4:
            if servida:
                return 45
            else:
                return 40
        else:
            return 0

    if categoria == "Generala":
        if max_repetidos == 5:
            if servida:
                return 100
            else:
                return 50
        else:
            return 0

    if categoria == "Doble Generala":
        return 0

    return 0

def detectar_combo_servido(dados):
    conteo = {}

    for numero in range(1, 7):
        conteo[numero] = dados.count(numero)

    valores_set = set(dados) #set hace conjuntos y no guarda repetidos

    escaleras = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6},
        {1, 3, 4, 5, 6}
    ]

    max_repetidos = max(conteo.values())

    if max_repetidos == 5:
        return "generala servida"

    if max_repetidos >= 4:
        return "poker servido"

    if 3 in conteo.values() and 2 in conteo.values():
        return "full servido"

    if valores_set in escaleras:
        return "escalera servida"

    return None

def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta == "si" or respuesta == "no":
            return respuesta
        else:
            print("Error: tenes que responder si o no.")

def turno_jugador(marcador):
    print("tu turno")

    dados = tirar_dados()
    servida = True

    for num_tirada in range(1, 4):
        print(f"tu tirada {num_tirada} de 3")
        print(f"tus dados son: {dados}")

        if num_tirada == 3:
            break

        servida = False

        while True:
            guardar = []

            print("que dados queres guardar?")

            for dado in dados:
                respuesta = pedir_si_no(f"{dado} = si/no: ")

                if respuesta == "si":
                    guardar.append(dado)

            print(f"dados guardados: {guardar}")

            confirmar = pedir_si_no("estas seguro? (si/no): ")

            if confirmar == "si":
                break

        cantidad_nuevos = 5 - len(guardar)
        nuevos = tirar_dados(cantidad_nuevos)
        dados = guardar + nuevos

        print(f"dados guardados: {guardar}")
        print(f"dados nuevos: {nuevos}")
        print(f"dados finales: {dados}")

        if len(guardar) == 5:
            break
    
    print ("categorias disponibles: ")

    disponibles = categorias_disponibles(marcador)

    for i in range (len(disponibles)):
        categoria = disponibles[i]
        puntaje = calcular_puntajes (categoria, dados, servida)

        print (f"{i+1}. {categoria} - {puntaje} puntos")

    categoria_elegida = pedir_categoria(disponibles)
    puntaje = calcular_puntajes (categoria_elegida, dados, servida)

    if categoria_elegida == "doble generala":
        conteo = {}

        for numero in range(1, 7):
            conteo[numero] = dados.count(numero)

        max_repetidos = max(conteo.values())

        if marcador["Generala"] is not None and max_repetidos == 5:
            puntaje = 100
        else:
            puntaje = 0

    marcador[categoria_elegida] = puntaje

    print(f"\nAnotaste {puntaje} puntos en {categoria_elegida}.")

    return marcador

def turno_cpu(marcador):
    print ("turno cpu")

    dados = tirar_dados()
    servida = True

    for num_tirada in range(1, 4):
        print(f"Tirada {num_tirada}: {dados}")

        if servida:
            combo = detectar_combo_servido(dados)

            if combo is not None:
                print(f"{combo} para la CPU")

                categorias_combo = {
                    "generala servida": "Generala",
                    "poker servido": "Poker",
                    "full servido": "Full",
                    "escalera servida": "Escalera"
                }

                categoria_combo = categorias_combo[combo]

                if marcador[categoria_combo] is None:
                    break

        if num_tirada == 3:
            break

        servida = False

        conteo = {}

        for numero in range(1, 7):
            conteo[numero] = dados.count(numero)

        mejor_numero = 1
        mayor_cantidad = conteo[1]

        for numero in range(2, 7):
            if conteo[numero] > mayor_cantidad:
                mayor_cantidad = conteo[numero]
                mejor_numero = numero

        guardar = []

        for dado in dados:
            if dado == mejor_numero:
                guardar.append(dado)

        if len(guardar) >= 4:
            break

        cantidad_nuevos = 5 - len(guardar)
        dados = reemplazar_dados(guardar, cantidad_nuevos)

    disponibles = categorias_disponibles(marcador)

    mejor_categoria = disponibles[0]
    mejor_puntaje = calcular_puntajes(mejor_categoria, dados, servida)

    for categoria in disponibles:
        puntaje = calcular_puntajes(categoria, dados, servida)

        if categoria == "Doble Generala":
            conteo = {}

            for numero in range(1, 7):
                conteo[numero] = dados.count(numero)

            max_repetidos = max(conteo.values())

            if marcador["Generala"] is not None and max_repetidos == 5:
                puntaje = 100
            else:
                puntaje = 0

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_categoria = categoria

    if mejor_puntaje == 0:
        prioridades = [
            "Doble Generala",
            "Generala",
            "Poker",
            "Full",
            "Escalera",
            "Seises",
            "Cincos",
            "Cuatros",
            "Treses",
            "Doses",
            "Unos"
        ]

        for categoria in prioridades:
            if marcador[categoria] is None:
                mejor_categoria = categoria
                mejor_puntaje = 0
                break

    marcador[mejor_categoria] = mejor_puntaje

    print(f"CPU anota {mejor_puntaje} puntos en {mejor_categoria}")

    return marcador

def mostrar_marcador(marcador_jugador, marcador_cpu):
    print(f"{'CATEGORIA':<22} {'JUGADOR':>10} {'CPU':>10}")

    for categoria in categorias:
        puntaje_jugador = marcador_jugador[categoria]
        puntaje_cpu = marcador_cpu[categoria]

        if puntaje_jugador is None:
            puntaje_jugador = "-"
        else:
            puntaje_jugador = str(puntaje_jugador)

        if puntaje_cpu is None:
            puntaje_cpu = "-"
        else:
            puntaje_cpu = str(puntaje_cpu)

        print(f"{categoria:<22} {puntaje_jugador:>10} {puntaje_cpu:>10}")


    total_jugador = sumar_puntajes(marcador_jugador)
    total_cpu = sumar_puntajes(marcador_cpu)

    print(f"{'TOTAL':<22} {total_jugador:>10} {total_cpu:>10}")

def pedir_numero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: el numero tiene que ser mayor a 0.")

        except ValueError:
            print("Error: tenes que ingresar un numero.")


def pedir_apuesta(saldo):
    while True:
        apuesta = pedir_numero_positivo("Cuanto queres apostar?: ")

        if apuesta <= saldo:
            return apuesta
        else:
            print(f"No podes apostar mas de tu saldo. Tu saldo actual es {saldo}.")


def crear_usuario():
    print("CREAR NUEVO USUARIO")

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    saldo = pedir_numero_positivo("Ingrese saldo inicial: ")

    return nombre, apellido, saldo


def jugargenerala(nombre, apellido, saldo):
    print()
    print("====================================================")
    print("                    GENERALA                        ")
    print("====================================================")
    print()
    print(f"BIENVENIDO A LA GENERALA, {nombre} {apellido}")
    print(f"Tu saldo actual es: {saldo}")
    print()

    respuesta = input("Presione ENTER para jugar o 0 para volver al menu: ")

    if respuesta == "0":
        return int(saldo)

    apuesta = pedir_apuesta(saldo)

    print(f"Apostaste: {apuesta}")

    print("""
Cómo jugar:
---------------------------------------------
Cada turno tiene hasta 3 tiradas.

Después de cada tirada el juego te pregunta dado
por dado si lo querés guardar. Respondé si o no.

Ejemplo:
  Tus dados = [1, 2, 3, 3, 4]
  ¿Cuáles guardás?
    1 = si / no: si
    2 = si / no: no
    3 = si / no: si
    3 = si / no: si
    4 = si / no: no
  Guardados: [1, 3, 3]
  Nuevos:    [5, 6]

Al final del turno elegís en qué categoría anotar
tu combinación. Cada categoría se usa una sola vez.
Si no tenés la combinación quedará en 0.
---------------------------------------------
""")

    marcador_jugador = marcador_vacio()
    marcador_cpu = marcador_vacio()

    rondas = len(categorias)

    for ronda in range(1, rondas + 1):
        print(f"\nRONDA {ronda} de {rondas}")

        mostrar_marcador(marcador_jugador, marcador_cpu)

        marcador_jugador = turno_jugador(marcador_jugador)

        input("Enter para turno de la CPU")

        marcador_cpu = turno_cpu(marcador_cpu)

    print("RESULTADO FINAL")

    mostrar_marcador(marcador_jugador, marcador_cpu)

    total_jugador = sumar_puntajes(marcador_jugador)
    total_cpu = sumar_puntajes(marcador_cpu)

    if total_jugador > total_cpu:
        print(f"Ganaste: {total_jugador} vs {total_cpu}")
        saldo = saldo + apuesta
        print(f"Ganaste {apuesta}. Tu nuevo saldo es {saldo}.")

    elif total_cpu > total_jugador:
        print(f"Gano la CPU: {total_cpu} vs {total_jugador}")
        saldo = saldo - apuesta
        print(f"Perdiste {apuesta}. Tu nuevo saldo es {saldo}.")

    else:
        print(f"Empate: {total_jugador} puntos cada uno")
        print(f"No ganaste ni perdiste saldo. Tu saldo sigue siendo {saldo}.")

    
    while True:

        respuesta = input("\n¿Que desea hacer?\n1. Jugar otra partida\n0. Volver al menu\nOpcion: ")

        if respuesta == "1":
            return jugargenerala(nombre, apellido, saldo)

        elif respuesta == "0":
            return int(saldo)

        else:
            print("Opcion invalida")

if __name__ == "__main__":
    nombre, apellido, saldo = crear_usuario()
    jugargenerala(nombre, apellido, saldo)
