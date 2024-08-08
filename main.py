import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

counter = 0

face_match = False

reference_img = cv2.imread("reference.jpg")

def check_face(frame):
    pass

while True:
    ret, frame = cap.read()
    
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
    
    if face_match:
        cv2.putText(frame, "Face Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "No Face Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        breakgit a

cap.release()
cv2.destroyAllWindows()
