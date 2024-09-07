import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input("Enter Write text")
    print("hold tag near")
    reader.write(text)
    print("Written")
    print(text)
    
finally:
    GPIO.cleanup()