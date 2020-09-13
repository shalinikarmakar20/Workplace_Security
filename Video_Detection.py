import cv2,time
n=10
for i in range(0,n):
    video=cv2.VideoCapture(i)
    a=1
    while True:
      a=a+1
      check,frame=video.read()
      print(frame)
      qray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow("Capture",qray)
      cv2.imshow("Capture1",frame)
      cv2.waitKey(1)
    if key==ord('q'):
        break
    print(a)
video.release()
cv2.destroyAllWindows()
