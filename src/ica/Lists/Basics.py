def every_other(list1):
    list2=[]
    for i in range(0,len(list1),2):
        list2.append(list1[i])
    return list2


# print(every_other([1,2,3,4,5,6]))


def sum_positive(list1):
    total_sum = 0

    for i in range(0,len(list1)):#For all values of the list 1
        if list1[i] > 0  :
           total_sum = total_sum + list1[i]
            #total += list1[i]

    return total_sum

print(sum_positive([-1,-2,-3,-4,5,6]))




