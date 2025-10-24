def sum3(values):
    assert type(values) in [list, tuple]
    assert len(values) >= 3
    assert type(values[0]) in [int, float]
    assert type(values[1]) in [int, float]
    assert type(values[2]) in [int, float]

    return (values[0] + values[1] + values[2])



if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) ) # isn't length 3
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )



