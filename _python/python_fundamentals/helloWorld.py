# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variablecopy
name = "Noelle"
myName = "Bara Salameh"
print( "Hello ",myName )	# with a comma
print("Hello "+myName)	# with a +
# 3. print "Hello 42!" with the number in a variable
myFavNumber = 7
print("Hello ",myFavNumber)	# with a comma
print("Hello "+ str(myFavNumber))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Mansaf"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f str