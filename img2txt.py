"""
@author: Viet Nguyen <nhviet1009@gmail.com>
"""
import argparse

import cv2
import numpy as np


mode = "simple"
num_cols = 10000
img_path = "elevation thermo_1_500000.jpg"
out_path = "thermo_1000.txt"



def main(mode,num_cols, img_path, out_path):
    if mode == "simple":
        CHAR_LIST = '@%#*+=-:. '
    else:
        CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    num_chars = len(CHAR_LIST)
    num_cols = num_cols
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    cell_width = width / num_cols
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if num_cols > width or num_rows > height:
        print("Too many columns or rows. Use default setting")
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)

    output_file = open(out_path, 'w')
    for i in range(num_rows):
        print("row "+str(i)+" of: "+str(num_rows))
        for j in range(num_cols):
            output_file.write(
                CHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                          int(j * cell_width):min(int((j + 1) * cell_width),
                                                                  width)]) * num_chars / 255), num_chars - 1)])
        output_file.write("\n")
    output_file.close()


if __name__ == '__main__':
    
    main(mode,num_cols, img_path, out_path)
    print("finished")
