from yowsup.stacks import  YowStackBuilder
from layer import EchoLayer
from humedadLayer import HumedadLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv
#Este scrip es el que nos sirve para realizar la conexion a wassap
credentials = ("50372883405", "XW7+QE0ijFik0pqD8yfYiuPP7KA=") # aqui definimos una tupla con el numero de telefono registrado y la contraseña recivida por consola previamente antes configurado

if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\  #se llena la pila que se estara ejecutando constatemente a la espera de mensajes de texto se define una capa echo layer 
        .pushDefaultLayers(True)\#que es la capa que procesara los mensajes por wassap 
        .push(EchoLayer)\# se define la capa HumedadLayer que es la que se ejecutara para monitorear la humedad del suelo
        .push(HumedadLayer)\
        .build()

    stack.setCredentials(credentials)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    stack.loop() #this is the program mainloop se pone en un siclo la pila para que este a la espera de eventos
