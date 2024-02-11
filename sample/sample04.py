#OpenCVのライブラリを組み込む
import cv2

#画像を読み込む
img = cv2.imread('image/fruits.jpg')

#四角形を画像に描写する(緑色)
img = cv2.rectangle(img, (0,10), (200,200), (0,255,0), 3)

#円形を画像に描写する(青色塗りつぶり)
img = cv2.circle(img, (300,300), 100, (255,0,0), -1)


#画像を表示する
cv2.imshow("Fruits Image", img)

#キーボードを押すと画像の表示終了
cv2.waitKey(0)

#表示した画像ウィンドウを閉じる
cv2.destroyAllWindows()