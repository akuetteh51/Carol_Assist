import serial
import time
import speak
ser=serial.Serial('/dev/ttyUSB0',9600)
ser.timeout=1
#print(ser.name)

def DataToSend(text):
	ser .write(text.encode())
	time.sleep(0.5)
	speak.speak(ser.readline().decode('ascii'))
	ser.close()

# Arduino
# Serial.begin(9600);
# pinMode(LED_BUILTIN,OUTPUT);
# void loop
# if(Serial.available()>0){
# 	data=Serial.readStringUntil('\n');
# 	if(data =="on"){
# 	digitalWrite(LED_BUILTIN,HIGH);
# 	Serial.write("Light on");
# 	}
# 	if(data=="off"){
# 	digitalWrite(LED_BUILTIN,LOW);
# 	Serial.write("Led off");
# 	}
	
# 	}
DataToSend("on")