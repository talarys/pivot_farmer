import cv2
import numpy as np


def find(needle, haystack):
    needle_img = cv2.imread('./images/'+needle+'.png', 0)
    haystack_img = cv2.cvtColor(np.array(haystack), cv2.COLOR_BGR2GRAY)

    r = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(r)

    return max_loc if max_val > 0.8 else -1


def findAll(needle, haystack):
    needle_img = cv2.imread('./images/'+needle+'.png', 0)
    haystack_img = cv2.cvtColor(np.array(haystack), cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    res_h, res_w = res.shape[:2]
    pivots = []
    while max_val >= 0.9:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.9:
            pivots.append(max_loc)

            x1 = max(max_loc[0] - 120//2, 0)
            y1 = max(max_loc[1] - 120//2, 0)

            x2 = min(max_loc[0] + 120//2, res_w)
            y2 = min(max_loc[1] + 120//2, res_h)

            res[y1:y2, x1:x2] = 0

    return pivots if pivots != [] else -1
