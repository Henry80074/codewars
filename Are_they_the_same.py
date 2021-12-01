def comp(array1, array2):
    
    square = []
    if array1 == None or array2 == None:
        return False
    if len(array1) != len(array2):
        return False
    for a in array1:
        square.append(a**2)
    array2.sort()
    square.sort()
    if array2 == square:
        return True
    else:
        return False
