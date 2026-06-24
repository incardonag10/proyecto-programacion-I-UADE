import random

CATEGORIAS = [
    "Unos", "Doses", "Treses", "Cuatros", "Cincos", "Seises",
    "Escalera", "Full", "Poker", "Generala", "Doble Generala"
]

#  PUNTAJE

def calcular_puntaje(categoria, dados, servida=False):
    conteo = {i: dados.count(i) for i in range(1, 7)}
    valores = sorted(dados)

    if categoria == "Unos":    return conteo[1] * 1
    if categoria == "Doses":   return conteo[2] * 2
    if categoria == "Treses":  return conteo[3] * 3
    if categoria == "Cuatros": return conteo[4] * 4
    if categoria == "Cincos":  return conteo[5] * 5
    if categoria == "Seises":  return conteo[6] * 6

    if categoria == "Escalera":
        if valores in ([1,2,3,4,5], [2,3,4,5,6], [1,3,4,5,6]):
            return 25 if servida else 20
        return 0

    if categoria == "Full":
        if 3 in conteo.values() and 2 in conteo.values():
            return 35 if servida else 30
        return 0

    if categoria == "Poker":
        if any(v >= 4 for v in conteo.values()):
            return 45 if servida else 40
        return 0

    if categoria == "Generala":
        if any(v == 5 for v in conteo.values()):
            return 100 if servida else 50
        return 0

    if categoria == "Doble Generala":
        return 0

    return 0


# ─────────────────────────────────────────────
#  TURNO DEL JUGADOR
# ─────────────────────────────────────────────

def turno_jugador(marcador):
    print("\n" + "="*40)
    print("TU TURNO")
    print("="*40)

    dados = [random.randint(1, 6) for _ in range(5)]
    servida = True

    for num_tirada in range(1, 4):
        print(f"\n  Tirada {num_tirada} de 3:")
        print(f"  Tus dados = {dados}\n")

        # Detectar combinación servida (solo en primera tirada)
        if servida:
            valores_ord = sorted(dados)
            conteo = {i: dados.count(i) for i in range(1, 7)}
            combo = None
            if any(v == 5 for v in conteo.values()):
                combo = "¡GENERALA SERVIDA!"
            elif any(v >= 4 for v in conteo.values()):
                combo = "¡POKER SERVIDO!"
            elif 3 in conteo.values() and 2 in conteo.values():
                combo = "¡FULL SERVIDO!"
            elif valores_ord in ([1,2,3,4,5], [2,3,4,5,6], [1,3,4,5,6]):
                combo = "¡ESCALERA SERVIDA!"

            if combo:
                print(f"{combo}")

                # Ver si la categoría correspondiente ya está anotada
                cat_map = {
                    "¡GENERALA SERVIDA!": "Generala",
                    "¡POKER SERVIDO!": "Poker",
                    "¡FULL SERVIDO!": "Full",
                    "¡ESCALERA SERVIDA!": "Escalera",
                }
                cat_combo = cat_map[combo]
                ya_anotada = marcador.get(cat_combo) is not None

                if combo == "¡GENERALA SERVIDA!" and not ya_anotada:
                    break  # Generala servida no se puede mejorar

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

        # En la ultima tirada no se pregunta si quiere tirar de nuevo
        if num_tirada == 3:
            break

        servida = False

        # Preguntar dado por dado
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

        # Tirar los que no se guardaron
        nuevos = [random.randint(1, 6) for _ in range(5 - len(guardar))]
        dados = guardar + nuevos

        if guardar:
            print(f"\n  Guardados: {guardar}")
        if nuevos:
            print(f"  Nuevos:    {nuevos}")


        # Si guardó todos, no tiene sentido seguir tirando
        if len(guardar) == 5:
            break

    # ─── Elegir categoría ───────────────────────
    print("\n\nCategorías disponibles:\n")
    disponibles = [c for c in CATEGORIAS if marcador[c] is None]
    for i, cat in enumerate(disponibles, 1):
        pts = calcular_puntaje(cat, dados, servida)
        etiqueta = f"  ✅ {pts} pts" if pts > 0 else "  ❌ 0 pts (se tacha)"
        print(f"    {i:2}. {cat:<22}{etiqueta}")

    while True:
        try:
            eleccion = int(input("\n  ¿Qué categoría anotás? (número): ")) - 1
            if 0 <= eleccion < len(disponibles):
                cat_elegida = disponibles[eleccion]
                break
            print("  Número fuera de rango, intentá de nuevo.")
        except ValueError:
            print("  Ingresá un número.")

    pts = calcular_puntaje(cat_elegida, dados, servida)

    if cat_elegida == "Doble Generala":
        if marcador.get("Generala") and any(dados.count(d) == 5 for d in dados):
            pts = 100
        else:
            pts = 0

    marcador[cat_elegida] = pts
    print(f"\nAnotaste {pts} puntos en '{cat_elegida}'\n")
    return marcador


# ─────────────────────────────────────────────
#  TURNO DE LA CPU
# ─────────────────────────────────────────────

def turno_cpu(marcador):
    print("\n" + "="*40)
    print("TURNO CPU")
    print("="*40)

    dados = [random.randint(1, 6) for _ in range(5)]
    servida = True
    print(f"\n  Tirada 1: {dados}")

    for num_tirada in range(2, 4):
        if servida and any(dados.count(d) == 5 for d in dados):
            print("¡GENERALA SERVIDA para la CPU!")
            break

        conteo = {d: dados.count(d) for d in set(dados)}
        mejor_val = max(conteo, key=conteo.get)
        guardar = [d for d in dados if d == mejor_val]

        if len(guardar) >= 4:
            break

        servida = False
        nuevos = [random.randint(1, 6) for _ in range(5 - len(guardar))]
        dados = guardar + nuevos
        print(f"  Tirada {num_tirada}: {dados}")

    disponibles = [c for c in CATEGORIAS if marcador[c] is None]
    mejor_cat = max(disponibles, key=lambda c: calcular_puntaje(c, dados, servida))
    pts = calcular_puntaje(mejor_cat, dados, servida)

    if pts == 0:
        for cat in ["Doble Generala", "Generala", "Poker", "Full", "Escalera",
                    "Seises", "Cincos", "Cuatros", "Treses", "Doses", "Unos"]:
            if marcador[cat] is None:
                mejor_cat = cat
                break

    marcador[mejor_cat] = pts
    print(f"CPU anota {pts} pts en '{mejor_cat}'\n")
    return marcador


# ─────────────────────────────────────────────
#  MARCADOR
# ─────────────────────────────────────────────

def marcador_vacio():
    return {cat: None for cat in CATEGORIAS}


def mostrar_marcador(marc_j, marc_cpu):
    print("\n" + "="*52)
    print(f"  {'CATEGORÍA':<22} {'JUGADOR':>10} {'CPU':>10}")
    print("  " + "-"*48)
    for cat in CATEGORIAS:
        j = str(marc_j[cat]) if marc_j[cat] is not None else "—"
        c = str(marc_cpu[cat]) if marc_cpu[cat] is not None else "—"
        print(f"  {cat:<22} {j:>10} {c:>10}")
    print("  " + "-"*48)
    total_j = sum(v for v in marc_j.values() if v is not None)
    total_c = sum(v for v in marc_cpu.values() if v is not None)
    print(f"  {'TOTAL':<22} {total_j:>10} {total_c:>10}")
    print("=" * 52 + "\n")


# ─────────────────────────────────────────────
#  JUEGO PRINCIPAL
# ─────────────────────────────────────────────

def jugar():
    print("\n" + "★"*40)
    print("BIENVENIDO A LA GENERALA")
    print("★"*40)
    print("""
  Cómo jugar:
  ─────────────────────────────────────────────
  Cada turno tiene hasta 3 tiradas.

  Después de cada tirada, el juego te pregunta dado
  por dado si lo querés guardar (s) o volver a tirar (n).

  Ejemplo:
    Tus dados = [1, 2, 3, 3, 4]
    ¿Cuáles guardás?
      1 = s
      2 = n
      3 = s
      3 = s
      4 = n
    Guardados:  [1, 3, 3]
    Nuevos:     [5, 6]
    Tus dados = [1, 3, 3, 5, 6]

  Al final del turno elegís en qué categoría anotar
  tu combinación. Cada categoría se usa una sola vez.
  Si no tenés la combinación, podés igualmente anotarla
  pero quedará en 0 (tachada).
  ─────────────────────────────────────────────
""")

    marc_j   = marcador_vacio()
    marc_cpu = marcador_vacio()
    rondas   = len(CATEGORIAS)

    for ronda in range(1, rondas + 1):
        print(f"\nRONDA {ronda} de {rondas}")
        mostrar_marcador(marc_j, marc_cpu)

        marc_j   = turno_jugador(marc_j)
        input("  [ENTER para ver el turno de la CPU] ")
        marc_cpu = turno_cpu(marc_cpu)

    print("\n" + "★"*40)
    print("RESULTADO FINAL")
    mostrar_marcador(marc_j, marc_cpu)

    total_j = sum(v for v in marc_j.values() if v is not None)
    total_c = sum(v for v in marc_cpu.values() if v is not None)

    if total_j > total_c:
        print(f"GANASTE! {total_j} vs {total_c}\n")
    elif total_c > total_j:
        print(f"Ganó la CPU: {total_c} vs {total_j}\n")
    else:
        print(f"EMPATE! {total_j} puntos cada uno\n")

    print("★"*40 + "\n")


if __name__ == "__main__":
    jugar()
