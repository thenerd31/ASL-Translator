import cv2
import os
import random
import numpy as np
from pathlib import Path

def get_image_size():
    img = cv2.imread('gestures/0/A100.jpg', 0)
    return img.shape
root_dir = Path(__file__).parents[1]
gestures = os.listdir(str(root_dir)+'/gestures/')
gestures.sort(key=int)
image_x, image_y = get_image_size()

full_img = None
for gesture in gestures:
    gesture_dir = os.path.join('gestures', gesture)
    gesture_images = [file for file in os.listdir(gesture_dir) if file.endswith('.jpg')]
    random_image = random.choice(gesture_images) if gesture_images else None

    if random_image is not None:
        img_path = os.path.join(gesture_dir, random_image)
        img = cv2.imread(img_path, 0)
    else:
        img = np.zeros((image_y, image_x), dtype=np.uint8)

    if full_img is None:
        full_img = img
    else:
        full_img = np.hstack((full_img, img))

cv2.imshow("gestures", full_img)
cv2.imwrite('full_img.jpg', full_img)
cv2.waitKey(0)

