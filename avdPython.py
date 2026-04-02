'''
Q1. Write Python code to create a dictionary containing mobile names and their prices. Create 
DataFrame from this dictionary. Display the contents of DataFrame.

import pandas as pd

Student = {
    "Names": ["Vaibhav", "Sanket", "Sushant", "Saurabh", "Satyam", "Karan"],
    "Marks": [98, 75, 65, 55, 55, 60]
}

df = pd.DataFrame(Student)

print(Student)
print()
print(df)
print()
print(df.head(1))
print()
print(df.loc[0])

Q2. Create a package vehicle with a sub package types, sub package type contains modules cars and 
bikes. Each module should have a function available_models() returning a list of models. Write a 
python program to display all available models of cars and bikes.



Q2. Write a python program to list all files in a current directory. Display total count of .py files and 
content of any one .py files.'''
'''


import os
directories = os.getcwd()
curr = os.listdir(directories)
cnt = 0
for file in curr:
    if file.endswith(".py"):
        print(file)
        cnt = cnt+1
        if cnt == 4:
            print("Content in ", file)
            with open(file, 'r') as f:
                print(f.read())
if cnt == 0:
    print("No Python Files are Present")

print()
print("Total Files are - ", cnt)
print()



Q1. Write a python program to accept a string, Count total number of vowels, consonants and special 
symbols from it.


statement = input("Enter A String ")
vow = con = sp = 0


for i in statement:
    if i in "aeiou":
        vow = vow + 1
    elif i.isalpha():
        con = con + 1
    else:
        sp = sp + 1
print(f"Total No. of Vowel {vow}, Total No. of Consonent {con}, Total No. of Special Characters {sp}")
'''    
'''
Q2. Consider a following record in DataFrame IPL. Player Team Category BidPrice Runs
Hardik Pandya Mumbai Indians Batsman 13 1000
K L Rahul Kings Eleven Batsman 12 2400
Andre Russel Kolkata Knight Riders Batsman null 900
Jasprit Bumrah Mumbai Indians Bowler 10 200
Virat Kohli RCB Batsman 17 3600
Rohit Sharma Mumbai Indians Batsman null 3700
Create above DataFrame in python and write python code for following
a) Retrieve first 2 rows
b) Retrieve last 3 rows
c) Check null values present in DataFrame.
d) Replace null value with mean of that column.
e) Find most expensive player.
f) Print total players per team.


import pandas as pd

dic = {
    "Player" : ["Hardik", "Rahul", "Russel", "Bumrah", "Virat", "Rohit"],
    "Team" : ["MI", "PBKS", "KKR", "MI", "RCB", "MI"],
    "Category" : ["Batsman", "Batsman", "Batsman", "Bowler", "Batsman", "Batsman"],
    "BidPrice" : [13, 12, None, 10, 17, None],
    "Runs" : [1000, 2400, 900, 200, 3600, 3700]
}

IPL = pd.DataFrame(dic)

print(IPL)

print()

print(IPL.head(2))

print()

print(IPL.tail(3))

print(IPL.isnull().sum())

IPL["BidPrice"].fillna(IPL["BidPrice"].mean(), inplace=True)

print(IPL)

print()

maxbid = IPL["BidPrice"].max()

player = IPL[IPL["BidPrice"] == maxbid]

print(player)

print()

print(IPL.groupby("Team")["Player"].count())


Q2. Write a Python program to demonstrate a user-defined exception that checks whether the entered 
marks are between 0 and 100. Display an appropriate message for invalid input and out-of-range 
values. Also display Grade of marks


class error(Exception):
    pass

try:
    marks = int(input("Enter Marks "))
    
    if marks < 0 or marks > 100:
        raise error("Marks Are Out of Range")
    if marks > 90:
        print("A+")
    elif marks > 80:
        print("A")
    elif marks > 70:
        print("B+")
    elif marks > 60:
        print("B")
    elif marks > 50:
        print("C+")
    elif marks > 40:
        print("C")
    elif marks > 35:
        print("D")
    else:
        print("Fail")

except ValueError:
    print("Invalid Value")

except error as e:
    print("Error : ", e)

    
Q1. Write a Python program that accepts value of m and n. Divides m by n and handles a
ZeroDivisionError if the user tries to divide by zero.


dividend = int(input("Enter Dividend "))
divisor = int(input("Enter Divisor "))

try:
    print(dividend / divisor)
except ZeroDivisionError:
    print("Divisor Cannot be Zero")


Q2. Write a python program to create a module containing factorial function, power dictionary and list 
of vowels. Save this as variables.py. Import variables module to print the factorial of n, print the 
power of n, and second alphabet from the vowels list. (Accept n from user)


Q2. Write a python program to accept a file name from user. If file exist display contents of file and 
number of characters, words and lines in a file, otherwise display appropriate message.


import os

directories = os.getcwd()

curr = os.listdir(directories)

for file in curr:
    print(file)

file = input("Enter any of the above File Name ")

with open(file, 'r')as f:
    data = f.read()

char = word = line = 0

for i in data:
    char = char + 1
    if i == ' ':
        word = word + 1
    if i == '\n':
        line = line + 1

print("Total Characters in file = ", char)
print("Total Words in file = ", word)
print("Total Lines in file = ", line)


Q1. Write a Python program to create a list of elements. Shuffle the elements of a given list and display 
the list. [Hint: Use random.shuffle()]


import random

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(li)
random.shuffle(li)
print(li)


Q2. Create a following DataFrame named as “data”. Write the python code for the following 
commands. Company Count Price
Pencil Apsara 15 250
Pencil Natraj 20 200
Pen Cello 25 600
Pen Parkar 35 900
Eraser Apsara 20 300
a) Find all rows with the label “Pencil”. Extract all columns
b) Change the Eraser count as 25 instead of 20.
c) List only the columns Company and Price.
d) List only rows with labels ‘Pencil’ and ‘Pen’
e) Rename Column Count as Quantity and display DataFrame.


import pandas as pd

data = {
    "Name" : ["Pencil", "Pencil", "Pen", "Pen", "Eraser"],
    "Company" : ["Apsara", "Natraj", "Cello", "Parkar", "Apsara"],
    "Count" : [15, 20, 25, 35, 20],
    "Price" : [250, 200, 600, 900, 300]
}

df = pd.DataFrame(data)

print(df[df["Name"] == "Pencil"])

df.loc[df["Count"] == 25, "Count"] = 20

print(df)

print(df[["Company", "Price"]])

print(df[df["Name"].isin(["Pen", "Pencil"])])

df.rename(columns = {"Count" : "Quantity"}, inplace = True)

print(df)


Q2. Write a python program for following
a) Create a file which stores the first name, middle name and last name of your 5 friends
b) Display contents of file
c) Append other 5 friend’s names
d) Display


with open("names.txt", "a") as f:
    f.write("\nSanket Rajaram Sul")

print(f)

with open("names.txt", "r") as f:
    print(f.read())


Q1. Write a python program to accept a string, find all words that do not contain vowels.


string = input("Enter a String ")
words = string.split()
new = []

for word in words:
    is_vowel = False
    for i in word:
        if i in "aeiouAeiou":
            is_vowel = True
            break
    if not is_vowel:
        new.append(word)

print(new)


Q2. Create a package banking with modules account.py and loan.py.
a)account.py should contain function open_account(name)that accepts a user’s name and prints a message
confirming account creation
b)loan.py should contain functionapply_loan(amount)that accepts a loan amount and prints a confirmation
message with the amount
Write a python program to import modules from banking package and demonstrate both functions.


Q2. Write a python program to create a list of prime numbers between m and n using List 
comprehension. (Accept the value of m and n from user, m should be less than n)


import numpy as np

a = int(input("Enter A (A Must be less than B)"))
b = int(input("Enter B (A Must be less than B)"))
prime = []
for i in range(a, b):
    flg = True
    for j in range(2, i):
        if(i % j == 0):
            flg = False
            break
    if flg:
        prime.append(i)
print(prime)


Q1. Write a Python program that prompts the user to input two numbers and raises a TypeError 
exception if the inputs are not numerical.


try:
    a = int(input("Enter a Number "))
    b = int(input("Enter a Number "))

    result = a + b

    print("Valid Inputs")

except ValueError:
    try:
        raise TypeError("Inputs are not numeric")
    except TypeError as e:
        print(e)


Q2. Create a following DataFrame named as “data”. Write the python code for the following
Company Count Price
Pencil Apsara 15 250
Pencil Natraj 20 200
Pen Cello 25 600
Pen Parkar 35 900
Eraser Apsara 20 300
a) Find all rows with the label “Pencil”. Extract all columns
b) Change the count of Eraser as 25 instead of 20.
c) List only the columns Company and Price.
d) List only rows with labels ‘Pencil’ and ‘Pen’




e) Delete column Count from the above DataFrame and display DataFrame..
Q2. Create a Web Page using Flask which contains following information about your Personal Portfolio 
Page
a) Show your name as a centered heading.
b) List your Qualification details.
c) Add your special skill


Q1. Write a python program to accept a string, extract all words that start with a capital letter and 
remove all special characters from a string. Display modified string. (Accept input from user)


import re

string = input("Enter a String ")
capital = []

cleaned = re.sub(r'[^A-Za-z]', ' ', string)

words = cleaned.split()

for word in words:
    if word[0].isupper():
        capital.append(word)
        

print("Modified String:", cleaned)
print("Words starting with capital letter:", capital)

Q2. Create a Web Page using Flask which contains following information about your Library Book List
a) Show the library name as a heading.
b) Display all available books in a table with title and author.
c) Add quote about reading in bold and blue color.

Q2. Write a python program to accept file name. If file exist copy contents of one file into another file 
and display contents of new file along with total number of lines, words and characters otherwise 
give appropriate message

import os
directories = os.getcwd()
curr = os.listdir(directories)

for file in curr:
    print(file, end = '\t')
try:
    file = input("Enter File Name")
    
    with open(file, "r") as f:
        data = f.read()

    print(data)

    char = len(data)
    word = data.split()
    lines = data.split('\n')

    print("Characters - ", char)
    print("Words - ", len(word))
    print("Lines - ", len(lines))

    with open("newfile", "w") as f:
        f.write(data)

    with open("newfile", "r") as f:
        data2 = f.read()

    print(data2)

except FileNotFoundError:
    print("No File Named", file)


Q1. Write a python program to accepts value of radius from user and calculate the area of a circle using 
function. (Use 3.14 as the value of π).

r = int(input("Enter Radius"))

print(3.14*r**2)


Q2. Write a python program to create a list, string and tuple in python. Apply random module to display 
unique multiple random elements from above created sequence type.


import random
li = ["Vaibhav", "Sanket", "Sushant"]
sub = ("Eng", "Maths", "CS")
string = "Hello Everyone"

print(random.sample(li, 2))
print(random.sample(sub, 2))
print(random.sample(string, 2))

Q2. Create a Web Page using Flask which contains following information about your college.
a) College Name as a heading in center of web page.
b) Display all the courses available in your college.
c) Image of your Colleg
'''

