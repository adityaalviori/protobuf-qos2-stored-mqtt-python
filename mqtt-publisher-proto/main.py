import paho.mqtt.client as mqtt
import configparser as cp
from getmac import get_mac_address as gma
import time
import random
import data_pb2 as data_pb2
import datetime

config_path = "config.ini"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))


if __name__ == "__main__":
    config = cp.ConfigParser()
    config.read(config_path)

    client = mqtt.Client(config["MQTT"]["ClientID"], False)
    # client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect(
        config["MQTT"]["Broker"],
        config.getint("MQTT", "Port"),
        config.getint("MQTT", "KeepAlive"),
    )
    client.loop_start()
    count = 0
    qos_pub = config.getint("MQTT", "QoS")
    print(qos_pub)

    while True:

        mac = gma()
        topic_pub = "data/device/" + mac.replace(":", "")

        now = datetime.datetime.now()

        print(now)

        db = data_pb2.Data()
        db.id = count
        db.time = int(datetime.datetime.timestamp(now))
        db.sensor.temperature = random.randint(250, 350)
        db.sensor.humidity = random.randint(550, 650)
        db.sensor.voltage.extend(
            [
                random.randint(220, 225),
                random.randint(220, 225),
                random.randint(220, 225),
            ]
        )

        proto_msg = db.SerializeToString()

        print(proto_msg.hex())
        print(db.id)
        print(db.time)
        print(db.sensor.temperature)
        print(db.sensor.humidity)
        print(db.sensor.voltage)
        

        client.publish(topic_pub, proto_msg, qos=qos_pub, retain=True)

        count = count + 1

        print("======")

        time.sleep(10)
