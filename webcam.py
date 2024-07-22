import cv2

capture=cv2.VideoCapture(0)
result=True
while (result):
    a,frame=capture.read()
    cv2.imwrite("test.jpg",frame)
    result=False
    print("image captured....")

capture.release()
