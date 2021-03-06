import RPi.GPIO as GPIO
# output pins in GPIO
FAN_PIN = 14
EXHAUST_PIN = 15 # RXD
HEAT_PIN = 23
# BLUE_PIN = 23;
VALVE_PIN = 18
LIGHT_PIN = 24

# input pins in GPIO
DHT_PIN = 2
HIGH_WATER_PIN = 16
MEDIUM_WATER_PIN = 20
TRAY_LEVEL_PIN = 21
# RIBBON
# RESERVOIR_SENSOR

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(HEAT_PIN, GPIO.OUT)
GPIO.setup(EXHAUST_PIN, GPIO.OUT)
GPIO.setup(VALVE_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)
GPIO.output(FAN_PIN, False)
GPIO.output(HEAT_PIN, False)
GPIO.output(EXHAUST_PIN, False)
GPIO.output(VALVE_PIN, False)