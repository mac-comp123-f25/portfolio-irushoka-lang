def smallest_diff(x, y, z):
    """
    Returns the smallest difference between three numbers x, y, and z.
    """
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff

print(smallest_diff(3, 9, 5))      # Expected output: 2
