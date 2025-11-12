def has_QOCD(name: str):
    if "Q" in name or "O" in name  or "C" in name or "D" in name:
        result = True
    else:
        result = False

    return result

print(has_QOCD("Quinn"))


if __name__ == "__main__": #Another test
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")



