def add_tax(price, tax_rate):
    tax_amt = price * tax_rate
    return price + tax_amt

add_tax(25.99, 0.0725)
print(add_tax(25.99, 0.0725))