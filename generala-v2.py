import random
from functools import reduce

CATEGORIAS = [
    "Unos", "Doses", "Treses", "Cuatros", "Cincos", "Seises",
    "Escalera", "Full", "Poker", "Generala", "Doble Generala"
]

def tirar_dados(cantidad=5):
    """genera una lista de dados al azar usando comprensión de listas"""
    return [random.randint(1, 6) for i in range(cantidad)]

def reemplazar_dados(guardados, cantidad_nuevos):
    """devuelve los guardados + dados nuevos tirados"""
    nuevos = tirar_dados(cantidad_nuevos)
    return guardados + nuevos

puntaje_numerico = lambda numero, dados: dados.count(numero) * numero

categorias_disponibles = lambda marcador: list(filter(lambda c: marcador[c] is None, CATEGORIAS))

def sumar_puntajes(marcador):
    """Usa reduce para sumar todos los puntajes anotados."""
    puntajes = []

    for v in marcador.values():
        if v is not None:
            puntajes.append(v)

    if not puntajes:
        return 0
    
    return reduce(lambda acum, x: acum + x, puntajes)

def pedir_categoria(disponibles):
    """Pide al usuario que elija una categoría. Maneja entradas inválidas."""
    while True:
        try:
            eleccion = int(input("\n  ¿Qué categoría anotás? (número): ")) - 1
            if 0 <= eleccion < len(disponibles):
                return disponibles[eleccion]
            raise ValueError("Número fuera de rango.")
        except ValueError as e:
            print(f"  Entrada inválida: {e} Intentá de nuevo.")

def marcador_vacio():
    """Crea el marcador inicial como diccionario con todas las categorías en None."""
    marcador = {}

    for cat in CATEGORIAS:
        marcador[cat] = None

    return marcador

def calcular_puntaje(categoria, dados, servida=False):
    """Calcula el puntaje según la categoría elegida."""
    
    conteo = {i: dados.count(i) for i in range(1, 7)}
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
        return puntaje_numerico(numericas[categoria], dados)

    if categoria == "Escalera":
        if valores in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6]):
            return 25 if servida else 20
        return 0

    if categoria == "Full":
        if 3 in conteo.values() and 2 in conteo.values():
            return 35 if servida else 30
        return 0

    if categoria == "Poker":
        if max_repetidos >= 4:
            return 45 if servida else 40
        return 0

    if categoria == "Generala":
        if max_repetidos == 5:
            return 100 if servida else 50
        return 0

    if categoria == "Doble Generala":
        return 0

    return 0

def detectar_combo_servido(dados):
    """
    Usa conjuntos para detectar si los dados forman una combinación
    especial en la primera tirada.
    """
    conteo = {i: dados.count(i) for i in range(1, 7)}
    valores_set = set(dados)                         
    escaleras = [{1,2,3,4,5}, {2,3,4,5,6}, {1,3,4,5,6}]  

    if any(v == 5 for v in conteo.values()):
        return "¡GENERALA SERVIDA!"
    if any(v >= 4 for v in conteo.values()):
        return "¡POKER SERVIDO!"
    if 3 in conteo.values() and 2 in conteo.values():
        return "¡FULL SERVIDO!"
    if valores_set in escaleras:                          
        return "¡ESCALERA SERVIDA!"
    return None

# ---------------------------------------------
#  TURNO DEL JUGADOR
# ---------------------------------------------

def turno_jugador(marcador):
    print("\n" + "="*40)
    print("            TU TURNO  ")
    print("="*40)

    dados = tirar_dados() 
    servida = True

    for num_tirada in range(1, 4):
        print(f"\n  Tirada {num_tirada} de 3:")
        print(f"  Tus dados = {dados}\n")

        if servida:
            combo = detectar_combo_servido(dados)

            if combo:
                print(f"   {combo}")

                cat_map = {                               
                    "¡GENERALA SERVIDA!": "Generala",
                    "¡POKER SERVIDO!":    "Poker",
                    "¡FULL SERVIDO!":     "Full",
                    "¡ESCALERA SERVIDA!": "Escalera",
                }
                cat_combo  = cat_map[combo]
                ya_anotada = marcador.get(cat_combo) is not None

                if combo == "¡GENERALA SERVIDA!" and not ya_anotada:
                    break

                if ya_anotada:
                    print(f"  (Ya tenés '{cat_combo}' anotado, seguís tirando.)")
                else:
                    while True:
                        resp = input("  ¿Querés anotar ya o seguir tirando? (anotar/seguir): ").strip().lower()
                        if resp in ("anotar", "seguir"):
                            break
                        print("  Respondé 'anotar' o 'seguir'.")
                    if resp == "anotar":
                        break

        if num_tirada == 3:
            break

        servida = False

        # Pedir dados a guardar con confirmación (TP5: manejo de excepciones en pedir_categoria)
        while True:
            print("  ¿Cuáles guardás?\n")
            guardar = []
            for d in dados:
                while True:
                    resp = input(f"    {d} = si / no: ").strip().lower()
                    if resp in ("si", "no"):
                        if resp == "si":
                            guardar.append(d)
                        break
                    print("      Respondé 'si' o 'no'.")

            print(f"\n  Guardás: {guardar if guardar else '(ninguno)'}")
            while True:
                confirmar = input("  ¿Estás seguro? (si/no): ").strip().lower()
                if confirmar in ("si", "no"):
                    break
                print("  Respondé 'si' o 'no'.")
            if confirmar == "si":
                break
            print()

        dados = reemplazar_dados(guardar, 5 - len(guardar))
        nuevos = dados[len(guardar):]

        if guardar:
            print(f"\n  Guardados: {guardar}")
        if nuevos:
            print(f"  Nuevos:    {list(nuevos)}")

        if len(guardar) == 5:
            break

    # Mostrar categorías usando filter (TP4)
    print("Categorías disponibles:")
    disponibles = categorias_disponibles(marcador)
    for i, cat in enumerate(disponibles, 1):
        pts = calcular_puntaje(cat, dados, servida)
        etiqueta = f"  [OK] {pts} pts" if pts > 0 else "  [--] 0 pts (se tacha)"
        print(f"    {i:2}. {cat:<22}{etiqueta}")

    cat_elegida = pedir_categoria(disponibles)
    pts = calcular_puntaje(cat_elegida, dados, servida)

    if cat_elegida == "Doble Generala":
        if marcador.get("Generala") and any(dados.count(d) == 5 for d in dados):
            pts = 100
        else:
            pts = 0

    marcador[cat_elegida] = pts
    print(f"\n  OK Anotaste {pts} puntos en '{cat_elegida}'\n")
    return marcador


# ---------------------------------------------
#  TURNO DE LA CPU
# ---------------------------------------------

def turno_cpu(marcador):
    print("==============================")
    print("            TURNO CPU  ")
    print("==============================")

    dados = tirar_dados()   # TP2
    servida = True
    print(f"Tirada 1: {dados}")

    for num_tirada in range(2, 4):
        if servida and detectar_combo_servido(dados):   
            print(f"{detectar_combo_servido(dados)} para la CPU!")
            break

        conteo = {d: dados.count(d) for d in set(dados)}  
        mejor_val = max(conteo, key=conteo.get)
        guardar = [d for d in dados if d == mejor_val]

        if len(guardar) >= 4:
            break

        servida = False
        dados = reemplazar_dados(guardar, 5 - len(guardar)) 
        print(f"  Tirada {num_tirada}: {dados}")

    disponibles = categorias_disponibles(marcador)
    puntajes = list(map(lambda c: (c, calcular_puntaje(c, dados, servida)), disponibles)) 
    mejor_cat, pts = max(puntajes, key=lambda x: x[1])

    if pts == 0:
        for cat in ["Doble Generala", "Generala", "Poker", "Full", "Escalera",
                    "Seises", "Cincos", "Cuatros", "Treses", "Doses", "Unos"]:
            if marcador[cat] is None:
                mejor_cat = cat
                break

    marcador[mejor_cat] = pts
    print(f"   CPU anota {pts} pts en '{mejor_cat}'\n")
    return marcador

def mostrar_marcador(marc_j, marc_cpu):
    print("==============================")
    print(f"  {'CATEGORÍA':<22} {'JUGADOR':>10} {'CPU':>10}")
    print("==============================")
    for cat in CATEGORIAS:
        j = str(marc_j[cat]) if marc_j[cat] is not None else "—"
        c = str(marc_cpu[cat]) if marc_cpu[cat] is not None else "—"
        print(f"  {cat:<22} {j:>10} {c:>10}")
    print("==============================")
    # TP4: reduce para sumar puntajes
    total_j = sumar_puntajes(marc_j)
    total_c = sumar_puntajes(marc_cpu)
    print(f"  {'TOTAL':<22} {total_j:>10} {total_c:>10}")
    print("==============================")


# ---------------------------------------------
#  JUEGO PRINCIPAL
# ---------------------------------------------

def jugar():
    print("==============================")
    print("BIENVENIDO A LA GENERALA")
    print("==============================")
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
  Si no tenés la combinación quedará en 0 (tachada).
  ---------------------------------------------
""")

    marc_j   = marcador_vacio()  
    marc_cpu = marcador_vacio()
    rondas   = len(CATEGORIAS)

    for ronda in range(1, rondas + 1):
        print(f"{'>>>'}  RONDA {ronda} de {rondas}  {'<<<'}")
        mostrar_marcador(marc_j, marc_cpu)

        marc_j   = turno_jugador(marc_j)
        input("  [ENTER para ver el turno de la CPU] ")
        marc_cpu = turno_cpu(marc_cpu)

    print("==============================")
    print("RESULTADO FINAL")
    mostrar_marcador(marc_j, marc_cpu)

    total_j = sumar_puntajes(marc_j)
    total_c = sumar_puntajes(marc_cpu)

    if total_j > total_c:
        print(f"¡GANASTE! {total_j} vs {total_c}")
    elif total_c > total_j:
        print(f"   Ganó la CPU: {total_c} vs {total_j}")
    else:
        print(f"¡EMPATE! {total_j} puntos cada uno")

    print("==============================")

if __name__ == "__main__":
    jugar()