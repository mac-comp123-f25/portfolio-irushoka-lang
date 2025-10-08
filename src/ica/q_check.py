
def  has_q (name: str) :
    if  "q" in name:
        result = True
    else:
        result = False

    return result

print(has_q("q"))

if __name__ == "__main__": #Import the function into another file.
  assert has_q("quick") == True #Making sure thatthe function is working
  assert has_q("math") == False
  print("All tests passed!") # If the passed, it will show that all test past. More of an internal test.


