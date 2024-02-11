import cv2

#エラーが出る場合は、VideoCaptureの値を変えてください
cap = cv2.VideoCapture(0)
cascade_path = "haarcascade_frontalface_default.xml"

while True:

    ret, frame = cap.read()


    frame = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)

    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

    color = (0, 255, 0) 

    if len(facerect) > 0:
      for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    cv2.imshow('Raw Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()