#Hi

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

video = []

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video.append(gray)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    hand, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(frame.shape, np.uint8)

    max_area = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if (area > max_area):
            max_area = area
            ci = i
    cnt = contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)

    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])  # cx = M10/M00
        cy = int(moments['m01'] / moments['m00'])  # cy = M01/M00

    centr = (cx, cy)
    cv2.circle(frame, centr, 5, [0, 0, 255], 2)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 2)

    x, y, w, h = cv2.boundingRect(cnt)
    crop_img = frame[100:300, 100:300]
    cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 0)

    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape, np.uint8)
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

    cnt = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    hull = cv2.convexHull(cnt, returnPoints=False)

    if (1):
        defects = cv2.convexityDefects(cnt, hull)
        mind = 0
        maxd = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            dist = cv2.pointPolygonTest(cnt, centr, True)
            cv2.line(frame, start, end, [0, 255, 0], 2)

            cv2.circle(frame, far, 5, [0, 0, 255], -1)
        print(i)
        i = 0


    cv2.imshow('output', drawing)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#code from:  http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
            #https://github.com/iftheqhar/opencv2_python/blob/master/software/firmware/cam.py
            #https://github.com/vipul-sharma20/gesture-opencv/blob/master/gesture.py


