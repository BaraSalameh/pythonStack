#1
#Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).

def countDown(number):
    ls = []
    for i in range(number,0,-1):
        ls.append(i)
    return ls

print(countDown(5))

#2
#  Print and Return - Create a function that will receive a list with two numbers. 
#  Print the first value and return the second.
#  Example: print_and_return([1,2]) should print 1 and return 2
print("")
def printAndReturn(ls):
    print(ls[0])
    return ls[1]
print(printAndReturn([1,2]))

#3
#  First Plus Length - Create a function that accepts a list and returns the sum of the first 
#  value in the list plus the list's length.
#  Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
print("")
def firstPlusLength(ls):
    return ls[0]+len(ls)
ls = firstPlusLength([1,2,3,4,5])
print(ls)

#4
#  Values Greater than Second - Write a function that accepts a list and creates a new list containing 
#  only the values from the original list that are greater than its 2nd value. 
#  Print how many values this is and then return the new list. If the list has less than 2 elements, 
#  have the function return False
#  Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#  Example: values_greater_than_second([3]) should return False
print("")
def valuesGreaterThanSecond(ls):
    if len(ls) < 2:
        return False
    flag = ls[1]
    newList = []
    for i in range(0,len(ls)):
        if ls[i] == 1:
            continue
        if ls[i] > flag:
            newList.append(ls[i])
    print(len(newList))
    return newList
newList = valuesGreaterThanSecond([5,2,3,2,1,4])
print(newList)
anotherList = valuesGreaterThanSecond([3])
print(anotherList)

#5
#  This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
#  The function should create and return a list whose length is equal to the given size, 
#  and whose values are all the given value.
#  Example: length_and_value(4,7) should return [7,7,7,7]
#  Example: length_and_value(6,2) should return [2,2,2,2,2,2]
print("")
def lengthAndValue(size,value):
    newList = []
    for i in range(0,size):
        newList.append(value)
    return newList
newList = lengthAndValue(4,7)
print(newList)
anotherList = lengthAndValue(6,2)
print(anotherList)