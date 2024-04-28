import paho.mqtt.client as mqtt
import configparser as cp
import data_pb2 as data_pb2
import datetime

config_path = "config.ini"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("data/device/#")  # subscribe all message


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.hex()))
    now = datetime.datetime.now()
    print("datetime from machine: " + str(now))
    try:  # parse proto message
        db = data_pb2.Data()
        db.ParseFromString(msg.payload)

        print("datetime from message: " + str(datetime.datetime.fromtimestamp(db.time)))

        print("==>message parse result")
        print(db.id)
        print(db.time)
        print(db.sensor.temperature)
        print(db.sensor.humidity)
        print(db.sensor.voltage)

        print("======")
    except:
        print("message not proto")


config = cp.ConfigParser()
config.read(config_path)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.reconnect_delay_set(1, 10)  # reconneect delay in 10seconds

client.connect(
    config["MQTT"]["Broker"],
    config.getint("MQTT", "Port"),
    config.getint("MQTT", "KeepAlive"),
)

client.loop_forever()
