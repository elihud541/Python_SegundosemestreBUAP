import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Carga de datos ---
# Usamos el nombre exacto de tu archivo
df = pd.read_csv('Raw Data.csv')

# Extraer columnas (nombres exactos de tu CSV)
lat = df['Latitude (°)']
lon = df['Longitude (°)']

# --- 2. Conversión a metros (Sistema Cartesiano) ---
# Radio de la Tierra en metros
R = 6371000 
# Convertimos grados a metros usando el primer punto como origen (0,0)
x = R * np.radians(lon - lon.iloc[0]) * np.cos(np.radians(lat.iloc[0]))
y = R * np.radians(lat - lat.iloc[0])

# --- 3. Vectores de Desplazamiento ---
# La función diff calcula la resta entre puntos consecutivos: x[i+1] - x[i]
vx = np.diff(x)
vy = np.diff(y)

# --- 4. Cálculos Vectoriales ---
# Magnitud de cada vector (Distancia por tramo)
magnitudes = np.sqrt(vx**2 + vy**2)

# Ángulo entre tramos consecutivos (Producto Punto)
angulos_giro = []
for i in range(len(vx) - 1):
    A = [vx[i], vy[i]]
    B = [vx[i+1], vy[i+1]]
    
    # cos(theta) = (A·B) / (|A|*|B|)
    dot_product = np.dot(A, B)
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B)
    
    # Evitar errores de precisión con clip
    cos_theta = np.clip(dot_product / (norm_A * norm_B), -1.0, 1.0)
    angulo = np.degrees(np.arccos(cos_theta))
    angulos_giro.append(angulo)

# --- 5. Visualización ---
plt.figure(figsize=(12, 7), facecolor='white')
# Graficamos los vectores con quiver
plt.quiver(x[:-1], y[:-1], vx, vy, angles='xy', scale_units='xy', scale=1, 
           color='teal', label='Vectores de desplazamiento', width=0.005)

# Dibujamos los puntos GPS para referencia
plt.scatter(x, y, color='crimson', s=15, label='Puntos registrados')

plt.title('Reconstrucción de Trayectoria Física (Vectores)', fontsize=14)
plt.xlabel('Eje X (metros)', fontsize=12)
plt.ylabel('Eje Y (metros)', fontsize=12)
plt.axis('equal') # Importante para que 1m en X sea igual a 1m en Y
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# --- Resultados para el reporte ---
print("-" * 30)
print(f"RESUMEN DE LA PRÁCTICA")
print("-" * 30)
print(f"Distancia Total (Suma de magnitudes): {np.sum(magnitudes):.2f} m")
print(f"Desplazamiento Neto (Vector resultante): {np.sqrt(np.sum(vx)**2 + np.sum(vy)**2):.2f} m")
if angulos_giro:
    print(f"Promedio de ángulo en giros: {np.mean(angulos_giro):.2f}°")