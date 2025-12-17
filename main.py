a = 10  # int variable: "int means - Integer"
# We can put into this variable just number like"1,2,3..."

b = "10"  # it's string variable can contain symbol ("") or ('') which say Inteprеter,
# "hay I have string" but this variable cannot be (10, asdasd, 123) without (""), ('').

c = 10.5  # this is the float variable. Float is the desemal nomber like 1.2 ...

# Python it's language where we don't need write what type of variable you need,
# but we can transformate integer into string or float

# example:

# variable a = 10 it's integer. We can convert into str - String
d = str(a)


# it is just note for which variable we cheking
print("variable: a")

# it is just for understandeble what type of variable do we have
print(type(a))

# it is just note for which variable we cheking
print("variable: d")

# it is just for understandeble what type of variable do we have
print(type(d))

# _________________________________________________________________________________________________
#                               lists

# This is the list of number
List = [1, 2, 3]

# list it's like variable but that can conteinnig not just number.
# We can put into the list: number - integer , string, float and another list

List = [1, "1", 1.2]

# We can add or remove items

# here We are add item.
List.append("1")
print(List)

# here We are remove by name of item.
List.remove("1")
print(List)

# here We are remove by index.
List.pop(0)

# print(variable, string, int ...) - this is function for print something in consol
print(List)


# note of conting a list:
# list always starts with zero
# so its will be like List = [0,1,2] if we have for example
# List = [1,2,3]
# ////////^
# ////////this is 0 index and than it graded to 1. So in list List "1 - it will be 0 index", "2 - it will be 1 index"
# , and "3 - it will be 2 index"


# _________________________________________________________________________________________________
#                                   dictionary

my_dictionary = {}  # this is a dictionary. "{}" say for python what that means a dictionary, so if we have for example variable
# "number_of_phone = {}". So that mean a dictionary.
# dictionary "my_dictionary" can contain key word and value for example:

my_dictionary = {"Dima": "19 years old"}

# print all dictionary
print(my_dictionary)

# now we print just value
print(my_dictionary["Dima"])
# in [] we can put what do you want to know about these key word.


# change value in the dictionary
my_dictionary["Dima"] = "20 years old"
print(my_dictionary)

# add new think in dictionary
my_dictionary["Dany"] = "45 years old"
print(my_dictionary)

# KEY!!!!!!!!
# you can change key but you cannot remove key
my_dictionary["Maria"] = my_dictionary.pop("Dany")
print(my_dictionary)

# _________________________________________________________________________________________________________
#                                  if statments
my_variable = 0
if my_variable == 0:
    # so if we have if statment in python we need write "if my_variable == 0:"
    # 							 ^^ ^^^^^^^^^^^ ^^ ^^
    # 1.) "if"- its key word say "I need compare if this equals this"
    # 2.)"my_varable" - its variable which we can compare
    # 3.)"==" - it compare
    # 4.) number or string which we comparing with variable
	print("0")
# so we can put in the if statments compresion operators or relational operators
# for example:
# "<,>,!=, ==, <=, >="

my_variable = 1
if my_variable > 0:
    # type(variable) - function show what type variables do you have.
    print(f"{my_variable} begger than 0")
    #    ^
    # f"{}" - its means what we can put into the bracket variabl




    
#!variable! 
#so Python have a addition assignment
# in regular we do this:
x = 6
# and I need to add number for example 5 
# we can write like that:
x = x  + 5
# but it so large. so sometimes its  great idea to write like x = x + 5
# but if we want to write shotly we can write like x += 5
x += 5
# that means add 5 to x I remaind you x = 6. so 6+5=11
# its same like x = x + 5 but simplyfi to x += 5
