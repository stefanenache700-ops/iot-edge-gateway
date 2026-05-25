import time

def pack_sensor_data(sensor_id, protocol, data_type, value):
    payload = {
        "sensor_id": sensor_id,
        "protocol": protocol,
        "type": data_type,
        "value": value,
        "timestamp": time.time()
    }
    
    data_string = f"{sensor_id}{protocol}{data_type}{value}"
    payload["checksum"] = sum(ord(c) for c in data_string) % 256
    
    return payload