# ESP32 Inteligente: Detecta, decide y actúa 🤖📏

Este proyecto fue desarrollado para el taller presentado en **Maker Faire** y demuestra cómo un microcontrolador puede tomar decisiones en tiempo real usando sensores y actuadores. Utiliza una placa **IdeaBoard de CRCibernetica con ESP32-WROOM-32E**, programada en **CircuitPython**, para detectar distancia, decidir un ángulo proporcional y accionar un servo motor, además de registrar los eventos automáticamente en Google Forms.

---

## 🎯 ¿Qué hace este sistema?

- 🧠 **Detecta** objetos mediante un sensor ultrasónico **HC-SR04**.
- ⚖️ **Decide** el ángulo de apertura de un **servo SG90**, proporcional a la distancia:
  - A 10 cm: 0° (cerrado)
  - A 2 cm: 90° (totalmente abierto)
- 🔧 **Actúa** moviendo el servo.
- 📝 **Registra automáticamente**:
  - Distancia (cm)
  - Ángulo de apertura (°)
  - Estado del servo (Sí/No)
  - Hora local del evento
- 🌐 Los datos se envían a un **Google Form** desde una laptop conectada vía USB.

---

## 📁 Estructura del proyecto

```
esp32-inteligente-detecta-decide-actua/
│
├── code/
│   ├── main.py                      # Script para enviar datos al Google Form (PC)
│   ├── sensor_ultrasonico.py       # Función de medición del HC-SR04 (ESP32)
│   ├── validador_sensor.py         # Validación independiente del sensor
│   ├── validador_servo.py          # Validación independiente del servo
│   ├── sensor_y_servo_integrado.py # Control proporcional sensor + servo
│   └── secrets.py                  # Configuración general (WiFi, etc.)
│
├── assets/
│   └── diagrama_conexion.png       # (Opcional) Diagrama visual de conexiones
│
├── README.md
├── LICENSE
└── requirements.txt                # Requisitos para el script de laptop
```

---

## 🧪 Hardware requerido

- IdeaBoard CRCibernetica con ESP32
- Sensor ultrasónico **HC-SR04**
- Servo motor **SG90**
- 2 resistencias (ej. 1 kΩ + 1 kΩ para divisor de voltaje en el pin ECHO)
- Cables Dupont
- Laptop con Python 3
- Cable USB + alimentación de 5 V estable

---

## 💻 Software necesario

### En la ESP32
- CircuitPython
- Librerías:
  - `digitalio`
  - `pulseio`
  - `pwmio`
  - `adafruit_motor`

### En la laptop (para el envío al formulario)
- Python 3
- `requests`, `pyserial`

Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## 🔬 Archivos clave

| Archivo                         | Descripción                                                    |
|--------------------------------|----------------------------------------------------------------|
| `validador_sensor.py`          | Prueba el sensor ultrasónico de forma aislada                  |
| `validador_servo.py`           | Prueba el servo moviéndolo de 0° a 90° y viceversa             |
| `sensor_y_servo_integrado.py`  | Mide distancia y mueve el servo proporcionalmente              |
| `main.py`                      | Lee datos del ESP32 y los envía a un Google Form               |
| `secrets.py`                   | Contiene claves y configuraciones generales                    |

---

## 📊 Aplicaciones posibles

- 🚪 Puertas o compuertas automáticas sin contacto
- 📦 Activación de vitrinas inteligentes
- 🧪 Estaciones educativas para enseñanza de IoT y electrónica
- 🧠 Edge computing para detección y respuesta sin conexión constante
- 📈 Recolección y análisis de datos físicos en tiempo real

---

## 🧠 Inteligencia embebida

Este sistema aplica **lógica proporcional embebida** en el dispositivo, sin necesidad de conectarse a servidores para funcionar, simulando principios básicos de automatización e inteligencia artificial en el borde (**Edge AI**).

---

## 📤 Créditos

Proyecto desarrollado por **Jorge Luis Ortega Badilla**  
Con el apoyo de **MakerLab - Universidad CENFOTEC**  
Para el evento **Maker Faire Costa Rica 2025**

---

## 📄 Licencia

MIT License – Libre para uso educativo y personal.