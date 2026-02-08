# serial bluetooth Terminal
import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Initialize serial communication
ser = serial.Serial(
    port = '/dev/ttyUSB0', 
    baudrate=9600,
    timeout=1
)
# initializing motors
IPL1 = 2
IPL2 = 3
IPR1 = 17
IPR2 = 4

GPIO.setup(IPL1, GPIO.OUT)
GPIO.setup(IPL2, GPIO.OUT) 
GPIO.setup(IPR1, GPIO.OUT)
GPIO.setup(IPR2, GPIO.OUT)

def forward():
    GPIO.output(IPL1, True) # you can also use GPIO.HIGH
    GPIO.output(IPL2, False) # you can also use GPIO.LOW
    GPIO.output(IPR1, True)
    GPIO.output(IPR2, False)

def backward():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, True)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, True)

def stop():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, False)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, False)

def Left():
    GPIO.output(IPL1, False)
    GPIO.output(IPL2, True)
    GPIO.output(IPR1, True)
    GPIO.output(IPR2, False)

def Right():
    GPIO.output(IPL1, True)
    GPIO.output(IPL2, False)
    GPIO.output(IPR1, False)
    GPIO.output(IPR2, True)

try:
    while True:
        ser.write(str.encode("Rules:\n f: Move forward\n b: Move backward\n l: Move left\n r: Move right\n s: stop\n"))
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            print(line)
            if line == "f":
                stop() # before changing direction, stop the motors so that motors don't burn out
                forward()
            elif line == "b":
                stop()
                backward()
            elif line == "l":
                stop()
                Left()
            elif line == "r":
                stop()
                Right() 
            elif line == "s":
                stop()
            else:
                stop()
        time.sleep(1)

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()