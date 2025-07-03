import time
import board
import digitalio
import pulseio
import pwmio
from adafruit_motor import servo

# === Pines de conexión ===
TRIG_PIN = board.IO26      
ECHO_PIN = board.IO25
SERVO_PIN = board.IO19

# === Configuración del sensor ultrasónico ===
trig = digitalio.DigitalInOut(TRIG_PIN)
trig.direction = digitalio.Direction.OUTPUT

echo = pulseio.PulseIn(ECHO_PIN)
echo.pause()
echo.clear()

# === Configuración del servo motor ===
pwm = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)
mi_servo = servo.Servo(pwm)


# Mapeo lineal de valores
def mapear(x, in_min, in_max, out_min, out_max):
    x = max(min(x, in_min), in_max)  # Limita entre 10 y 5 cm
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Medir distancia en cm
def medir_distancia():
    trig.value = False
    time.sleep(0.002)
    trig.value = True
    time.sleep(0.01)
    trig.value = False

    echo.clear()
    echo.resume()
    time.sleep(0.1)
    echo.pause()

    if len(echo) == 0:
        return None

    duracion_pulso = echo[0]
    distancia_cm = (duracion_pulso / 2) / 29.1
    return round(distancia_cm, 2)

# Loop principal
while True:
    distancia = medir_distancia()
    if distancia:
        print("Distancia:", distancia, "cm")

        if distancia <= 10:
            angulo = mapear(distancia, 10, 5, 0, 90)
            mi_servo.angle = angulo
            print(f"Servo ajustado a {round(angulo)}°")
        else:
            mi_servo.angle = 0
            print("Fuera del rango, servo a 0°")
    else:
        print("Sin señal de eco.")

    time.sleep(0.5)
