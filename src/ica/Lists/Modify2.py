
def remove_all (value, list):
    if value in list:

        list.remove(value)
        return list
p_list  =  ['a', 'b', 'c', 'd', 'e', 'f']
remove_all('a', p_list)

print(p_list)