print("Happy Coding Happy Life")

character_name = "John"
character_age = "35"
print("This is " + character_name + ".")

number = 35.49573
is_Male = True
is_Female = False


###########string
print("insert a new line \n This is a new line")
print("escape character \"")
print(character_name.lower()) #lowerCase
print(character_name.upper()) #upperCase
print(character_name.islower()) #if it is lowercase
print(character_name.upper().isupper())
print(len(character_name)) #the length of the string
print(character_name[0]) #the specific character of the string
print(character_name.index("o")) #find the index of the character(s)
print(character_name.replace("J","A")) #replace string


###########number
print(2)
print(-3582.452)
print(3+4.5)
print((3+4)*5)
print(10 % 3) #get the remainder
number = 5
print(str(number)) #convert number to string
print(abs(number)) #get the absolute number
print(pow(3,2))  #the power of the number (number,power)
print(max(4,10))  #get the bigger number
print(min(4,10))
print(round(3.7))  #round the number

from math import *  #import math functions
print(floor(3.7))
print(ceil(3.2))
print(sqrt(36))  #get the square root


###########get input from a user
name = input("Enter your name:")
print(name)


###########build a Calculator
num1 = input("enter a number: ")
num2 = input("enter another number: ")
#int float
result = print(int(num1) + int(num2))


###########list
friends = ["a","b","c"]   #string number true/false
print(friends[0])
print(friends[-1]) #back of the list, the last one
print(friends[0:]) #get all the elements from the first
print(friends[0:2]) #get the first two


###########list functions
luck_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
list2 = [0,0,0,0,0,0]
print(luck_numbers)
luck_numbers.extend(list2) #add a list
luck_numbers.append(888) #add an element
luck_numbers.insert(1,"new") #add an element in the middle
luck_numbers.remove(0) #remove the first 0
luck_numbers.pop() #remove the last element
print(luck_numbers.index(0))
print(luck_numbers.count(0)) #count an element
luck_numbers.remove("new")
luck_numbers.sort()
luck_numbers.reverse() #reverse the list
luck_numbers2 = luck_numbers.copy()
luck_numbers.clear() #clear the list
print(luck_numbers)
print(luck_numbers2)


############Tuples
coordinates = (4,5,6) #can't change
print(coordinates[0])


############Function
def say_hi(name,age):
    print("hello " + name + age)
say_hi(character_name,character_age)


############Return
def cube(num):
    return num*num*num
    #no codes after return
print(cube(3))


############If Statements
if is_Male or is_Female:    #or and
    print("A")
elif is_Male and not(is_Female):  #else if
    print("B")
else:
    print("C")
###
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:   # == !=
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: return num3
print(max_num(3,4,5))


############Dictionary
monthConvertions = {
"Jan": "January",
"Feb": "Febuary",
"Mar": "March",
}
print(monthConvertions["Jan"])
print(monthConvertions.get("xxx","my Default value")) #if the key is not found, it'll give a default value "none"


############while loop
i = 1
while i <= 10:
    print(i)
    i += 1

############
empty_string = ""


############for loop
letters = ["aa","bb","cc"]
for every_letter in letters:
    print(every_letter)
for index_or_any_other_name in range(0,4):
    print(index_or_any_other_name)  #not include 4


############Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,2))


############2D Lists
number_grid = [
 [1,2,3],
 [4,5,6],
 [7,8,9],
 [0]
]
print(number_grid[1][2]) #should be 6
for row in number_grid: #print all the elements in the grid
    for col in row:
        print(col)


############translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("input something: ")))


############except
try:
    num0 = int(input("enter a number: "))
    print(num0)
except ZeroDivisionError as err: #set the error to varible "err"
    print(err)
except ValueError:
    print("invalid input")


############reading files
new_file = open("filename.txt","r") # "r"read mode, "w"write mode, "a" append mode, "r+" read and write
print(new_file.readable()) #check if the file is readable
print(new_file.read())
print(new_file.readline()) #read a single line
print(new_file.readlines()) #read lines and put them into an array
new_file.close()


############Writing to Files
new_file = open("filename.txt","a")
new_file.write("\nsomething new") #add a new line
new_file.close()

new_file = open("filename.txt","w") #overwrite the entire file
new_file.write("something new")
new_file.close()

new_file1 = open("filename1.txt","w") #create a new file


############Modules & Pip
import file_name
print(file_name.my_functions_in_file())
#google "list of python modules"
#terminal: pip install thePythonFile
#terminal: pip uninstall thePythonFile


############Classes & Objects
class Class_name:
    #initialize function
    def __init__(self, element1, element2, element3, element4):
        self.element1 = name
        self.element2 = major
        self.element3 = gpa
        self.element4 = is_or_not
    #create a class function
    def my_class_function (self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#import the class in the file_name
from file_name import Class_name
student1 = Class_name("Jim","business",3.8,False)
print(student1.name)
print(student1.my_class_function())


############Inheritance (class functions from another class)
class Class_name2(Class_name): #import all the functions in class1 into class2
