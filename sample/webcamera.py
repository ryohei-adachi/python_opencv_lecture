import cv2

#VideoCapture オブジェクトを取得
#エラーが出る場合は、VideoCaptureの値を変えてください
capture = cv2.VideoCapture(0)


while(True):
    
    #Webカメラのフレームを取得
    ret, frame = capture.read()

    #画面を表示
    cv2.imshow('frame',frame)

    #qキーを押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()