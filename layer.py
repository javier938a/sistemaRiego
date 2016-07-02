from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import RPi.GPIO as GPIO
import time

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
       
        pinVal=2 #Pin para la valvula
        pinBon = 3# pin para la bonba
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinVal,GPIO.OUT)
        GPIO.setup(pinBon,GPIO.OUT)
        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            print messageProtocolEntity.getBody()
            sms = messageProtocolEntity.getBody()
            notif = ""
            if sms =="OFF":
                notif= "Sistema de riego Apagado"
                GPIO.output(pinVal,GPIO.HIGH)
                GPIO.output(pinBon,GPIO.HIGH)
                
            elif sms == "ON":
                notif="Sistema de riego encendido"
                GPIO.output(pinVal,GPIO.LOW)
                GPIO.output(pinBon,GPIO.LOW)
            if notif=="": 
                notif = "Comando no valido"
            outgoingMessageProtocolEntity = TextMessageProtocolEntity(notif, to = messageProtocolEntity.getFrom())
            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
