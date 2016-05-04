import requests
import RPi.GPIO as GPIO
import time

sensor = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

previous_state = False
current_state = False

last_movement = time.time()
light_on = False
while True:
    time.sleep(0.5)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        print("Current state: ", current_state)
        #Send data to server.
        r = requests.post('http://192.168.1.4:3003/motion', data = {'on' : current_state})