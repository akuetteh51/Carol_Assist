import pyttsx3
en=pyttsx3.init()
voices=en.getProperty('voices')
en.setProperty('voice',voices[1].id)


def speak(text):
	
	en.say(text)
	en.runAndWait()

speak("kwame")