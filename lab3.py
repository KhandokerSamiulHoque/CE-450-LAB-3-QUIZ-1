import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RED_GPIO_PIN = 20
GREEN_GPIO_PIN = 16
BLUE_GPIO_PIN = 21
GPIO.setup(RED_GPIO_PIN, GPIO.OUT)
GPIO.setup(GREEN_GPIO_PIN, GPIO.OUT)
GPIO.setup(BLUE_GPIO_PIN, GPIO.OUT)

MORSE_CODE_SEQ = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '--..',
    'Z': '-.--',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}
DOT_INTERVAL = 0.3  
DASH_INTERVAL = 2 * DOT_INTERVAL
CHAR_INTERVAL = 2 * DASH_INTERVAL

def blink(led_pin, interval):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(DOT_INTERVAL)

def send_message(message):
    for char in message:
        char = char.upper()
        if char == ' ':
            time.sleep(CHAR_INTERVAL)  
        else:
            code = MORSE_CODE_SEQ[char]
            for symbol in code:
                if symbol == '.':
                    blink(RED_GPIO_PIN, DOT_INTERVAL)
                elif symbol == '-':
                    blink(BLUE_GPIO_PIN, DASH_INTERVAL)
            sleep_length = CHAR_INTERVAL - (len(code) * DOT_INTERVAL)
            if sleep_length > 0:
                time.sleep(sleep_length)  

try:
    while True:
        send_message("TEST123")
        time.sleep(CHAR_INTERVAL)  

except KeyboardInterrupt:
    GPIO.cleanup()
