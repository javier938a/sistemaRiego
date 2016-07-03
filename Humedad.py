import RPi.GPIO as GPIO
from datetime import date, datetime
import time

class Humedad(object):
    def __init__(self):
        self.pinVal = 2#pin de valvula
        self.pinBon = 3#pin de bonba
        self.hume = 4#pin de el sensor de humedad
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinVal,GPIO.OUT)#establece pin de valvula como salida
        GPIO.setup(self.pinBon,GPIO.OUT)#establece pin de bonba como salida
        GPIO.setup(self.hume,GPIO.IN)#establece pin de sensor de humedad como entrada
        self.iniciarSensoreo()#llama al metodo que ejecutara el sensoreo de humedad de tierra
    def iniciarSensoreo(self):
        while True:#introducimos un siclo infinito para que este revisando el estado del sensor y hora
            print "Hola soy un siclo"
            self.hora = datetime.now().hour#campura la hora
            self.minuto = datetime.now().minute#captura los minutos
            print "hora: "+str(self.hora)+"Minuto: "+str(self.minuto)
            if self.hora > 0 and self.minuto > 0 or self.hora> 0 and self.minuto>0:#aqui defini asi porque el objetivo era probar el sensor de humedad pero para ya dejarlo en aplicaion tendria que especificar la hora que empesara a regar
                print "prueva si el suelo esta mojado"
                self.valor = GPIO.input(self.hume)#Obtenemos el estado del el sensor de humedad su esta seco 0 y se esta mjado es 1
                print "Estado sensor humedad: "+str(self.valor)
                if self.valor == 0:#si la tierra esta seca regara por 15 segundos por cuestiones de prueva y no perder tiempo
                    GPIO.output(self.pinVal,GPIO.LOW)# enciende la valvula
                    GPIO.output(self.pinBon,GPIO.LOW)#enciende la bonba
                    time.sleep(15) #adormece por 15 minutos o esperamos 15 minutos 
                    GPIO.output(self.pinVal,GPIO.HIGH)#apaga la valvula
                    GPIO.output(self.pinBon,GPIO.HIGH)#apaga la bonba
                elif self.valor ==1:# si valor es igual a 1 entonces a tierra esta mojada y se apagan los aparatos 
                    GPIO.output(self.pinVal,GPIO.HIGH)# si el la tierra esta humeda se apagan los aparatos bonba  valbula
                    GPIO.output(self.pinBon,GPIO.HIGH)


hume = Humedad()

