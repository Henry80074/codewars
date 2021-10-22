
def flatten_and_sort(array):
    list = []
    for l in array:
        for i in l:
            list.append(i)
    return sorted(list)
       
