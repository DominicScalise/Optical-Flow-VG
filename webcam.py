import cv2
import numpy as np
import math
import ball
import rect

cap = cv2.VideoCapture(0)

pong = ball.ball(100,100, 10)

center = [350,70]
center2 = [350, 1000]
paddle1 = rect.paddle(center, h = 200, w = 100)
paddle2 = rect.paddle(center2, h = 200, w = 100)

while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img,1)
    cv2.rectangle(img,(120,20),(0,700),(0,255,0),0)
    crop_imgL = img[20:700, 0:120]
    cv2.rectangle(img,(1158,20),(1278,700),(0,255,0),0)
    crop_imgR = img[20:700, 1158:1278]
    cv2.circle(img, (pong.ypos, pong.xpos), 10, (250, 250, 250), thickness=20)


    # LEFT
    grey = cv2.cvtColor(crop_imgL, cv2.COLOR_BGR2GRAY)
    # grey2 = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)

    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
           cv2.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    x,y,w,h = cv2.boundingRect(cnt)
    #cv2.rectangle(crop_imgL,(x,y),(x+w,y+h),(0,0,255),0)
    cv2.rectangle(crop_imgL,(0,20),(0,700),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_imgL.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_imgL,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_imgL,start,end,[0,255,0],2)
        #cv2.circle(crop_imgL,far,5,[0,0,255],-1)


    # RIGHT
    grey = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)
        # grey2 = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                                   cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
               cv2.CHAIN_APPROX_NONE)

    cnt = max(contours, key = lambda x: cv2.contourArea(x))


    x,y,w,h = cv2.boundingRect(cnt)
    #cv2.rectangle(crop_imgL,(x,y),(x+w,y+h),(0,0,255),0)
    cv2.rectangle(crop_imgR,(0,20),(0,700),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_imgR.shape,np.uint8)


    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1

            cv2.circle(crop_imgR,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_imgR,start,end,[0,255,0],2)
        #cv2.circle(crop_imgL,far,5,[0,0,255],-1)

        
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    YELLOW_MIN = np.array([20, 80, 80],np.uint8)
    YELLOW_MAX = np.array([40, 255, 255],np.uint8)
    BLUE_MIN = np.array([110,50,50],np.uint8)
    BLUE_MAX = np.array([130,255,255],np.uint8)
    SKINTONE_MIN = np.array([0,48,80],np.uint8)
    SKINTONE_MAX = np.array([20,255,255],np.uint8)


    #Skin tone detector
    frame_threshed = cv2.inRange(hsv_img, SKINTONE_MIN, SKINTONE_MAX)
    imgray = frame_threshed
    ret,thresh = cv2.threshold(frame_threshed,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]


    count2 = 0;
    yavg = 0;
    for y in range(0, 700):
        count = 0;
        for x in range(20, 120):
            if(frame_threshed[y][x] != 0): count += 1
        if count >= 75:
            yavg += y
            count2 += 1

    if count2 != 0:
        yavg = yavg/count2
    else: yavg = center[0]

    count2 = 0;
    yavg2 = 0;
    for y in range(0, 700):
        count = 0;
        for x in range(700, 1300):
            if (frame_threshed[y][x] != 0): count += 1
        if count >= 75:
            yavg += y
            count2 += 1

    if count2 != 0:
        yavg2 = yavg2/count2
    else: yavg2 = center2[0]



    cv2.rectangle(img, paddle1.topleft, paddle1.bottomright, (0,255,0), thickness= -1, lineType=8, shift=0)
    cv2.rectangle(img, paddle2.topleft, paddle2.bottomright, (0, 255, 0), thickness=-1, lineType=8, shift=0)

    paddle1 = rect.paddle.update(paddle1, [yavg, 70])
    paddle2 = rect.paddle.update(paddle2, [yavg2, 1000])
    pong = ball.ball.update(pong, paddle1, paddle2)

    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    # #Yellow detector
    # frame_threshed = cv2.inRange(hsv_img, BLUE_MIN, BLUE_MAX)
    # imgray = frame_threshed
    # ret,thresh = cv2.threshold(frame_threshed,127,255,0)
    # contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # # Find the index of the largest contour
    # areas = [cv2.contourArea(c) for c in contours]
    # max_index = np.argmax(areas)
    # cnt=contours[max_index]

    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    if count_defects == 1:
        cv2.putText(img,"Do first action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 2:
        cv2.putText(img, "Do second action", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    elif count_defects == 3:
        cv2.putText(img,"Do third action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"Do fourth action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img,"Welcome to our game!", (50,50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    print(cnt)
    cv2.imshow('Gesture', img)

    # all_img = np.hstack((drawing, crop_imgL))
    # cv2.imshow('Contours', all_img)

    k = cv2.waitKey(10)
    if k == 27:
        break

#code from:  http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
            #https://github.com/iftheqhar/opencv2_python/blob/master/software/firmware/cam.py
            #https://github.com/vipul-sharma20/gesture-opencv/blob/master/gesture.py
            #http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html


#skin color threshholding - find examples of skin color, find ellipse of skin colors