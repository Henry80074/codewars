def create_phone_number(n):
    check = all(isinstance(item, int) for item in n)
    if len(n) == 10 and check:
        first = n[0:3]
        second = n[3:6]
        third = n[6:10]
        string = "({}) {}-{}".format("".join(str(i) for i in first), 
                                     "".join(str(i) for i in second),
                                     "".join(str(i) for i in third))
    else:
        return("error")
    return string
   
