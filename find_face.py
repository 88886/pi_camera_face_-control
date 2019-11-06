import cv2
import time
import requests
capture = cv2.VideoCapture(0)#��ȡ����ͷ����
casc_path = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX


end_time=0
countdown=0
while(True):
    #��ȡһ֡ͼ��
    ret,frame=capture.read()#��һ������ֵ��boolֵ���ж��Ƿ���ͼ�񣬵ڶ�������ͼ��
    if ret:
        #ת��Ϊ�Ҷ�ͼ
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRects = faceCascade.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))#����һ�����飬�����������һ�£��������Ĵ�С��Χ�Ĳ���
        count = str(len(faceRects))

        if int(count) > 0:      #����0���⵽����
            start_time = time.time()#Ҫ�жϷ��������ʱ���������μ����������30�룬��Ȼ����ܲ���
            if end_time<1:
                requests.get("http://192.168.1.165:8080/")
                end_time = time.time()
            countdown= int(start_time-end_time)
            if start_time-end_time>30:
                requests.get("http://192.168.1.165:8080/") #ÿ���������Զ�Ҫ��������ip
                end_time = time.time()
            for faceRect in faceRects: #���ƿ�򣬵������ÿһ������
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        cv2.putText(frame, "count:"+count, (10, 40), font, 0.8, (0, 255, 255), 2)#���һ������������������ʾ
        #��ʾͼ��
        cv2.imshow("test", frame)
        c = cv2.waitKey(10)#�ȴ��˳���
        if c & 0xFF == ord('q'):
          break