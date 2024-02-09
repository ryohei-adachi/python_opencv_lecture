#OpenCVのライブラリを組み込む
import cv2

#画像を読み込む
img = cv2.imread('fruits.jpg')

#画像のサイズを変更する
resize_img = cv2.resize(img, dsize=(800,300))

#画像を表示する
cv2.imshow("Fruits Image", resize_img)

#キーボードを押すと画像の表示終了
cv2.waitKey(0)

#表示した画像ウィンドウを閉じる
cv2.destroyAllWindows()