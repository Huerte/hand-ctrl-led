<div align="center">

# hand-ctrl-led

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![Platform](https://img.shields.io/badge/platform-Python%20%7C%20Arduino-blueviolet.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)
[![Last Commit](https://img.shields.io/github/last-commit/Huerte/hand-ctrl-led.svg)](#)

**A hand gesture recognition system that controls 5 Arduino LEDs based on finger states.**

<a href="https://github.com/Huerte/hand-ctrl-led/issues">Report Bug</a> · <a href="https://github.com/Huerte/hand-ctrl-led/issues">Request Feature</a>

</div>

---

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Hardware Setup](#hardware-setup)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Demo

> Screenshot demonstrating the project hardware layout.

![Demo Screenshot](src/wiring%20diagram/circuit.png)

_This project runs in a terminal environment and relies on webcam access to detect gestures._

---

## Features

hand-ctrl-led provides a real-time computer vision interface designed for hardware control via gestures.  
Built to be responsive, easy to set up, and highly customizable for other hardware applications.

- **Real-time Hand Tracking:** Uses MediaPipe and OpenCV to track hand gestures via a webcam.
- **Finger State Detection:** Accurately detects whether each of the 5 fingers is open or closed based on joint coordinates.
- **Serial Communication:** Efficiently sends binary state data to the Arduino microcontroller over a USB Serial connection.
- **Hardware Control:** Maps the state of 5 fingers to 5 individual LEDs via Arduino GPIO pins.

---

## Prerequisites

- **Python 3.x**
- **Arduino IDE**
- **Hardware:**
  - 1x Arduino Board (e.g., Uno, Nano)
  - 5x LEDs
  - 5x Resistors (e.g., 220Ω or 330Ω)
  - Jumper wires and breadboard
  - Webcam

---

## Installation Guide

Follow these steps to set up the software for the project.

### Step 1: Get the Code

```bash
git clone https://github.com/Huerte/hand-ctrl-led.git
cd hand-ctrl-led
```

---

### Step 2: Install Python Dependencies

It is recommended to use a virtual environment. Install the required packages via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### Step 3: Flash the Arduino

1. Open the `src/script/script.ino` file using the Arduino IDE.
2. Connect your Arduino board to your computer via USB.
3. Select your board and the corresponding COM port in the Arduino IDE (`Tools` > `Board` / `Port`).
4. Click the **Upload** button to flash the code to the Arduino.

---

## Usage

1. **Verify COM Port:** Ensure the Arduino is connected. Open `src/main.py` and modify the `serial.port` value on line 17 to match your Arduino's COM port (e.g., `'COM3'`, `/dev/ttyACM0`).
2. **Setup Circuit:** Wire your LEDs to pins 7, 8, 9, 10, and 11 on the Arduino. (See [Hardware Setup](#hardware-setup))
3. **Run the Script:** Execute the Python script.
   ```bash
   python src/main.py
   ```
4. **Action:** The webcam window should appear. Hold your hand up to the camera. Open or close your fingers to turn the corresponding LEDs on or off.
5. **Exit:** Press the `ESC` key while focused on the webcam window to exit the program safely.

---

## Project Structure

```text
hand-ctrl-led/
│
├── src/
│   ├── main.py                  # Core Python logic (OpenCV & MediaPipe)
│   ├── script/
│   │   └── script.ino           # Arduino code to receive serial data and control LEDs
│   └── wiring diagram/
│       └── circuit.png          # Visual breadboard diagram for the LEDs
│
├── LICENSE                      # MIT License file
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Hardware Setup

The Arduino expects 5 LEDs connected to specific digital pins configured as outputs. 

**Pin Mapping:**
- **Pin 7:** LED 1 (Thumb)
- **Pin 8:** LED 2 (Index Finger)
- **Pin 9:** LED 3 (Middle Finger)
- **Pin 10:** LED 4 (Ring Finger)
- **Pin 11:** LED 5 (Pinky Finger)

*Make sure to use a current-limiting resistor for each LED connected to the ground (GND).*
Refer to the `src/wiring diagram/circuit.png` file for a visual representation.

---

## Troubleshooting

### Common Issues

**Serial Port Error**
```text
serial.serialutil.SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)
```
> **Fix:** 
> 1. Ensure the Arduino IDE Serial Monitor is closed, as it blocks the port.
> 2. Verify that the COM port in `src/main.py` matches the one your Arduino is connected to.

**Webcam Not Turning On**
```text
cv2.error: OpenCV(4.11.0) /io/opencv/modules/highgui/src/window.cpp:971: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
```
> **Fix:** 
> Ensure your webcam is properly connected and recognized by your OS. If you have multiple cameras, change `cv2.VideoCapture(0)` in `src/main.py` to `cv2.VideoCapture(1)` or higher.

> Still stuck? [Open an issue](https://github.com/Huerte/hand-ctrl-led/issues) with your error details and environment info.

---

## Contributing

Contributions are welcome and appreciated!

1. Fork the Project
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the **MIT** License. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

&copy; 2026 Huerte. All Rights Reserved.

</div>
