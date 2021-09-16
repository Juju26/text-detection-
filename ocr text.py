#pipy for easyocr,torch torchvision torchaudio
import easyocr
import os
import glob
import cv2

path = 'C:/Users/Asus/OneDrive/Desktop/juju/smrt goggles/codes/text detection/data base local'
for filename in glob.glob(os.path.join(path, '*.png')):
   with open(os.path.join(path, filename), 'r') as f:
    #img_pa='C:/Users/Asus/OneDrive/Desktop/juju/smrt goggles/codes/using web cam/download.png' 
    res_list=[]
    read=easyocr.Reader(['en'])
    result=read.readtext(filename)
    for i in range(len(result)):    
        p=[]
        p.append(result[i][1])
        res_list.append(''.join(i for i in p))
    #print(res_list)


