import random 

def Rand(start, end, num): 
    res = [random.randint(start, end) for j in range(num)]
    return res 

print(Rand(0,10,20))