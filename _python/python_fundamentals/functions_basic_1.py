#1
def a():
    return 5
print(a()) # calling the function a wich returns 5 then printing 5 as a final output.

print("")
#2
def a():
    return 5
print(a()+a()) #  the print statement calls the function twise, in each call it adds the returned numbers
               #  wich is 5 + 5 and for the final output its 10.
print("")

#3
def a():
    return 5
    return 10
print(a()) #  the print statement calls the function once, and the function returns the first return
           #  statement only which is 5 as a final output for the print.
print("")

#4
def a():
    return 5
    print(10)
print(a())  #  it's like the 3rd question wich returns the first return statement and exit the function
            #  and prints the f as a final output in the print.
print("")

#5
def a():
    print(5)
x = a()  #this line calls the function wich print 5 only.
print(x)  #for this line i think it prints an empty value or a random one or an error because the function
          #didn't return any value to store it in x.

print("")
#6

#def a(b,c):
 #   print(b+c)
#print(a(1,2) + a(2,3))  #  the print statement calls the function with different values each time,      
                        #  i think the output would be as the result for the first call only wich is 3,
                        #  beacause the second print statement will give an error cause of nothing returned
                        #  as a first or second parameter.
#print("")
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))  #  the output would be 25 as a result for concatination of b and c, they are an string now
print("")

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#  the first output would be the result of printing line 56 wich is 100.
#  then the function will go to the else statement in line 59 and return 10.
#  at the end the print statement at line 62 will print the returned value wich is 10
#  so the final output would be 100  10
print("")

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))  #  this call to the function will return 7 to be printed.
print(a(5,3))  #  this call will return 14 to be printed.
print(a(2,3) + a(5,3))  #  this two calls for the function will return 7 as the first parameter
                        #  and 14 as the second one, The print statement will sum the returned 
                        #  numbers 7 + 14 and print the summation -> 21
print("")

#10
def a(b,c):
    return b+c  #  this line will return the summation of 3 and 5 -> 8
    return 10  #  this line is unreachable cause of the first return statement.
print(a(3,5))  #  this line will print the returned answer wich is 8
print("")

#11
b = 500
print(b) #  variable b will be printed -> 500
def a():
    b = 300
    print(b)
print(b)  #  the global variable b will be printed again -> 500
a()  #  this line will call the function wich will print the local variable b -> 300
print(b)  #  the global variable b will be printed for the third time -> 500
          #  so the final output will be like 500 , 500 , 300 , 500
print("")

#12
b = 500  
print(b)  #  variable b will be printed -> 500
def a():
    b = 300
    print(b)  
    return b
print(b)  #  variable b will be printed again -> 500
a()  #  this line will call the function wich will print the local variable b -> 300 and return the value
print(b)  #  variable b will be printed for the third time -> 500
          #  so the final output will be like 500 , 500 , 300 , 500
print("")

#13
b = 500  
print(b)  #  variable b will be printed -> 500
def a():
    b = 300
    print(b)
    return b
print(b)  #  variable b will be printed again -> 500
b=a()  #  this line will call the function wich will print local b -> 300, return it and store it in b
print(b)  #  this line will print the saved local variable in b -> 300
          #  so the final output will be like 500 , 500 , 300 , 300
print("")

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()  #  this line will call function a wich will print the number 1 and then the a function will call
     #  function b wich will print the number 3, and goes back to function a that will print the number 2
     #  so as a final output will be 1 , 3 , 2
print("")

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# for line 150, the function a will be called and prints the number 1, then variable x will store the 
#  the returned value from function b wich will print the number 3 and return the number 5.
#  then the value stored on variable x weill be printed wich is 5, in the last line in function a it
#  will return number 10 to be stored in variable y, and for the last line (151) it will print 10.
#  so the final output would be like 1 , 3 , 5 , 10





