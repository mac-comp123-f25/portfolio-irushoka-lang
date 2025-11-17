from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(pic1,corner_x,corner_y, width, height ):
    new_pic = Picture(width, height)

    for x in range(width):
        for y in range(height):

            original_x = corner_x + x  # Corner_x is the region to crop and x the region we want to remain
            original_y = corner_y + y

            color = pic1.getColor(original_x, original_y)
            new_pic.setColor(x, y, color)


    return new_pic



dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam.show()
dam_crop1.show()
dam_crop2.show()

keep_windows_open()