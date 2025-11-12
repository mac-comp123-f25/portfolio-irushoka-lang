from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def weighted_scale(pic,w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (w1*r + w2*g + w3*b)/3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

image = Picture("../SampleImages/antiqueTractors.jpg") #To upload an image you do, double dots... and then the working directory
image.show()

new_image = weighted_scale(image,0.8, 0.1, 0.1)
new_image.show()
# weighted_scale(image,2, 2, 2)

keep_windows_open()