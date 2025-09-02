import cv2

#choose camera width and height
FrameWidth = 800
FrameHeight = 600

#write a function to capture the video

cap = cv2.VideoCapture(0)
#capture video

while True:
    success, img = cap.read() # if the camera is opened it will return success
    #resize image
    img_captured = cv2.resize(img, (FrameWidth, FrameHeight))
    #lets make a greyscale image as well
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_greyresize = cv2.resize(img_grey, (FrameWidth, FrameHeight))
    cv2.imshow("Greyscale Image", img_greyresize)
    #display image
    cv2.imshow("Captured Image", img_captured)

    #write something to remove captured image
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()