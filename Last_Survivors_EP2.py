def last_survivors(string):
    array = [x for x in string]
    
    while len(array) != len(set(array)):
        for c in array:
            num = array.count(c)
            if num % 2 == 0 or num >=3:
                if c != "z":
                    array.append(chr(ord(c)+1))
                else:
                    array.append("a")
                array.remove(c)
                array.remove(c)
    string = ''.join(c for c in array)
    return(string)
