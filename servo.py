import time
import board
import pwmio
from adafruit_motor import servo

# PWM en el pin donde conectaste el servo
pwm = pwmio.PWMOut(board.IO19, duty_cycle=2 ** 15, frequency=50)
mi_servo = servo.Servo(pwm)

# Mover el servo entre 0 y 90 grados
while True:
    mi_servo.angle = 0
    time.sleep(2)
    mi_servo.angle = 90
    time.sleep(2)
