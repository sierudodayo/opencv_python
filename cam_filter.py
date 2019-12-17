import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)


print("noise_val?")

noise_count = int(input())


while True:
    ret, frame = cap.read()
    
    frame_gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
    frame_noise = frame_gray

    height, width = frame_noise.shape

    coun_h = int(0)
    coun_w = int(0)
    
    for i in range( 0, int(noise_count)):
        noiseX = random.randint(1,int(width)-1)
        noiseY = random.randint(1,int(height)-1)

        if i % 2 == 0:
            frame_noise[noiseY,noiseX] = 255;
        else:
            frame_noise[noiseY,noiseX] = 0;


    cv2.imshow("frame_in", frame)
    cv2.imshow("frame_gray",frame_gray)
    cv2.imshow("frame_noise", frame_noise)

    frame_ave3 = cv2.blur( frame_gray, ( 3, 3))
    frame_ave5 = cv2.blur( frame_gray, ( 5, 5))
    frame_gau3 = cv2.GaussianBlur( frame_gray, ( 3, 3), 1)
    frame_gau9 = cv2.GaussianBlur( frame_gray, ( 9, 9), 3)
    frame_median = cv2.medianBlur( frame_gray, 3)

    cv2.imshow("frame_ave3", frame_ave3)
    cv2.imshow("frame_ave5", frame_ave5)
    cv2.imshow("frame_gau3", frame_gau3)
    cv2.imshow("frame_gau9", frame_gau9)
    cv2.imshow("frame_median", frame_median)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
