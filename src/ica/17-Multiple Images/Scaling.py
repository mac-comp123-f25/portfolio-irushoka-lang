from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def scale_down(image):

    width = image.getWidth()
    height = image.getHeight()

    new_width = (width) // 2
    new_height = (height) // 2

    new_pic = Picture(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):

            scaled_pixel_x = x * 2
            scaled_pixel_y = y * 2

            color = image.getColor(scaled_pixel_x, scaled_pixel_y)
            new_pic.setColor(x, y, color)

    return new_pic




dam = Picture("../SampleImages/hooverDam.jpg")
dam_scaled_down = scale_down(dam)
dam_scaled_down.show()
dam.show()
keep_windows_open()