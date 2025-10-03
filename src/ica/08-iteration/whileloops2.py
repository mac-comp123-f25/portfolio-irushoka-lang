def print_every_fifth(x):
  while x >= 0:  # x is the loop variable
    print(x)
    x = x - 5
  # when indentation stops, while loop is over
  print("Done!")

#print_every_fifth(11)

def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ")
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)

# square_user_nums()


def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # the loop variable
    total = 0  # the accumulator variable
    while curr_val < topNum:
        total = total + curr_val  # add next value to accumulator
        curr_val = curr_val + 1  # update the loop variable
        print(curr_val)
        print(total)

    return total

print(sum_to_n(6))


def add_user_nums():
    sum_of_nums = 0
    user_inp = input("Enter a next number: ")
    user_num = int(user_inp)

    while user_num != 0:
       sum_of_nums = sum_of_nums + user_num
       user_inp = input("Enter a next number: ")
       user_num = int(user_inp)

    return sum_of_nums

print(add_user_nums())