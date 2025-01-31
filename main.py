import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
#######################


##########################
cap = cv2.VideoCapture(0)
detector = htm.FindHands(detection_con=0.7)

ptime = 0

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface,POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=400
volPer = 0
while True:
    success, img = cap.read()
    if not success:
        continue  # Skip this frame if reading failed

    img = detector.findHands(img)  # Detect hands
    lmList = detector.findPosition(img, draw=False)  # Get hand landmarks

    if len(lmList) != 0:  # Ensure index 4 and 8 exist
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip
        cx,cy=(x1+x2)//2, (y1+y2)//2

        print(f"Thumb Tip: ({x1}, {y1}) | Index Finger Tip: ({x2}, {y2})")  # ✅ Keep printing coordinates

        # Draw circles on thumb and index finger tips
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2-x1,y2-y1)
        # print(length)
        # hand range 50-300
        # vol range -65 - 0
        vol = np.interp(length,[50,300],[minVol,maxVol])
        volBar = np.interp(length,[50,300],[400,150])
        volPer = np.interp(length,[50,300],[0,100])

        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    else:
        print("No hand detected.")
    # FPS Calculation
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(img, f'volume: {int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

    ctime = time.time()
    fps = 1 / (ctime - ptime) if ctime != ptime else 0
    ptime = ctime

    # Display FPS on the frame
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    # Show the image
    cv2.imshow("Img", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
