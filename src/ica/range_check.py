# x = int(input("Enter a value for x: "))
# y = int(input("Enter a value for y: "))
# if x > y:
#   print(x, y)
# elif y > x:
#   print(y, x)
# else:
#   print(x)


#We want value to be within 1-10 and if not we want them to converge to either 1 or 10.
def range_limit(num: int):
    if num > 1 and num < 10:
        return(num)

    elif num < 1: #This is like a another nested condition into our if statement.
        return(1)

    else:
        return(10)

print(range_limit(5))


if __name__ == "__main__":
  assert range_limit(8) == 8
  assert range_limit(-1) == 1
  assert range_limit(50) == 10
  print("All tests passed!")





