# Voice-Control-Smart-Room

This project allows you to control your room appliances, like a fan or light, using your voice. It uses Python to detect your voice commands and sends them to an Arduino UNO. The Arduino then rotates a servo motor to physically switch the light or fan on and off.

This is useful if you want to build a smart home setup without using expensive smart switches or devices.

---

## How It Works

1. You speak a command like “Turn on the light”.
2. Python listens using your computer’s microphone and converts the speech to text.
3. If the command matches "turn on" or "turn off", Python sends a signal (`1` or `0`) to the Arduino via USB.
4. Arduino receives the signal and rotates a servo motor to press or toggle a switch.

---

## Components Required

- Arduino UNO
- Servo Motor (SG90 or similar)
- Jumper Wires
- USB Cable to connect Arduino
- Computer with microphone
- Arduino IDE installed
- Python installed (with required libraries)

---

## Arduino Circuit Connection

- Connect the servo signal pin to pin 9 of Arduino.
- Connect the servo VCC to 5V on Arduino.
- Connect the servo GND to GND on Arduino.
- Upload the Arduino code using Arduino IDE.

---

## Python Libraries Required

You need to install the following Python libraries:
- pyserial: For sending data to Arduino via USB
- speechrecognition: For converting voice to text
- pyaudio: For accessing microphone input

---

## How to Run the Project

Step 1: Upload the Arduino Code
- Open Arduino IDE
- Select Board → "Arduino UNO"
- Select Port → "COM11" (or your actual port)
- Paste the Arduino code and click Upload

Step 2: Run Python Script
- Save the Python code as voice_control.py
- Open Command Prompt
- Navigate to the folder using: cd path\to\your\folder
- Run the script: python voice_control.py

Now speak into your microphone using phrases like:

"Turn on the light"
"Turn off the light"

---

# License
This project is licensed under the MIT License. You are free to use, share, and modify it, but please give proper credit. This project is shared as-is with no warranty.

---

# Author
Himanshi Gigal

---
