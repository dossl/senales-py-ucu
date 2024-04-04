import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import spectrogram
import librosa
from google.colab import files
#uploaded = files.upload()

# Función para cargar un archivo MP3 y obtener la transformada de Fourier del audio
def mp3_to_fft(filename):
    # Cargar el archivo MP3 utilizando librosa
    audio, _ = librosa.load(filename, sr=None)

    # Calcular la Transformada de Fourier
    fft_result = fft(audio)

    # Calcular las frecuencias correspondientes
    freqs = np.fft.fftfreq(len(fft_result))

    return freqs, np.abs(fft_result)

# Nombre del archivo MP3 que deseas procesar
mp3_file = '6669.mp3'

# Obtener la transformada de Fourier del audio
freqs, fft_result = mp3_to_fft(mp3_file)

# Multiplicar el vector de frecuencias por la frecuencia de muestreo del audio fs = 44kHz
freqs = (2*44000) * freqs

# Crear un gráfico para mostrar el módulo de la transformada de Fourier
print(fft_result)
print(freqs)
plt.figure(figsize=(12, 6))
plt.title('Módulo de la Transformada de Fourier')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.plot(freqs, fft_result)
plt.grid()
plt.xlim(500, 1000)  # Limitar el rango de frecuencias para una mejor visualización
plt.show()