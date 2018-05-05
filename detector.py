import cv2
import numpy as np
def Recognise_Face(ImageName):
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    rec=cv2.face.LBPHFaceRecognizer_create();
    rec.read("trainingData.yml")
    id=0
    fontface=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.imread(ImageName);
    #print(img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if id==1:
            id="Sahil"    
        else:
            id="Unknown"   
        cv2.putText(img,str(id),(x,y+h),fontface,2,(255,0,0),3);
    return id

if __name__ == '__main__':
    name = Recognise_Face('try.jpg')
    print(name)