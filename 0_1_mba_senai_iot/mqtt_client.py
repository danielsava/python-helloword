"""
    Para instalar o módulo MQTT
    - pip install paho-mqtt
"""


import paho.mqtt.client as mqtt
import time
import json
import random

# Dados de conexão com o Broker
mqtt_broker = "192.168.101.58"  # "iot.eclipse.org"
mqtt_broker_port = 1883
mqtt_keep_alive = 60

# Variável de controle para reacao com o atuador dispositivo IoT
cmd_status_controle = False

# Topics Broker
mqtt_topic_pub = "iot/senai/101/sava/cmd"
mqtt_topic_sub = "iot/senai/101/sava/data"


# Callback de conexão
def on_connect(client, userdata, flags, rc):
    print("Conectado! - Status: " + str(rc))
    client.subscribe(mqtt_topic_sub)


def on_message(client, userdata, msg):
    global cmd_status_controle
    msg_recebida = str(msg.payload, 'utf-8')
    print('MSG: [' + msg.topic + '] - ' + msg_recebida)
    msg_json = json.loads(msg_recebida)

    if float(msg_json["UMID"]) >= 60.0:
        cmd_status_controle = True
    else:
        cmd_status_controle = False


# Código principal da aplicação
if __name__ == '__main__':
    print(" ###### Iniciando aplicação Cliente MQTT #####")

    # Cria objeto cliente para MQTT
    client = mqtt.Client(client_id="iot_python_sava", clean_session=True)

    # Vínculo de callbacks de eventos
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_broker, mqtt_broker_port, mqtt_keep_alive)

    # Espera um pouco pra conexao
    time.sleep(5)

    # Inicia thread de monitoramento do cliente MQTT
    client.loop_start()

    while True:
        time.sleep(3)

        if cmd_status_controle:
            if not bool(msg_json["CMD"]): #Controle para não ficar mandando toda hora desligar
                client.publish(mqtt_topic_pub, "ON")
        else:
            if bool(msg_json["CMD"]):
                client.publish(mqtt_topic_pub, "OFF")