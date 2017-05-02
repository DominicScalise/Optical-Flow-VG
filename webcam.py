# Matthew Choi, John Marshall, Ellie O'Neil, Dominic Scalise
#
# webcam.py creates a pong game environment primarily using hand detection and skin tone detection.
# The dimensions for this game fit the screen of a 13-inch Macbook.

import cv2
import numpy as np
import math
import ball
import rect
import datetime

cap = cv2.VideoCapture(0)

pong = ball.ball(100,100, 20)

# Star game, set scores for both players to 0, and create the paddles for each player.
start = True
scoreL = 0
scoreR = 0
center = [55, 350]
center2 = [1223, 350]
paddle1 = rect.paddle(center, h = 130, w = 100)
paddle2 = rect.paddle(center2, h = 130, w = 100)

# Open camera for game
while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img,1)

    # Create rectangle for hand detection region
    # Also create pong ball using ball.py class
    crop_imgL = img[100:300, 520:720]
    cv2.circle(img, (pong.ypos, pong.xpos), 10, (250, 250, 250), thickness=20)

    # Set up hand detection algorithm by setting image to grayscale and blurring it with Gaussian
    # to remove noise
    grey = cv2.cvtColor(crop_imgL, cv2.COLOR_BGR2GRAY)
    
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Main body of hand detection algorithm. Find the contours and convexities in the image and
    # count the defects found at the given frame.
    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
           cv2.CHAIN_APPROX_NONE)
    
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_imgL,(x,y),(x+w,y+h),(0,0,255),0)
    # cv2.rectangle(crop_imgL,(0,20),(0,700),(0,0,255),0)
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
        otherStart = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - otherStart[0])**2 + (end[1] - otherStart[1])**2)
        b = math.sqrt((far[0] - otherStart[0])**2 + (far[1] - otherStart[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_imgL,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_imgL,otherStart,end,[0,255,0],2)
        #cv2.circle(crop_imgL,far,5,[0,0,255],-1)

    #Start the game
    if start:
        pong.xvol = 0
        pong.yvol = 0
        pong.xpos = 100
        pong.ypos = 100
        start2 = False

    # If there are two or more defects in the hand detection region (aka if there are more than one fingers)
    # then start the clock for the game
    if count_defects >= 2:
        timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=4)
        timer_3 = datetime.datetime.utcnow() + datetime.timedelta(seconds=3)
        timer_2 = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
        timer_1 = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        start = False
        start2 = True

    # Begin the countdown and start the game when it finishes
    if start2:
        if datetime.datetime.utcnow() > timer_stop:
            pong = pong.start()
            start2 = False
        elif datetime.datetime.utcnow() > timer_3:
            cv2.putText(img, 'GO!', (590, 240), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 0, 0), thickness=10)
        elif datetime.datetime.utcnow() > timer_2:
            cv2.putText(img, '1', (590, 240), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(0, 255, 255), thickness=10)
        elif datetime.datetime.utcnow() > timer_1:
            cv2.putText(img, '2', (590, 240), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(255, 0, 0), thickness=10)
        else:
            cv2.putText(img, '3', (590, 240), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(0, 255, 255), thickness=10)


    # Find color thresholds for skin tone detection
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
    # areas = [cv2.contourArea(c) for c in contours]
    # max_index = np.argmax(areas)
    # cnt=contours[max_index]

    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    # Algorithm that finds how many pixels per row are skin tone pixels. It then compares this to a 60%
    # threshold and if the given row is more than the threshold then it is used for moving the paddle.
    #(make variables here for height and width)
    count2 = 0;
    yavg = 0;
    for y in range(0, 720):
        count = 0;
        count = np.sum(frame_threshed[y,:100] != 0)
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
        count = np.sum(frame_threshed[y,1123:1223] != 0)
        if count >= 60:
            yavg2 += y
            count2 += 1

    if count2 != 0:
        yavg2 = yavg2/count2
    else: yavg2 = paddle2.center[1]

    # Updates the dimensions of the paddles
    vertexL1 = (int(paddle1.topleft[0]), int(paddle1.topleft[1]))
    vertexL2 = (int(paddle1.bottomright[0]), int(paddle1.bottomright[1]))
    vertexR1 = (int(paddle2.topleft[0]), int(paddle2.topleft[1]))
    vertexR2 = (int(paddle2.bottomright[0]), int(paddle2.bottomright[1]))

    cv2.rectangle(img, vertexL1, vertexL2, (0, 0, 255), thickness= -1, lineType=8, shift=0)
    cv2.rectangle(img, vertexR1, vertexR2, (0, 0, 255), thickness= -1, lineType=8, shift=0)

    paddle1 = rect.paddle.update(paddle1, [55, yavg])
    paddle2 = rect.paddle.update(paddle2, [1223, yavg2])
    pong, L, R = ball.ball.update(pong, paddle1, paddle2)

    # Updates the scores
    scoreL += L
    scoreR += R
    if(R or L > 0): start = True

    # Posts the scores on the screen
    cv2.putText(img, 'Score: ' + str(scoreL), (0, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(255, 0, 0), thickness=3)
    cv2.putText(img, 'Score: ' + str(scoreR), (1123, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 255, 255), thickness=5)
    cv2.imshow('Gesture', img)

    #cv2.putText(img, 'To end game, press command-Q', (0, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #            color=(0, 255, 255), thickness=2)


    # End game by pressing the escape key
    k = cv2.waitKey(10)
    if k == 27:
        break


#smoothing over time