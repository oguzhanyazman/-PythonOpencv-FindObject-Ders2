import cv2
import numpy as np

farm_img = cv2.imread('main.jpg', cv2.IMREAD_UNCHANGED)
wheat_img = cv2.imread('find.jpg', cv2.IMREAD_UNCHANGED)



### gray option
mainGray = cv2.cvtColor(farm_img, cv2.COLOR_BGR2GRAY)
findobject_gray1 = cv2.cvtColor(wheat_img, cv2.COLOR_BGR2GRAY)



result = cv2.matchTemplate(mainGray, findobject_gray1, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
threshold = .75
yloc, xloc = np.where(result >= threshold)



w = wheat_img.shape[1]
h = wheat_img.shape[0]

cv2.rectangle(farm_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

for (x, y) in zip(xloc, yloc):                  #blue   green  red
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0,0,255), 2)


cv2.imshow('zz', farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

