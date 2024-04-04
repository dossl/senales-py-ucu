import numpy as np
import matplotlib.pyplot as plt

# Definimos la función periódica de ejemplo (puedes cambiar esta función)
#def ejemplo_funcion_periodica(t):
#    return np.sin(2 * np.pi * t)# + 0.5 * np.sin(4 * np.pi * t)

def funcion_cuadrada(t, periodo=1.0):
    half_period = periodo / 2
    return np.where((t % periodo) < half_period, 1.0, -1.0)

# Parámetros
T = 1.0  # Periodo de la función
k = 400    # Número de términos a sumar

# Crear un arreglo de tiempo
t = np.linspace(0.0, 2*T, 1000)  # 1000 puntos en un periodo

# Inicializar la suma de Fourier como números complejos
fourier_sum = np.zeros_like(t, dtype=complex)

# Calcular la suma de los primeros k términos de la serie de Fourier
for n in range(1, k + 1):
    cn = 1 / T * np.trapz(funcion_cuadrada(t) * np.exp(-1j * 2 * np.pi * n * t / T), t)
    fourier_sum += cn * np.exp(1j * 2 * np.pi * n * t / T)

# Modificar esta línea para obtener la parte real de fourier_sum
fourier_sum_real = fourier_sum.real

# Graficar la parte real de la suma de Fourier
plt.figure(figsize=(10, 5))
plt.plot(t, fourier_sum.real)
plt.title(f'Suma de los primeros {k} términos de la serie de Fourier (Parte Real)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
