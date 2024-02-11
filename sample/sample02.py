#OpenCVのライブラリを組み込む
import cv2

#画像を読み込む
img = cv2.imread('image/fruits.jpg')

#画像をグレースケール化する。
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#画像を表示する
cv2.imshow("Fruits Image", gray_img)

#キーボードを押すと画像の表示終了
cv2.waitKey(0)

#表示した画像ウィンドウを閉じる
cv2.destroyAllWindows()