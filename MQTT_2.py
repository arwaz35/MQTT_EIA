from http import client
import paho.mqtt.client as mqtt
import time

def on_message(cliente,userdata,message):
    dato = message.payload.decode('utf-8')
    print(dato)
    print(type(dato))
    #print("mensaje recibido",str(message.payload.decode("utf-8")))

broker_ip = 'daniel-eia.cloud.shiftr.io'

cliente = mqtt.Client("dispositivo1")
cliente.username_pw_set('daniel-eia', 'PfB28Q6QswPRw9iY')
cliente.connect(broker_ip)
cliente.subscribe('compresor1/Corriente/Fase', 0)

cliente.on_message = on_message
#cliente.loop_start()
cliente.loop_forever()
# while True:
#     dato = cliente.subscribe('compresor1')
#     print("Dato: ", dato)
#     time.sleep(1)
    