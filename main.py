a = 10 # int variable: "int means - Integer". 
       # We can put into this variable just number like"1,2,3..."

b = "10" # it's string variable can contain symbol ("") or ('') which say Inteprеter, 
    # "hay I have string" but this variable cannot be (10, asdasd, 123) without (""), ('').     

c = 10.5 # this is the float variable. Float is the desemal nomber like 1.2 ...

# Python it's language where we don't need write what type of variable you need,
# but we can transformate integer into string or float

# example

# variable a = 10 it's integer. We can convert into str - String
d = str(a)

# type(variable) - function show what type variables do you have.

# it is just note for which variable we cheking 
print("variable: a")

# it is just for understandeble what type of variable do we have 
print(type(a))

# it is just note for which variable we cheking 
print("variable: d")

# it is just for understandeble what type of variable do we have 
print(type(d))

#_________________________________________________________________________________________________
#                               lists

# This is the list of number 
List = [1,2,3]

# list it's like variable but that can conteinnig not just number.
# We can put into the list: number - integer , string, float and another list

List = [1,"1",1.2]

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

#_________________________________________________________________________________________________
#                                   dictionary

my_dictionary = {} # this is a dictionary. "{}" say for python what that means a dictionary, so if we have for example variable
                   # "number_of_phone = {}". So that mean a dictionary.
# dictionary "my_dictionary" can contain key word and value for example:

my_dictionary = {"Dima":"19 years old"}

# print all dictionary
print(my_dictionary)

# now we print just value
print(my_dictionary["Dima"]) # in [] we can put what do you want to know about these key word.

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
                                                    #^^ ^^^^^^^^^^^ ^^ ^^
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
    print(f"{my_variable} begger than 0")
        # ^
        # f"{}" - its means what we can put into the bracket variable 
        # 