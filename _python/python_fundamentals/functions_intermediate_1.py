import random

def randInt(min = 0 , max = 100):
    if min > max:
        min = min + max
        max = min - max
        min = min - max
    num = random.randint(min,max)
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))


print(randInt(3,-1))