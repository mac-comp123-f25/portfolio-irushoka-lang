str_seconds = input("Please enter number of seconds here =")
total_seconds = int(str_seconds)

hours = total_seconds // 3600
seconds_still_remaining = total_seconds % 3600
min = seconds_still_remaining // 60
seconds_finally_remaining = seconds_still_remaining % 60

print ("Hrs =", hours, "mins=", min, "seconds=", seconds_finally_remaining)

