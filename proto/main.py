import data_pb2 as data_pb2

if __name__ == "__main__":
    
    db = data_pb2.Data()
    db.id = 123
    db.time = 1714026073
    db.sensor.temperature = 310
    db.sensor.humidity = 650
    db.sensor.voltage.extend(
        [
            221,
            225,
            222,
        ]
    )
    
    proto_msg = db.SerializeToString()
    
    print("proto raw message:", proto_msg.hex())
    
    db2 = data_pb2.Data()
    db2.ParseFromString(proto_msg)
    print("proto parse: ")
    print(db2)
    
    print("proto parse each param: ")
    print(db2.id)
    print(db2.time)
    print(db2.sensor.temperature)
    print(db2.sensor.humidity)
    print(db2.sensor.voltage)