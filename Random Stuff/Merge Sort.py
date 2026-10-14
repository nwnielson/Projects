list = [4,7,2,5,1,9]

def merge_sort(list) :
    m = len(list) // 2
    if (len(list) <= 1) :
        return list
    a = merge_sort(list[:m])
    b = merge_sort(list[m:])
    r = []
    while a and b :
        if a <= b :
            r.append(a.pop(0))
        else :
            r.append(b.pop(0))
    return r + a + b

print(merge_sort(list))