import cv2 

video_capture = cv2.VideoCapture(0)
while True:
    ret, video_data = video_capture.read()
    cv2.imshow("Live Video Press Q to Exit", video_data)
    if (cv2.waitKey(10) == ord('q')):
        break

video_capture.release()