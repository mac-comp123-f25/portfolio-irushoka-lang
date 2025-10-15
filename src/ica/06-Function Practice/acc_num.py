def sum_range(start_val, end_val):
    cnt = 0     # initialize accumulator to default value 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x     # update: add new x value to old value of cnt
    return cnt

print(sum_range(3,4)) #Adds all the values in the range
print(sum_range(-10,-10)) #Gives us the same
print(sum_range(28,23))#Gives us zero
print(sum_range(-100,-100)) #Same value

