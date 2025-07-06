import cv2
import mediapipe as mp
import serial.tools.list_ports


cam = cv2.VideoCapture(0)

mp_hand = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hand.Hands()

# Serial port connection to arduino
try:
    serial = serial.Serial()
    serial.baudrate = 9600
    serial.port = 'COM3' # Change this according to your device port connected to arduino
    serial.open()
except Exception as e:
    print(e)

while True:

    success, frame = cam.read()

    if not success: break

    frame = cv2.flip(frame, 1)

    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbFrame)

    if results.multi_hand_landmarks:                
        landmarks = results.multi_hand_landmarks[0] # This only capture the first hand and read its gesture
        data = []
        mp_draw.draw_landmarks(
            frame,
            landmarks,
            mp_hand.HAND_CONNECTIONS
        )

        data.append(landmarks.landmark[4].x < landmarks.landmark[3].x)
        for finger_pos in [8, 12, 16, 20]:
            data.append(landmarks.landmark[finger_pos].y < landmarks.landmark[finger_pos - 1].y)

        try:
            extracted_data = ''.join(map(str, map(int, data))) + '*'
            serial.write(extracted_data.encode('utf-8'))
        except Exception as e:
            print(e)
        
    cv2.imshow('Hand Capture', frame)
    if cv2.waitKey(10) == 27: # Press ESC key to exit
        break


serial.close()
cam.release()
cv2.destroyAllWindows()