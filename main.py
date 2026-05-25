import threading
import queue
import time
import json
from simulator import run_sensors_simulation

def run_gateway_core(data_queue):
    print("[Gateway Core] sensor is running. Listening for sensor payloads...")

    while True:
        payload = data_queue.get()
        
        received_checksum = payload.pop("checksum", None)
        
        data_string = f"{payload['sensor_id']}{payload['protocol']}{payload['type']}{payload['value']}"
        calculated_checksum = sum(ord(c) for c in data_string) % 256
        
        if received_checksum != calculated_checksum:
            print(f"SECURITY ERROR: Pachet corupt detectat de la {payload['sensor_id']}! Dropped.")
            data_queue.task_done()
            continue
        sensor_id = payload["sensor_id"]
        protocol = payload["protocol"]
        data_type = payload["type"]
        val = payload["value"]

        print(f"DATA LOG: [{protocol}] Recieved from {sensor_id}: {val}")

        if data_type == "smoke_level" and val > 1.0:
            print(f"CRITICAL EVENT: SMOKE DETECTED ({val})! Triggering emergency protocols.")

        data_queue.task_done()

def main():
     print("=" * 60)
     print("     IoT EDGE GATEWAY SIMULATOR - PRODUCTION READY      ")
     print("=" * 60)

     system_bus = queue.Queue()

     sensor_thread = threading.Thread(
          target = run_sensors_simulation,
          args = (system_bus,),
          daemon = True
     )

     gateway_thread = threading.Thread(
          target = run_gateway_core,
          args = (system_bus,),
          daemon = True
     )

     sensor_thread.start()
     gateway_thread.start()

     try:
          while True:
               time.sleep(1)
     except KeyboardInterrupt:
            print("\n SYSTEM: Gateway-ul a fost oprit controlat din terminal. System offline.")

if __name__ == "__main__":
     main()
        