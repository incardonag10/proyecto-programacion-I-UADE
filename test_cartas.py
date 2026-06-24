from poker import (generar_cartas)

assert len(generar_cartas()) == 52

from poker import (repartir_cartas)
cartas = generar_cartas()
cartas_jugador = repartir_cartas(cartas, 2)
cartas_en_mesa = repartir_cartas(cartas, 5)
cartas_bot = repartir_cartas(cartas, 2)
todas = cartas_jugador + cartas_bot + cartas_en_mesa

assert len(todas) == len(set(todas))

from poker import generar_cartas, repartir_cartas, cartas_en_la_mesa_ronda
cartas_en_mesa = repartir_cartas(cartas, 3)
cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)

assert len(cartas_en_mesa) == 4

cartas_en_la_mesa_ronda(cartas, cartas_en_mesa)

assert len(cartas_en_mesa) == 5