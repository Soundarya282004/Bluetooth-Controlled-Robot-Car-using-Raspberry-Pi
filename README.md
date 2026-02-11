# Bluetooth-Controlled-Robot-Car-using-Raspberry-Pi
This project controls a robot car wirelessly using Bluetooth communication. A Raspberry Pi receives movement commands through a Bluetooth serial terminal and controls the motors accordingly.

🔌 Hardware Required

Raspberry Pi

Bluetooth Module (HC-05 / HC-06) or USB Bluetooth adapter

Motor Driver Module (L298N / L293D)

2 DC Motors + Wheels

Robot chassis

Battery pack

Jumper wires

🔧 GPIO Pin Configuration
Component	GPIO Pin
Left Motor IN1	GPIO 2
Left Motor IN2	GPIO 3
Right Motor IN1	GPIO 17
Right Motor IN2	GPIO 4
💻 Software Requirements

Install required libraries:

pip install pyserial
pip install RPi.GPIO

▶ How to Run the Code
1️⃣ Connect Bluetooth Module

Pair the Bluetooth module with your Raspberry Pi

Note the serial port (usually /dev/ttyUSB0 or /dev/rfcomm0)

Update this line if needed:

port='/dev/ttyUSB0'

2️⃣ Save the File

Save as:

Main.py

3️⃣ Run the Program
python3 Main.py

4️⃣ Send Commands via Bluetooth

Use any Bluetooth terminal app (Android or PC):

Command	Action
f	Move Forward
b	Move Backward
l	Turn Left
r	Turn Right
s	Stop

The rules are also sent to the Bluetooth terminal automatically.

⚙️ How the Code Works
🔹 Bluetooth Communication
ser = serial.Serial('/dev/ttyUSB0', 9600)


Receives control commands via Bluetooth serial communication.

🔹 Motor Control Functions

Each function controls GPIO pins connected to the motor driver.

Example:

def forward():


Moves both motors forward.

🔹 Safety Stop

Before changing direction, motors stop first to prevent damage:

stop()

🔁 Continuous Command Monitoring

The loop continuously checks for incoming Bluetooth commands and executes motor actions.

🛑 Stop the Program

Press:

CTRL + C


GPIO pins are safely reset using:

GPIO.cleanup()
