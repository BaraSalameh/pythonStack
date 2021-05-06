#1
#  Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#  Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
#  but whose values are now [-1, "big", "big", -5]
print("Biggie Size")
def biggieSize(ls):
    counter = 0
    for i in ls:
        if i > 0:
            ls[counter] = "big"
        counter += 1
    return ls

newList = biggieSize([-1, 3, 5, -5])
print(newList)
print("")
#2
#  Count Positives - Given a list of numbers, create a function to replace the last 
#  value with the number of positive values. (Note that zero is not considered to be a positive number).
#  Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#  Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
print("Count Positives")
def countPositives(ls):
    positiveCounter = 0
    counter = -1
    for i in ls:
        if i > 0:
            positiveCounter += 1
        counter += 1
    ls[counter] = positiveCounter
    return ls

newList = countPositives([-1,1,1,1])
print(newList)
print("")

#3
#  Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#  Example: sum_total([1,2,3,4]) should return 10
#  Example: sum_total([6,3,-2]) should return 7
print("Sum Total")
def sumTotal(ls):
    sum = 0
    for i in ls:
        sum += i
    return sum
newList = sumTotal([1,2,3,4])
print(newList)
print("")

#4
#  Average - Create a function that takes a list and returns the average of all the values.x
#  Example: average([1,2,3,4]) should return 2.5
print("Average")
def average(ls):
    sum = 0
    counter = 0
    for i in ls:
        sum += i
        counter += 1
    return sum/counter
newList = average([1,2,3,4])
print(newList)
print("")

#5
#  Length - Create a function that takes a list and returns the length of the list.
#  Example: length([37,2,1,-9]) should return 4
#  Example: length([]) should return 0
print("length")
def length(ls):
    counter = 0
    for i in ls:
        counter += 1
    return counter

newList = length([1,2,3,4])
print(newList)
print("")

#6
#  Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
#  If the list is empty, have the function return False.
#  Example: minimum([37,2,1,-9]) should return -9
#  Example: minimum([]) should return False
print("Minimum")
def minimum(ls):
    counter = 0
    min = 0
    for i in ls:
        if i < min:
            min = i
        counter += 1
    if counter == 0:
        return False
    return min
newList = minimum([37,2,1,-9])
print(newList)
print("")

#7
#  Maximum - Create a function that takes a list and returns the maximum value in the list. 
#  If the list is empty, have the function return False.
#  Example: maximum([37,2,1,-9]) should return 37
#  Example: maximum([]) should return False
print("Maximum")
def maximum(ls):
    counter = 0
    max = 0
    for i in ls:
        if i > max:
            max = i
        counter += 1
    if counter == 0:
        return False
    return max
newList = maximum([37,2,1,-9])
print(newList)
print("")

#8
#  Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, 
#  average, minimum, maximum and length of the list.
#  Example: ultimate_analysis([37,2,1,-9]) should return 
#  {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
print("Ultimate Analysis")
def ultimateAnalysis(ls):
    sum =sumTotal(ls) 
    min = minimum(ls)
    max = maximum(ls)
    ln = length(ls)
    avg = average(ls)

    newDictionary = {'sumTotal':sum,'average':avg,'minimum':min,'maximum':max,'length':ln}
    return newDictionary
newDictionary = ultimateAnalysis([37,2,1,-9])
print(newDictionary)
print("")

#9
#  Reverse List - Create a function that takes a list and return that list with values reversed. 
#  Do this without creating a second list. 
#  (This challenge is known to appear during basic technical interviews.)
#  Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
print("Reverse List")
def reverse(ls):
    i = 0
    j = -1
    for k in ls:
        j += 1
    while i < j:
        ls[i] = ls[i] + ls[j] 
        ls[j] = ls[i] - ls[j] 
        ls[i] = ls[i] - ls[j] 
        i += 1
        j -= 1
    return ls
newList = reverse([37,2,1,-9])
print(newList)

