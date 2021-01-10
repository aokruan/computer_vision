import cv2
import pytesseract
from imutils import contours

# Расположение tesseract в системе
pytesseract.pytesseract.tesseract_cmd = "D:\Program Files\Tesseract-OCR\\tesseract.exe"

image = cv2.imread("ex10.jpg")
height, width, _ = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imS = cv2.resize(gray, (960, 540))

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = contours.sort_contours(cnts[0])

for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    if area > 5000:
        img = image[y:y + h, x:x + w]
        result = pytesseract.image_to_string(img, lang="rus")
        if len(result) > 7:
            print(result)

# Отображение изображения в окне
# cv2.imshow("output", thresh)

# Закрыть окно по любому нажатию
# cv2.waitKey()


