
import math

def rect_area(width, length):
    """
    Compute the area of a rectangle, rounding up width and length to nearest integer.
    """
    width_rounded = math.ceil(width)
    length_rounded = math.ceil(length)
    area = width_rounded * length_rounded
    return area

# --- Helper function to compute roof cost ---
def roof_cost(area, sqf_cost):
    """
    Compute total cost given area and cost per square foot.
    """
    return area * sqf_cost

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

estimate_green_roof(32.8, 54.25, 35)