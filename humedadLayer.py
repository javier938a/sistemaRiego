from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import RPi.GPIO as GPIO
import time
from datetime import date, datetime

class HumedadLayer(YowInterfaceLayer):
    pinVal=2 #Pin para la valvula
    pinBon = 3# pin para la bonba
    hume= 4# Define el pin del sensor de Humedad
    def __init__(self):
		iniciarSensoreo()
		
		
    def iniciarSensoreo(self):#se encargara de sensorear a cada rato la hora para empesar a detectar si la tierra esta seca si la tierra esta seca lanzara 0 y si esta humeda lanzara 1
		while True:
			hora = datetime.now().hour
			minuto = datetime.now().minute
			if hora == 6 and minuto == 0 or hora == 18 and minuto == 0 :
				print "prueva si el suelo esta mojado"
				valor = GPIO.input(hume)
		    if valor == 0:#si la tierra esta seca regara por 15 minutos
                GPIO.output(pinVal,GPIO.LOW)# enciende la valvula
                GPIO.output(pinBon,GPIO.LOW)#enciende la bonba
                time.sleep(900) #adormece por 15 minutos 
                GPIO.output(pinVal,GPIO.HIGH)#apaga la valvula
                GPIO.output(pinBon,GPIO.HIGH)#apaga la bonba
			elif valor ==1:
				GPIO.output(pinVal,GPIO.HIGH)# si el la tierra esta humeda se apagan los aparatos bonba  valbula
				GPIO.output(pinBon,GPIO.HIGH)
		
		
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())

            outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                messageProtocolEntity.getBody(),
                to = messageProtocolEntity.getFrom())

            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
