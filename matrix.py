import random
def matrix(l):
    c=0
    z=[0]*10
    l[random.choice(l)] = 0
    while l!=z:
        for i in range(1,10):
            if i == random.choice(l) and l[random.choice(l)-1] != 0:
                l[random.choice(l)-1] = 0
                c+=1
            else:
                continue
        if c==9:
            return -1
        
print(matrix([1,2,3,4,5,6,7,8,9]))
