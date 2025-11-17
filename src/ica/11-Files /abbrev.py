def print_abbrev(filename):
    file = open(filename , 'r') # Opens the file
    line = file.readline() #Ask it to read a line
    while line: #Create a while loop, do it until there are no more lines tobe read
        print(line[:20])
        line = file.readline()

    file.close()

print_abbrev("../TextFiles/alice.txt")


