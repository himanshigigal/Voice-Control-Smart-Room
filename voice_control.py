import serial
import time
import speech_recognition as sr

# Setup Serial Communication (replace COM11 with your port)
arduino = serial.Serial('COM11', 9600)
time.sleep(2)  # Wait for Arduino to reset

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            if "turn off the light" in command.lower():
                arduino.write(b'1')  # Send '1' to Arduino
            elif "turn on the light" in command.lower():
                arduino.write(b'0')  # Send '0' to Arduino

        except Exception as e:
            print("Sorry, could not recognize your voice:", e)
