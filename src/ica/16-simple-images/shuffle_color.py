from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def negative(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = ( r -250 + g-250 +  b - 250)/3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

image = Picture("../SampleImages/antiqueTractors.jpg")

new_image = negative(image)

new_image.show ()
keep_windows_open()