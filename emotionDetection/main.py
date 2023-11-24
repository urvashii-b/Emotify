from keras.models import load_model
from time import sleep
from keras_preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2 #OpenCV ---> video is a collection of frames
import numpy as np
from flask import Flask , render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    face_classifier = cv2.CascadeClassifier(r'C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\emotionDetection\haarcascade_frontalface_default.xml')
    classifier =load_model(r'C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\emotionDetection\model.h5')

    emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

    cap = cv2.VideoCapture(0) # 0 for default camera of personal computer - capture

    i=0
    L={}
    while True:
        _,frame=cap.read()
        labels = []
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # converting to grayscale
        faces = face_classifier.detectMultiScale(gray)

        # making a rectangle box for face
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            roi_gray = gray[y:y+h,x:x+w] # region of interest = vertical height + horizontal width
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA) # trained model standard size

            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0] # using model to predict
                label=emotion_labels[prediction.argmax()] # maximum for angry
                if(label in L):
                    L[label]+=1
                else:
                    L[label]=1
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Emotion Detector',frame)
        i+=1
        print(i)
        if cv2.waitKey(1) & 0xff == ord('q') | i>50:
            break

    val = max(zip(L.values(),L.keys()))[1]
    if (val=='Angry' or val=='Surprise'):
        val = "Energetic"
    elif (val=='Fear' or val=='Neutral'):
        val = 'Calm'

    print(val)
    fp = open(r"C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\new.txt","w")
    fp.write(val)
    fp.close()
    import os
    os.system(r'python C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\songRecommender\test.py')
    print(max(zip(L.values(),L.keys()))[1])
    cap.release() # stop capturing frames
    cv2.destroyAllWindows()
    time.sleep(5)
    return "Hello World!"

if __name__ == '__main__' :
    app.debug =True
    app.run() # 0 for default camera of personal computer - capture