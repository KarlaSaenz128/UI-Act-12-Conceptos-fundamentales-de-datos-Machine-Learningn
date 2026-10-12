
# Karla Saenz 0133 NL 52 = 22
import pandas as pd
from sklearn.linear_model import LinearRegression # type: ignore

# 1. Crear el dataset correspondiente al caso 22
datos22 = {
    'distancia_km': [5.1, 2.9, 4.0, 1.4, 6.3],
    'trafico_nivel': [3, 2, 1, 3, 2],         # 1: Bajo, 2: Medio, 3: Alto
    'edad_repartidor': [40, 27, 33, 22, 45],
    'tiempo_entrega_min': [48, 24, 28, 14, 58] # Target / Variable a predecir
}

df = pd.DataFrame(datos22)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']]
y = df['tiempo_entrega_min']

# 3. Crear y entrenar el modelo de Regresión Lineal
modelo = LinearRegression()
modelo.fit(X, y)

# 4. Mostrar resultados y métricas básicas
print("--- MODELO ENTRENADO ---")
print(f"Coeficientes (pesos): {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Precisión R^2: {modelo.score(X, y):.4f}")

# 5. Ejemplo de predicción para un nuevo repartidor
# Distancia: 3.5 km, Tráfico: 2 (Medio), Edad: 30 años
nuevo_envio = pd.DataFrame([[3.5, 2, 30]], columns=['distancia_km', 'trafico_nivel', 'edad_repartidor'])
tiempo_predicho = modelo.predict(nuevo_envio)

print(f"\nTiempo estimado de entrega para el nuevo envío: {tiempo_predicho[0]:.2f} minutos")
print("Karla Saenz 0133 NL 52 = 22")