def copy_str(string, name, num_times):
    ans_str =  ""    # initialize accumulator to empty string
    for x in range(num_times):
        ans_str = ans_str + string + name    # update ans_str, by using the function within the efinition, this is an accumulator variable
        #Where we use a function within a function
    return ans_str

print(copy_str("Hello ",  "Kampe ",  4))

