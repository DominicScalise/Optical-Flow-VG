import cv2
import numpy as np
import math
import ball
import rect
import datetime

cap = cv2.VideoCapture(0)

pong = ball.ball(420, 620, 10)

start = True
scoreL = 0
scoreR = 0

center = [55, 350]
center2 = [1223, 350]
paddle1 = rect.paddle(center, h = 160, w = 80)
paddle2 = rect.paddle(center2, h = 160, w = 80)

while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img,1)
    #cv2.rectangle(img,(120,20),(0,700),(0,255,0),0)
    #crop_imgL = img[20:700, 0:120]
    #cv2.rectangle(img,(1158,20),(1278,700),(0,255,0),0)
    #crop_imgR = img[20:700, 1158:1278]
    cv2.circle(img, (pong.ypos, pong.xpos), 10, (250, 250, 250), thickness=20)

    if start:
        pong.xvol = 0
        pong.yvol = 0
        pong.xpos = 420
        pong.ypos = 620
        timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)
        timer_3 = datetime.datetime.utcnow() + datetime.timedelta(seconds=3)
        timer_2 = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
        timer_1 = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        start = False
        start2 = True
    if start2:
        if datetime.datetime.utcnow() > timer_stop:
            pong = pong.start()
            start2 = False
        elif datetime.datetime.utcnow() > timer_3:
            cv2.putText(img, 'GO!', (620, 620), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 255, 255), thickness=10)
        elif datetime.datetime.utcnow() > timer_2:
            cv2.putText(img, '1', (620, 620), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 255, 255), thickness=10)
        elif datetime.datetime.utcnow() > timer_1:
            cv2.putText(img, '2', (620, 620), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 255, 255), thickness=10)
        else:
            cv2.putText(img, '3', (620, 620), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 255, 255), thickness=10)




    # #LEFT
    # grey = cv2.cvtColor(crop_imgL, cv2.COLOR_BGR2GRAY)
    # # grey2 = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)
    #
    # value = (35, 35)
    # blurred = cv2.GaussianBlur(grey, value, 0)
    # _, thresh1 = cv2.threshold(blurred, 127, 255,
    #                            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #
    # contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
    #        cv2.CHAIN_APPROX_NONE)
    #
    # cnt = max(contours, key = lambda x: cv2.contourArea(x))
    #
    # x,y,w,h = cv2.boundingRect(cnt)
    # #cv2.rectangle(crop_imgL,(x,y),(x+w,y+h),(0,0,255),0)
    # cv2.rectangle(crop_imgL,(0,20),(0,700),(0,0,255),0)
    # hull = cv2.convexHull(cnt)
    # drawing = np.zeros(crop_imgL.shape,np.uint8)
    # cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    # cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    # hull = cv2.convexHull(cnt,returnPoints = False)
    # defects = cv2.convexityDefects(cnt,hull)
    # count_defects = 0
    # cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    # for i in range(defects.shape[0]):
    #     s,e,f,d = defects[i,0]
    #     start = tuple(cnt[s][0])
    #     end = tuple(cnt[e][0])
    #     far = tuple(cnt[f][0])
    #     a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    #     b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    #     c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    #     angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
    #     if angle <= 90:
    #         count_defects += 1
    #         cv2.circle(crop_imgL,far,1,[0,0,255],-1)
    #     #dist = cv2.pointPolygonTest(cnt,far,True)
    #     cv2.line(crop_imgL,start,end,[0,255,0],2)
    #     #cv2.circle(crop_imgL,far,5,[0,0,255],-1)
    #
    #
    # # RIGHT
    # grey = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)
    #     # grey2 = cv2.cvtColor(crop_imgR, cv2.COLOR_BGR2GRAY)
    # value = (35, 35)
    # blurred = cv2.GaussianBlur(grey, value, 0)
    # _, thresh1 = cv2.threshold(blurred, 127, 255,
    #                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #
    # contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
    #            cv2.CHAIN_APPROX_NONE)
    #
    # cnt = max(contours, key = lambda x: cv2.contourArea(x))
    #
    #
    # x,y,w,h = cv2.boundingRect(cnt)
    # #cv2.rectangle(crop_imgL,(x,y),(x+w,y+h),(0,0,255),0)
    # cv2.rectangle(crop_imgR,(0,20),(0,700),(0,0,255),0)
    # hull = cv2.convexHull(cnt)
    # drawing = np.zeros(crop_imgR.shape,np.uint8)
    #
    #
    # cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    # cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    # hull = cv2.convexHull(cnt,returnPoints = False)
    # hull2 = cv2.convexHull(cnt, returnPoints = True)
    # defects = cv2.convexityDefects(cnt,hull)
    # count_defects = 0
    # cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    # for i in range(defects.shape[0]):
    #     s,e,f,d = defects[i,0]
    #     start = tuple(cnt[s][0])
    #     end = tuple(cnt[e][0])
    #     far = tuple(cnt[f][0])
    #     a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    #     b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    #     c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    #     angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
    #     if angle <= 90:
    #         count_defects += 1
    #
    #         cv2.circle(crop_imgR,far,1,[0,0,255],-1)
    #     #dist = cv2.pointPolygonTest(cnt,far,True)
    #     cv2.line(crop_imgR,start,end,[0,255,0],2)
    #     #cv2.circle(crop_imgL,far,5,[0,0,255],-1)
    #
    #
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    YELLOW_MIN = np.array([20, 80, 80],np.uint8)
    YELLOW_MAX = np.array([40, 255, 255],np.uint8)
    BLUE_MIN = np.array([110,50,50],np.uint8)
    BLUE_MAX = np.array([130,255,255],np.uint8)
    SKINTONE_MIN = np.array([0,48,80],np.uint8)
    SKINTONE_MAX = np.array([20,255,255],np.uint8)

    # #
    #Skin tone detector
    frame_threshed = cv2.inRange(hsv_img, SKINTONE_MIN, SKINTONE_MAX)
    imgray = frame_threshed
    ret,thresh = cv2.threshold(frame_threshed,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Find the index of the largest contour
    # areas = [cv2.contourArea(c) for c in contours]
    # max_index = np.argmax(areas)
    # cnt=contours[max_index]

    count2 = 0;
    yavg = 0;
    for y in range(0, 720):
        count = 0;
        for x in range(0, 100):
            if(frame_threshed[y][x] != 0): count += 1
        if count >= 60:
            yavg += y
            count2 += 1

    if count2 != 0:
        yavg = yavg/count2
    else: yavg = paddle1.center[1]



    count2 = 0;
    yavg2 = 0;
    for y in range(0, 720):
        count = 0;
        for x in range(1123, 1223):
            if (frame_threshed[y][x] != 0): count += 1
        if count >= 60:
            yavg2 += y
            count2 += 1

    if count2 != 0:
        yavg2 = yavg2/count2
    else: yavg2 = paddle2.center[1]

    vertexL1 = (int(paddle1.topleft[0]), int(paddle1.topleft[1]))
    vertexL2 = (int(paddle1.bottomright[0]), int(paddle1.bottomright[1]))
    vertexR1 = (int(paddle2.topleft[0]), int(paddle2.topleft[1]))
    vertexR2 = (int(paddle2.bottomright[0]), int(paddle2.bottomright[1]))

    cv2.rectangle(img, vertexL1, vertexL2, (255, 0, 0), thickness= -1, lineType=8, shift=0)
    cv2.rectangle(img, vertexR1, vertexR2, (0, 0, 255), thickness= -1, lineType=8, shift=0)


    paddle1 = rect.paddle.update(paddle1, [55, yavg])
    paddle2 = rect.paddle.update(paddle2, [1223, yavg2])
    pong, L, R = ball.ball.update(pong, paddle1, paddle2)

    scoreL += L
    scoreR += R
    if(R or L > 0): start = True




    #make region size of rectangle
    #decide if it's a skin pixel or not - done (kinda)
    #set a threshold for each row of how many skin colored pixels
    #use all rows that pass the threshold test


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


    # if count_defects == 1:
    #     cv2.putText(img,"Do first action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    # elif count_defects == 2:
    #     cv2.putText(img, "Do second action", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    # elif count_defects == 3:
    #     cv2.putText(img,"Do third action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    # elif count_defects == 4:
    #     cv2.putText(img,"Do fourth action", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    # else:
    #     cv2.putText(img,"Welcome to our game!", (50,50),\
    #                 cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    # # cv2.imshow('Gesture', frame_threshed)

    cv2.putText(img, 'Score: ' + str(scoreL), (0, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(255, 0, 0), thickness=3)
    cv2.putText(img, 'Score: ' + str(scoreR), (1123, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 0, 255), thickness=5)
    cv2.imshow('Optical Pong', img)

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