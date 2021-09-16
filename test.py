import cv2
import os
import datetime

'''path = 'C:/Users/Asus/OneDrive/Desktop/juju/smrt goggles/codes/text detection/data base local'
cap = cv2.VideoCapture(0)
i = 1
os.chdir(path)

while(i<3):
    ret, frame = cap.read()
    if ret == False:
        break
    
    # Save Frame by Frame into specified path using imwrite method and name file like juju(1).jpg
    p=str(datetime.datetime.now())
    cv2.imwrite('test'+str(i)+'.png', frame)   
    i += 1 
cap.release()'''
p=str(datetime.datetime.now())
print(p)