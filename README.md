# IoT Edge Gateway Simulator (RTOS Mock)

A Software-in-the-Loop (SIL) simulation of an IoT Edge Gateway designed to handle multi-protocol sensor telemetry asynchronously. The system mimics a Real-Time Operating System (RTOS) environment to process safety-critical data locally (Edge Computing).

## 🚀 Key Features
- **Multi-threaded Architecture:** Implements a strict Producer-Consumer design pattern using Python's `threading` and thread-safe `queue.Queue`.
- **Hardware Abstraction Layer (HAL):** Simulates continuous digital telemetry from multiple smart home peripherals (Environmental, Security, and Safety-Critical sensors).
- **Industry Standard Protocols:** Models data structures mimicking **Matter**, **Thread**, and **BLE (Bluetooth Low Energy)** protocols.
- **Firmware-Level Security:** Validates packet integrity on-the-fly using a custom math **Checksum** algorithm to detect and drop corrupted data or injection attempts.
- **Edge Computing & Safety-Critical Processing:** Decides and triggers emergency protocols locally in milliseconds (e.g., critical smoke detection alert) without internet/Cloud dependency.

## 🛠️ Architecture & Tech Stack
- **Language:** Python 3
- **Core Modules:** `threading`, `queue`, `time`, `random`
- **Design Pattern:** Producer-Consumer (FIFO)

The system bus (`queue.Queue`) ensures safe memory access between threads, eliminating *Race Conditions* and maximizing CPU efficiency by blocking the gateway thread until new data payloads are dispatched by the sensors.

## 📦 Project Structure
```text
iot-edge-gateway/
│
├── core/
│   ├── __init__.py
│   └── protocol_util.py   # Packaging, timestamping, and Checksum calculation
│
├── sensors/
│   ├── __init__.py
│   └── simulator.py       # HAL - Simulating physical sensors & sampling rate
│
└── main.py                # RTOS Scheduler, Gateway Core & Edge Processing
