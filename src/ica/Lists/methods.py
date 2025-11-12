def end_points(numbers):
    return (min(numbers), max(numbers))


a_list = [1,2,3,4]

print(end_points(a_list))


#test_1
points = end_points(a_list)
print(points[0], points[1])


# --- Test call 2: unpack the tuple into two separate variables ---
(x, y) = end_points(a_list)
print(x, "and", y)
