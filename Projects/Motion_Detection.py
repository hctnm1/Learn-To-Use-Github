# we need to store the current frame of the video as soon as the video starts , we need to store that numpy array in variable , and have that variable static , so we don't want to change the value of the variable while the while loop runs in the script. as it will be set as the background. 
# when the motion occur it will show the image \video
# it won't display the static background

import cv2
import time

first_frame=None

video=cv2.VideoCapture(0)

while True:
    check , frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # GAUSSIAN BLUR METHOD : remove noise and smoth it , which increase the accuracy.
    # GAUSSIAN KERNEL: parameter of blurriness
    gray= cv2.GaussianBlur(gray,(21,21) , 0)       # 0= STANDAR DEVIATION


    if first_frame is None:
        first_frame = gray
        continue

    # ABSOLUTE DIFFERENCE: 
    del_frame= cv2.absdiff(first_frame , gray)

    # THRESHOLD METHOD:
    thres_frame=cv2.threshold(del_frame, 30 ,255 , cv2.THRESH_BINARY)[1]

    thres_frame=cv2.dilate(thres_frame, None , iterations=2)

    # CONTOUR METHOD : we want to store the contour in a tuple
    # RETRIEVE EXTERNAL METHOD : to draw external contours of the object
    # APPROXIMATION METHOD : chain_approx_simpe
    (cnts,__) = cv2.findContours(thres_frame.copy() , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.countourArea(countour) < 1000:
            continue

        (x , y ,w ,h) = cv2.boundingRect(countour)
        cv2.rectangle(frame,(x,y), (x+w , y+h) , (0 ,255,0) , 3) 


    cv2.imshow("motion", gray)
    cv2.imshow("compare", del_frame)
    cv2.imshow("threshold" ,thres_frame )

    print(gray)

    if cv2.waitKey(1)==ord('q'):         # press the "q" key and quit the video
        break

video.release()
cv2.destroyAllWindows()
