from http import client
import paho.mqtt.client as mqtt
import time
import random

broker_ip = 'daniel-eia.cloud.shiftr.io'

cliente = mqtt.Client("dispositivo1")
cliente.username_pw_set('daniel-eia', 'PfB28Q6QswPRw9iY')
cliente.connect(broker_ip)

cliente2 = mqtt.Client("dispositivo2")
cliente2.username_pw_set('daniel-eia', 'PfB28Q6QswPRw9iY')
cliente2.connect(broker_ip)

cliente.loop_start()
while True:
    valor_1= round(random.uniform(20.0, 50.0),2)
    valor_2= round(random.uniform(200.0, 500.0),2)
    cliente.publish("compresor1/Corriente/Fase", valor_1)
    cliente.publish("compresor1/Corriente/Fase2", valor_2)
    # cliente2.publish("compresor2/Corriente/Fase", 46)
    print("Envio de datos")
    time.sleep(5)
    
    
    