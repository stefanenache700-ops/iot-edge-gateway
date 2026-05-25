import time
import random
from protocol_util import pack_sensor_data

def run_sensors_simulation (data_queue):
    print("[Sensor Simulation] Harware abstraction layer started...")

    while True:
        temp_val = round(random.uniform(21.0, 26.0), 1)
        data_queue.put(pack_sensor_data("sensor_temp_01", "BLE", "temperature", temp_val))

        smoke_val = 0.0 if random.random() > 0.05 else round(random.uniform(1.2, 5.5), 1)
        data_queue.put(pack_sensor_data("sensor_smoke_01", "Thread", "smoke_level", smoke_val))

        lock_status = random.choice(["LOCKED", "UNLOCKED"])
        data_queue.put(pack_sensor_data("smart_lock_01", "Matter", "lock_status", lock_status))

        time.sleep(2)