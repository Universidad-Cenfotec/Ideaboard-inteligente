import time
import board
import digitalio
import pulseio

# Pines (ajusta según cómo conectaste TRIG y ECHO)
TRIG_PIN = board.IO26
ECHO_PIN = board.IO25

# Configura TRIG como salida
trig = digitalio.DigitalInOut(TRIG_PIN)
trig.direction = digitalio.Direction.OUTPUT

# Configura ECHO como entrada con captura de pulsos
echo = pulseio.PulseIn(ECHO_PIN)
echo.pause()
echo.clear()

def medir_distancia():
    # Disparo corto del TRIG
    trig.value = False
    time.sleep(0.002)
    trig.value = True
    time.sleep(0.01)
    trig.value = False

    # Esperar por respuesta
    echo.clear()
    echo.resume()
    time.sleep(0.1)
    echo.pause()

    if len(echo) == 0:
        return None  # No hay eco recibido

    pulse_duration = echo[0]  # En microsegundos
    distancia_cm = (pulse_duration / 2) / 29.1
    return round(distancia_cm, 2)

# Loop principal
while True:
    distancia = medir_distancia()
    if distancia:
        print("Distancia:", distancia, "cm")
    else:
        print("Sensor no detecta nada")
    time.sleep(1)
