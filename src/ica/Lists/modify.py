def change_start(value, lst):
    if len(lst) > 0: #The condition
        lst[0] = value

t_list = ['a', 'b', 'c', 'd', 'e', 'f']
change_start('X', t_list)
print(t_list)
