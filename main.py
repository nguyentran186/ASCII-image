import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."

image_path = "D:\VScode\Python\ML\ASCII image\image.jpg"
directory = "D:\VScode\Python\ML\ASCII image\sub image"

os.chdir(directory)

image = cv2.imread(image_path,0)
height, width = image.shape

def operate(num_col):
    ############### HEIGHT WIDTH
    num_cols = num_col*10
    cell_width = width / num_cols
    cell_height = cell_width * 2
    num_rows = int(height / cell_height)


    # cv2.imshow("IMAGE", image)
    # cv2.waitKey(0)

    #load Image file
    img = Image.new(mode="RGBA", size=(width,height), color='white')
    draw = ImageDraw.Draw(img)
    font=ImageFont.truetype('consola.ttf',int(4000/num_cols))

    for row in range(num_rows):
        for col in range(num_cols):
            sub_image = image[int(row*cell_height): int((row+1)*cell_height), int(col*cell_width): int((col+1)*cell_width)]
            index = int(np.mean(sub_image)/255*len(CHAR_LIST))
            draw.text((col*cell_width,row*cell_height),CHAR_LIST[index],font=font, fill='black')
    img.save("img{}.png".format(num_cols))

for i in range(1,100):
    operate(i)
