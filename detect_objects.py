import cv2
import numpy as np


def detect_count_objects(st_image):
    """This function detects and counts the objects

    :st_image: image uploaded using streamlit
    :returns: num_objects (int): number of detected objects
              image (opencv image): resulting image

    """
    # Defining the color ranges to be filtered.
    # The following ranges should be used on HSV domain image.
    low_apple_red = (160.0, 153.0, 153.0)
    high_apple_red = (180.0, 255.0, 255.0)
    low_apple_raw = (0.0, 150.0, 150.0)
    high_apple_raw = (15.0, 255.0, 255.0)

    file_bytes = np.asarray(bytearray(st_image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    image = opencv_image.copy()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask_red = cv2.inRange(image_hsv, low_apple_red, high_apple_red)
    mask_raw = cv2.inRange(image_hsv, low_apple_raw, high_apple_raw)

    mask = mask_red + mask_raw

    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
    c_num = 0
    for i, c in enumerate(cnts):
        # draw a circle enclosing the object
        ((x, y), r) = cv2.minEnclosingCircle(c)
        if r > 34:
            c_num += 1
            cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
            cv2.putText(image, "#{}".format(c_num), (int(x) - 10, int(y)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        else:
            continue
    # convert opencv bgr to rgb
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return c_num, image
