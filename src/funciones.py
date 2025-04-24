import re
import random
import string
from datetime import datetime

# Ejercicio 1: Filtrar líneas del Zen de Python
def filtrar_zen(zen_text):
    zen_lines = zen_text.split("\n")
    resultado = []
    for line in zen_lines:
        words = line.split()
        if len(words) > 1 and words[1][0].lower() in "aeiou":
            resultado.append(line)
    return resultado

# Ejercicio 2: Título más largo
def titulo_mas_largo(titles):
    return max(titles, key=lambda titulo: len(titulo.split()))

# Ejercicio 3: Filtrar reglas por palabra clave
def filtrar_reglas(rules, palabra_clave):
    lista_reglas = rules.split("\n")
    return [regla for regla in lista_reglas if palabra_clave in regla.lower()]

# Ejercicio 4: Validar nombre de usuario
def validar_usuario(usuario):
    # Verificar longitud mínima de 5 caracteres
    if len(usuario) < 5:
        return "El nombre de usuario debe tener al menos 5 caracteres."
    
    # Verificar si contiene al menos un número
    if not any(char.isdigit() for char in usuario):
        return "El nombre de usuario debe contener al menos un número."
    
    # Verificar si contiene al menos una letra mayúscula
    if not any(char.isupper() for char in usuario):
        return "El nombre de usuario debe contener al menos una letra mayúscula."
    
    # Verificar si solo contiene letras y números
    # El módulo re en Python se utiliza para trabajar con expresiones regulares.
    if not re.match("^[A-Za-z0-9]+$", usuario):
        return "El nombre de usuario solo puede contener letras y números."
    
    return "El nombre de usuario cumple con los requisitos."


# Ejercicio 5: Clasificar tiempo de reacción
def clasificar_reaccion(tiempo_reaccion):
    if tiempo_reaccion < 200:
        return "Rápido"
    elif 200 <= tiempo_reaccion <= 500:
        return "Normal"
    else:
        return "Lento"

# Ejercicio 6: Contar palabras clave en descripciones
def contar_palabras_clave(descriptions, keywords):
    return {keyword: sum(keyword in description.lower() for description in descriptions) for keyword in keywords}

# Ejercicio 7: Generar código de descuento
def generar_codigo_descuento(usuario):
    if len(usuario) > 15:
        return "El nombre de usuario no debe exceder los 15 caracteres."
    fecha_actual = datetime.now().strftime("%Y%m%d")
    caracteres_aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{usuario.upper()}-{fecha_actual}-{caracteres_aleatorios}"

# Ejercicio 8: Verificar si son anagramas
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejercicio 9: Limpiar lista de clientes
def limpiar_clientes(clientes):
    clientes = [cliente for cliente in clientes if cliente and cliente.strip()]
    clientes = [cliente.strip().title() for cliente in clientes]
    clientes = list(set(clientes))
    clientes.sort()
    return clientes

# Ejercicio 10: Calcular ranking de jugadores
def calcular_ranking(rounds, puntos):
    # Inicializar estadísticas de los jugadores
    estadisticas = {}

    # Procesar cada ronda
    for ronda, datos in enumerate(rounds, start=1):
        print(f"Ranking ronda {ronda}:")

        # Actualizar estadísticas
        for jugador, acciones in datos.items():
            if jugador not in estadisticas:
                estadisticas[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}

            estadisticas[jugador]['kills'] += acciones['kills']
            estadisticas[jugador]['assists'] += acciones['assists']
            estadisticas[jugador]['deaths'] += 1 if acciones['deaths'] else 0
            estadisticas[jugador]['points'] += (
                acciones['kills'] * puntos['kill'] +
                acciones['assists'] * puntos['assist'] +
                (puntos['death'] if acciones['deaths'] else 0)
            )

        # Determinar el MVP de la ronda
        mvp = max(datos.keys(), key=lambda j: (
            datos[j]['kills'] * puntos['kill'] +
            datos[j]['assists'] * puntos['assist'] +
            (puntos['death'] if datos[j]['deaths'] else 0)
        ))
        estadisticas[mvp]['mvps'] += 1

        # Ordenar y mostrar el ranking
        ranking = sorted(estadisticas.items(), key=lambda x: x[1]['points'], reverse=True)
        for jugador, stats in ranking:
            print(f"{jugador}: Kills={stats['kills']}, Asistencias={stats['assists']}, Muertes={stats['deaths']}, MVPs={stats['mvps']}, Puntos={stats['points']}")
        print()

    # Mostrar el ranking final
    print("Ranking final:")
    ranking_final = sorted(estadisticas.items(), key=lambda x: x[1]['points'], reverse=True)
    print("Jugador\tKills\tAsistencias\tMuertes\tMVPs\tPuntos")
    print("--------------------------------------------------------")
    for jugador, stats in ranking_final:
        print(f"{jugador}\t{stats['kills']}\t{stats['assists']}\t{stats['deaths']}\t{stats['mvps']}\t{stats['points']}")
    