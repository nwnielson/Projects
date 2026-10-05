list = [4,7,2,5,1,9]

def qs (list) :
    if (len(list) <= 1) :
        return list
    p = list[0]
    right = []
    left = []
    for i in list[1:] :
        if(i < p) :
            left.append(i)
        else :
            right.append(i)

    return qs(left) + [p] + qs(right)

print(qs(list))