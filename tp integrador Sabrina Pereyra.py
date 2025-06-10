
import numpy as np
import matplotlib.pyplot as plt
import time

def analizar_circuito_RLC(R, L, C, n=100000):
 """
Analiza un circuito RLC en serie y grafica la magnitud y fase de la impedancia.
También mide el tiempo de ejecución en función del número de puntos de frecuencia.

Parámetros:
R: Resistencia en ohmios
L: Inductancia en henrios
C: Capacitancia en faradios
n: Número de puntos de frecuencia (por defecto 1000)
"""
# Rango de frecuencias (de 10 Hz a 1 MHz)
frecuencia = np.logspace(1, 6, 1000)
omega = 2 * np.pi * frecuencia

# Resistencia en ohmios
R = 100
# Inductancia en henrios (1 mH)
L = 1e-3
# Capacitancia en faradios (1 µF)
C = 1e-6


# Cálculo de impedancias
Z_R = R
Z_L = 1j * omega * L
Z_C = 1 / (1j * omega * C)

# Impedancia total del circuito RLC en serie
Z_total = Z_R + Z_L + Z_C
# Magnitud y fase de la impedancia
magnitud_Z = np.abs(Z_total)
fase_Z = np.angle(Z_total, deg=True)

# Gráficas de magnitud y fase
plt.figure(figsize=(12, 6))

# Magnitud
plt.subplot(2, 1, 1)
plt.plot(frecuencia, magnitud_Z)
plt.xscale('log')
plt.yscale('log')
plt.title('Magnitud de la Impedancia del Circuito RLC en Serie')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|Z| (Ohmios)')
plt.grid(True, which='both', linestyle='--')

# Fase
plt.subplot(2, 1, 2)
plt.plot(frecuencia, fase_Z)
plt.xscale('log')
plt.title('Fase de la Impedancia del Circuito RLC en Serie')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (Grados)')
plt.grid(True, which='both', linestyle='--')

plt.tight_layout()
plt.show()

# Medición del tiempo de ejecución para distintos valores de n
tiempos_ejecucion = []
valores_n = np.logspace(1, 4, 10, dtype=int)

for n in valores_n:
  inicio = time.time()
  frecuencia = np.logspace(1, 6, n)
  omega = 2 * np.pi * frecuencia
  Z_L = 1j * omega * L
  Z_C = 1 / (1j * omega * C)
  Z_total = Z_R + Z_L + Z_C
  magnitud_Z = np.abs(Z_total)
  fase_Z = np.angle(Z_total, deg=True)
  fin = time.time()
  tiempos_ejecucion.append(fin - inicio)

# Gráfica del tiempo de ejecución
plt.figure(figsize=(8, 6))
plt.plot(valores_n, tiempos_ejecucion, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.title('Tiempo de Ejecución vs Número de Puntos de Frecuencia')
plt.xlabel('Número de Puntos de Frecuencia (n)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.grid(True, which='both', linestyle='--')
plt.show()

# Ejemplo de uso de la función
analizar_circuito_RLC(100, 1e-3, 1e-6)
