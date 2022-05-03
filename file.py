
num1 = 42  #variable declaration,numbers initialize
num2 = 2.3 #variable declaration, numbers initialize
boolean = True #variable declaration, Boolean initialize
string = 'Hello World' #variable declaration, String initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple initialize
print(type(fruit)) #print to console, type check
print(pizza_toppings[1]) #print to console, list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #print to console, Dictionary access value
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #Dictionary change value
print(fruit[2]) #print to console, tuple access value

if num1 > 45: #Conditional if
    print("It's greater") #print to console
else: #Conditional else
    print("It's lower") #print to console

if len(string) < 5: #Conditional if
    print("It's a short word!") #print to console
elif len(string) > 15: #Conditional elif
    print("It's a long word!") #print to console
else: #Conditional else
    print("Just right!") #print to console

for x in range(5): #For Loop start 0 until 5
    print(x) #print to console
for x in range(2,5): #For Loop start 2 until 5
    print(x) #print to console
for x in range(2,10,3): #For Loop start 2 until 10 increment 3
    print(x) #print to console
x = 0 #variable declaration
while(x < 5): #While loop start 0 until 5
    print(x) #print to console
    x += 1 #increment by 1

pizza_toppings.pop() #list delete last value
pizza_toppings.pop(1) #list delelte value at index 1

print(person) #print dictionary to console 
person.pop('eye_color') #Dictionary delete value 'eye_color
print(person) #print dictionary to console 

for topping in pizza_toppings: #for loop list
    if topping == 'Pepperoni': #conditional if
        continue #continue
    print('After 1st if statement') #print to console
    if topping == 'Olives': #conditional if
        break #end loop

def print_hello_ten_times(): #defining function
    for num in range(10): #for loop start 0 until 10
        print('Hello') #print to console

print_hello_ten_times() #function call

def print_hello_x_times(x): #defining function
    for num in range(x): #for loop start 0 until x
        print('Hello') #print to console

print_hello_x_times(4) #function call that will print 'Hello' 4 times

def print_hello_x_or_ten_times(x = 10): #defining function with default value x=10
    for num in range(x): #for loop start 0 until 10
        print('Hello') #print to console

print_hello_x_or_ten_times() #function call print to console 10 times
print_hello_x_or_ten_times(4) #function call print to console 4 times


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined
# num3 = 72 Variable declaration number initialize
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry')- AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'