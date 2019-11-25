def numbers_before_letters(l):
    return l.sort(key = lambda x: ([int,str].index(type(x)), x))

print(numbers_before_letters([1,2,3,4,'r',6,'s',8]))