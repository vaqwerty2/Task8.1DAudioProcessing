import speech_recognition as sr
from gpiozero import LED
from time import sleep

led = LED(17)

recognizer = sr.Recognizer()

def listen_for_commands(audio_file):
	with sr.AudioFile(audio_file) as source:
		audio = recognizer.record(source)

		try:
			command = recognizer.recognize_sphinx(audio)
			print(f"You said: {command}")
			return command

		except sr.UnknownValueError:
			print("Sorry, What did you say?")
			return ""
			
		except sr.RequestError as e:
			print(f"{e}")
			return ""


def control_led(command):
	if "on" in command:
		led.on()
		print("LED is on")
	elif "off" in command:
		led.off()
		print("LED is off")

audio_file = "/home/vidul11/Music/record_out.wav"
try:
	while True:
		command = listen_for_commands(audio_file)
		control_led(command)
		sleep(1)
except KeyboardInterrupt:
	print("Program stopped manually")
	led.off()
