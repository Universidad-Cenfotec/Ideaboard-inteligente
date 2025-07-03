# code.py

import time
import board
import digitalio
import pwmio
import pulseio
import wifi
import socketpool
import adafruit_requests
from adafruit_motor import servo
from secrets import secrets
import ssl

# Conectarse al WiFi
print("Conectando a WiFi...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("¡Conectado a WiFi!")
print("IP:", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# === Pines ===
TRIG_PIN = board.IO26
ECHO_PIN = board.IO25
SERVO_PIN = board.IO19

trig = digitalio.DigitalInOut(TRIG_PIN)
trig.direction = digitalio.Direction.OUTPUT

echo = pulseio.PulseIn(ECHO_PIN)
echo.pause()
echo.clear()

pwm = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)
mi_servo = servo.Servo(pwm)

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

def mapear(x, in_min, in_max, out_min, out_max):
    x = max(min(x, in_min), in_max)
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
'''
def enviar_formulario(distancia, angulo, servo_activado):
    url = "https://docs.google.com/forms/d/e/1FAIpQLScqqW5OTFZvFr_Ci4goyzgQL463iEQNoDSAa1-Tdopu0_1C6g/viewform?usp=header"
    data = {
        "entry.1234567890": str(distancia),
        "entry.2345678901": str(round(angulo, 2)),
        "entry.3456789012": "Sí" if servo_activado else "No",
        "entry.4567890123": time#.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        response = requests.post(url, data=data)
        print("📤 Enviado:", response.status_code)
        response.close()
    except Exception as e:
        print("❌ Error al enviar:", e)
        '''
def enviar_formulario(distancia, angulo, servo_activado):
    url = "https://docs.google.com/forms/d/e/1FAIpQLScqqW5OTFZvFr_Ci4goyzgQL463iEQNoDSAa1-Tdopu0_1C6g/formResponse"
    data = {
        "entry.1800922120": str(distancia),                 # Distancia
        "entry.369437487": str(round(angulo, 2)),           # Ángulo
        "entry.761152841": "Sí" if servo_activado else "No",# Servo activado
        # El timestamp es opcional; Google agrega uno automáticamente
        # "entry.1720108477": time.strftime("%Y-%m-%d %H:%M:%S") 
    }
    print("Enviando:", data)
    try:
        response = requests.post(url, data=data)
        print("📤 Enviado:", response.status_code)
        response.close()
    except Exception as e:
        print("❌ Error al enviar:", e)

# === Loop ===
while True:
    distancia = medir_distancia()
    if distancia:
        print("📏 Distancia:", distancia, "cm")

        if distancia <= 10:
            angulo = mapear(distancia, 10, 5, 0, 90)
            mi_servo.angle = angulo
            servo_activado = True
        else:
            angulo = 0
            mi_servo.angle = 0
            servo_activado = False

        enviar_formulario(distancia, angulo, servo_activado)
    else:
        print("❌ No se detectó eco.")

    time.sleep(1)
