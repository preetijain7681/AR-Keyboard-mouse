import cv2
import numpy as np

img = cv2.imread("key.jpg",cv2.IMREAD_UNCHANGED)
dimensions = img.shape
height= img.shape[0]
width= img.shape[1]
def get_keys():
    """

    this function is used to design the keyboard.

    it returns the 4 parameter that are needed to design the keys.

    they are key label, top right corner coordinate, bottom left corner coordinate, and center coordinate

    """

    max_keys_in_a_row = 11  # max number of keys in any row is 10 i.e the first row which contains 1234567890'backspace'


    key_width = int(
        width / max_keys_in_a_row)  # width of one key. width is divided by 10 as the max number of keys in a single row is 11.

    row0_key_width = key_width * 11  # width of zeroth or numeric row of keys

    row1_key_width = key_width * 10  # width of first row

    row2_key_width = key_width * 9  # width of second row

    row3_key_width = key_width * 7  # width of third row

    row4_key_width = key_width * 5  # width of space

    row_keys = []  # stores the keys along with its 2 corner coordinates and the center coordinate

    # for the zeroth row

    x1, y1 = 0, int((
                                height - key_width * 5) / 2)  # 5 is due to the fact that we will have 5 rows. y1 is set such that the whole keyboard has equal margin on both top and bottom

    x2, y2 = key_width + x1, key_width + y1

    c1, c2 = x1, y1  # copying x1, x2, y1 and y2

    keys = "1 2 3 4 5 6 7 8 9 0 <-"

    keys = keys.split(" ")

    for key in keys:

        if key == "<-":

            row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 25, int((y2 + y1) / 2) + 10)])

        else:

            row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 5, int((y2 + y1) / 2) + 10)])

        x1 += key_width

        x2 += key_width

    x1, y1 = c1, c2  # copying back from c1, c2, c3 and c4

    # for the first row

    x1, y1 = int((row0_key_width - row1_key_width) / 2) + x1, y1 + key_width

    x2, y2 = key_width + x1, key_width + y1

    c1, c2 = x1, y1  # copying x1, x2, y1 and y2

    keys = "qwertyuiop"

    for key in keys:
        row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 5, int((y2 + y1) / 2) + 10)])

        x1 += key_width

        x2 += key_width

    x1, y1 = c1, c2  # copying back from c1, c2, c3 and c4

    # for second row

    x1, y1 = int((
                             row1_key_width - row2_key_width) / 2) + x1, y1 + key_width  # x1 is set such that it leaves equal margin on both left and right side

    x2, y2 = key_width + x1, key_width + y1

    c1, c2 = x1, y1

    keys = "asdfghjkl"

    for key in keys:
        row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 5, int((y2 + y1) / 2) + 10)])

        x1 += key_width

        x2 += key_width

    x1, y1 = c1, c2

    # for third row

    x1, y1 = int((row2_key_width - row3_key_width) / 2) + x1, y1 + key_width

    x2, y2 = key_width + x1, key_width + y1

    c1, c2 = x1, y1

    keys = "zxcvbnm"

    for key in keys:
        row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 5, int((y2 + y1) / 2) + 10)])

        x1 += key_width

        x2 += key_width

    x1, y1 = c1, c2

    # for the space bar

    x1, y1 = int((row3_key_width - row4_key_width) / 2) + x1, y1 + key_width

    x2, y2 = 5 * key_width + x1, key_width + y1

    c1, c2 = x1, y1

    keys = " "

    for key in keys:
        row_keys.append([key, (x1, y1), (x2, y2), (int((x2 + x1) / 2) - 5, int((y2 + y1) / 2) + 10)])

        x1 += key_width

        x2 += key_width

    x1, y1 = c1, c2

    return row_keys


priti= get_keys()
print(priti)
for key in priti:
    cv2.putText(img, key[0], key[3], cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))

    cv2.rectangle(img, key[1], key[2], (0, 255, 0), thickness=2)


def do_keypress(img, center, row_keys_points):
    # this fuction presses a key and marks the pressed key with blue color

    for row in row_keys_points:

        arr1 = list(np.int0(np.array(center) >= np.array(
            row[1])))  # center of the contour has greater value than the top left corner point of a key

        arr2 = list(np.int0(np.array(center) <= np.array(
            row[2])))  # center of the contour has less value than the bottom right corner point of a key

        if arr1 == [1, 1] and arr2 == [1, 1]:

            if row[0] == '<-':

                gui.press('backspace')

            else:

                gui.press(row[0])

            cv2.fillConvexPoly(img, np.array([np.array(row[1]), \
 \
                                              np.array([row[1][0], row[2][1]]), \
 \
                                              np.array(row[2]), \
 \
                                              np.array([row[2][0], row[1][1]])]), \
 \
                               (255, 0, 0))

    return img

img=do_keypress(img,,priti)
cv2.imshow('img',img)
cv2.waitKey(0)