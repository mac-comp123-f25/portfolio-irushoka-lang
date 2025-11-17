from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x, y) in small_pic:
        color = small_pic.getColor(x, y)
        new_location_x = start_x + x
        new_location_y = start_y + y
        big_pic.setColor(new_location_x, new_location_y, color)

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()


keep_windows_open()


