import cv2

# save a video
# VideoWriter(path,fourcc code,no of frames per second,size)

# fourcc code
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter('./video.mp4',fourcc,20,(640,480))

# read a video from a file or a camera
# VideoCapture('filename'or'device index of your camera might be 0 or -1')
# for multiple camera you can use 1,2,3.. indexes also
cap= cv2.VideoCapture(0)

# loop to capture frame continously
# isOpened() retuen true is video is opened
while(cap.isOpened()):
    ret,frame=cap.read()
    # ret=true if frame is available and frame will have that frame
    # ret=false no frame is available


    # convert the BGR image to GRAYscale
    # cvtColor(source,typeof conversion)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Video',frame)

    # write the frame
    out.write(frame)
    if(cv2.waitKey(1)==27):
        break


# wait for 1millisec 
# key==27 is esc key
# release all the resources
cap.release()
out.release()
cv2.destroyAllWindows()

