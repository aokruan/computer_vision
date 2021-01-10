import time
import cv2
from imageai.Detection import ObjectDetection

# Для получения видеопотока с камеры
camera = cv2.VideoCapture(0)

# Для получения видеопотока с видео
# camera = cv2.VideoCapture("videoplayback1.mp4")

# Подключаем библиотеку
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("yolo-tiny.h5")
detector.loadModel()

finish = 0
array_detection = []

while camera.isOpened():
    ret, frame = camera.read()

    start = time.time()
    if start - finish > 2:
        _, array_detection = detector.detectObjectsFromImage(input_image=frame, input_type="array", output_type="array")
        finish = time.time()
        print(array_detection)

    for obj in array_detection:
        coord = obj["box_points"]
        cv2.rectangle(frame, (coord[0], coord[1]), (coord[2], coord[3]), (0, 0, 255))
        cv2.putText(frame, obj["name"], (coord[0], coord[1] - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    cv2.imshow("Test", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
exit(-1)

# from imageai.Detection import ObjectDetection
#
# detector = ObjectDetection()
# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath("yolo-tiny.h5")
# detector.loadModel()
#
# # Генерируем новое изображение с выделением границ
# # detector.detectObjectsFromImage(input_image="1.jpg", output_image_path="new_image.jpg")
# array_detection = detector.detectObjectsFromImage(input_image="1.jpg", output_image_path="new_image.jpg")
# print(array_detection)
