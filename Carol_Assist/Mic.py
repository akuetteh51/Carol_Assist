import speech_recognition as s
listener=s.Recognizer()
# command=""
def Take_command(command):
	try:
		with s.Microphone() as source:
			print("Am listening!!!!....")
			voice=listener.listen(source)
			command=listener.recognize_google(voice)
			command=command.lower()
			if 'esther' in command: 
				command=command.replace('esther','')
				print(command)

	except:
		pass
	return command

def Carol():
	if 'light on' in  Take_command(command):
		light=Take_commmand(command).replace('light on','')
		print("light turned On")

while True:
	Carol()

