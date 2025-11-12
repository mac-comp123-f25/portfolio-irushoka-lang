from src.ica.helpers.imageTools import *

def weighted_scale(pic,w1, w2, w3):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (w1*r + w2*g + w3*b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

weighted_scale(antiqueTractors.jpg ,2, 2, 2)