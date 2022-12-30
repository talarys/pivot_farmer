import cv2
import numpy as np


def findAll(template, image):
    template = cv2.imread(template, 0)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    threshold = 0.8
    matches = []

    while True:
        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > threshold:
            matches.append(max_loc)

            h, w = template.shape[:2]

            mask = np.zeros((h, w))
            image[max_loc[1]:max_loc[1]+mask.shape[1],
                  max_loc[0]: max_loc[0]+mask.shape[0]] = 0
        else:
            break

    return matches if matches != [] else -1


def find(template, image):
    template = cv2.imread(template, 0)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    r = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(r)

    return max_loc if max_val > 0.8 else -1
