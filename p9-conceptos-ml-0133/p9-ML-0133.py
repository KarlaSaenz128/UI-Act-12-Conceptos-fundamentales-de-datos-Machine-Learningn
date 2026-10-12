# Karla Saenz 0133 NL 52
# ==============================================================================
# ALUMNA: Lista N° 52
# FUENTE / REFERENCIA: https://pythones.net/funciones-en-python-3-tipos-y-sintaxis/
# DESCRIPCIÓN: Ejercicios de Funciones en Python (Tipos, Sintaxis, Parámetros y Retorno)
# ==============================================================================


# ------------------------------------------------------------------------------
# EJEMPLO 1: Función básica sin parámetros ni retorno
# Concepto: Sintaxis básica con 'def' y llamada a función simple.
# ------------------------------------------------------------------------------
def saludar_usuario():
    print("¡Bienvenida a la guía interactiva de funciones en Python!")

print("--- EJEMPLO 1 ---")
saludar_usuario()
print()


# ------------------------------------------------------------------------------
# EJEMPLO 2: Función con parámetros de entrada
# Concepto: Paso de valores mediante argumentos/parámetros.
# ------------------------------------------------------------------------------
def calcular_tiempo_estimado(distancia_km, velocidad_promedio_kmh):
    tiempo_horas = distancia_km / velocidad_promedio_kmh
    tiempo_minutos = tiempo_horas * 60
    print(f"Para {distancia_km} km a {velocidad_promedio_kmh} km/h, el tiempo estimado es: {tiempo_minutos:.1f} minutos.")

print("--- EJEMPLO 2 ---")
calcular_tiempo_estimado(distancia_km=5.1, velocidad_promedio_kmh=20)
print()


# ------------------------------------------------------------------------------
# EJEMPLO 3: Función con retorno de valor (return)
# Concepto: Devolver resultados procesados para guardarlos en variables.
# ------------------------------------------------------------------------------
def evaluar_nivel_trafico(nivel):
    if nivel == 1:
        return "Tráfico Fluido (+0 min de retraso)"
    elif nivel == 2:
        return "Tráfico Moderado (+5 min de retraso)"
    elif nivel == 3:
        return "Tráfico Pesado (+15 min de retraso)"
    else:
        return "Nivel de tráfico no válido"

print("--- EJEMPLO 3 ---")
estado_trafico = evaluar_nivel_trafico(3)
print(f"Estado reportado: {estado_trafico}")
print()


# ------------------------------------------------------------------------------
# EJEMPLO 4: Función con parámetros por defecto (opcionales)
# Concepto: Valores predeterminados si el usuario no ingresa un argumento.
# ------------------------------------------------------------------------------
def registrar_entrega(id_pedido, estado="Pendiente", tarifa_envio=25.0):
    resumen = f"Pedido #{id_pedido} | Estado: {estado} | Tarifa: ${tarifa_envio:.2f}"
    return resumen

print("--- EJEMPLO 4 ---")
# Uso con valores por defecto
print(registrar_entrega(101))
# Sobrescribiendo parámetros opcionales
print(registrar_entrega(102, estado="Entregado", tarifa_envio=35.50))
print()


# ------------------------------------------------------------------------------
# EJEMPLO 5: Funciones anónimas o expresivas (Lambda)
# Concepto: Sintaxis rápida en una sola línea para operaciones sencillas.
# ------------------------------------------------------------------------------
# Función lambda que calcula el recargo por retraso según los minutos transcurridos
calcular_recargo = lambda minutos: minutos * 1.5 if minutos > 30 else 0.0

print("--- EJEMPLO 5 ---")
minutos_demora = 48
recargo = calcular_recargo(minutos_demora)
print(f"Tiempo transcurrido: {minutos_demora} min -> Recargo aplicado: ${recargo:.2f}")
print()
print("Karla Saenz 0133 NL 52")