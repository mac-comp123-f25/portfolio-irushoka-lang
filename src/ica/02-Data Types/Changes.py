money = 732
dollars = money // 100
rem_dolars = money % 100
quarters = rem_dolars // 25
rem_quarters = rem_dolars % 25
dimes = rem_quarters // 10
rem_dimes = rem_quarters % 10
nickels = rem_dimes // 5
rem_nickels = rem_dimes % 5
pennies = rem_nickels

print(dollars, quarters, dimes, quarters, pennies )


