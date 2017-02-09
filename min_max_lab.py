def min (list1):
    list1 =iter(list1)
    min = list1.next()
    for i in list1:
        if i < min:
           min = i
    return min
def max(list1):
    list1 = iter (list1)
    max = list1.next()
    for i in list1:
        if i > max:
           max = i
    return max
def find_max_min(list1):
    new_list= []
    if (len(set(list1)) <=1):
        new_list.append(len(list1))
        return new_list
    else:
        return[min(list1), max(list1)]









