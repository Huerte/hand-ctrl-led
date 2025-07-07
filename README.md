# Hand LED Controller

## Features

- Real-time hand tracking using cam
- Detects each finger pos in real-time
- Send commands to Arduino via serial
- Each raised finger turns ON its assigned LED; lowering it turns it OFF

## Project Structure

```
├── src/
│   ├── main.py              # Python script (hand tracker)
│   └── sketch/
│       └── sketch.ino       # Arduino sketch
│   └── wiring diagram/
│       └── circuit.png      # Wiring diagram
├── requirements.txt
└── README.md
```

## Arduino side

### Hardware

- Arduino Uno R3
- 5 LED and 220 ohm resistor
- Jumper wires
- Breadboard

### Software
Open `src/sketch/sketch.ino` using Arduino IDE and upload to your board

> **Reminder:** Make sure to select the correct **COM port**:
>
> - In **Arduino IDE**: `Tools > Port`
> - In **Python code**: Edit the serial port in main.py `serial.port = 'COM3'` with your device port
>
> You can find the correct COM port in Arduino IDE after connecting the board.

### Wiring Diagram

![Circuit Diagram](/src/wiring%20diagram/circuit.png)

### Finger to LED Mapping

| Finger        | LED Pin on Arduino |
|---------------|--------------------|
| Thumb         | 8                  |
| Index Finger  | 9                  |
| Middle Finger | 10                 |
| Ring Finger   | 11                 |
| Pinky Finger  | 12                 |

## Python side

### Dependencies

```bash
pip install -r requirements.txt
```

### Run the Script
Make sure your Arduino is connected and update the COM port in `main.py`:

```python
serial.port = "COM3"  # Replace with your actual COM port
```

Then run:

```bash
python src/main.py
```

This will open your webcam and start gesture detection.

## Serial Communication

The Python script detects a single hand using MediaPipe and checks if each finger is raised.
It sends a 5-bit binary command (followed by `*`) to the Arduino through the serial port.

| Finger        | Bit Position | Detection Logic                                  |
|---------------|--------------|--------------------------------------------------|
| Thumb         | 0            | Tip (4) is left of joint (3)                     |
| Index Finger  | 1            | Tip (8) is above joint (7)                       |
| Middle Finger | 2            | Tip (12) is above joint (11)                     |
| Ring Finger   | 3            | Tip (16) is above joint (15)                     |
| Pinky Finger  | 4            | Tip (20) is above joint (19)                     |

Example output:
- `11111*` → All fingers up
- `01000*` → Only index finger up
- `00000*` → All fingers down

These strings are sent over serial like:

```python
serial.write("10110*".encode('utf-8'))
```

On the Arduino side, you can read the string, parse each bit, and control LEDs or devices accordingly.

## How It Works

1. **Hand Detection (Python + MediaPipe)**  
   The webcam captures live video. MediaPipe detects a hand and tracks 21 keypoints (landmarks) on it.

2. **Finger State Detection**  
   For each finger, we check if it's raised using the position of key landmarks:
   - Thumb: checks if tip is to the left of its joint.
   - Fingers: checks if tip is above the lower joint.

3. **Binary Encoding**  
   Each finger’s state is encoded as `1` (up) or `0` (down), forming a 5-bit binary string like `10110`.

4. **Serial Communication to Arduino**  
   The binary string with a `*` suffix (e.g. `10110*`) is sent over the serial port to the Arduino.

5. **Arduino Action**  
   Arduino reads the string, decodes it, and turns LEDs ON/OFF depending on the combination of finger states.

## Credits

Uses:
- [MediaPipe Hands](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV](https://opencv.org/)
- [Arduino Serial Communication](https://docs.arduino.cc/language-reference/en/functions/communication/serial/)

---

## License

Licensed under the MIT License. You can use, modify, and share this freely with attribution.
