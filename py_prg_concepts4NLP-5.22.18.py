#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:36:08 2018

@author: briangriner
"""

# Python programming concepts for NLP

# object has 3 things: Identity, Type, Value
new_string = "This is a string"
id(new_string) # shows object identifier (address)
type(new_string) # shows object type
new_string # shows object value

# Numeric types: integers and operations on them

num = 123
type(num)
num + 1000 # addition
num * 2 # multiplication
num / 2 # division

# decimal int - start with 1
1 + 1

# octal - int start with 0
oct(8)
oct(7 + 1)
0o10

# binary - start with 0b
bin(2)
0b1 + 0b1
bin(0b1 + 0b1)

# hexadecimal int - start 0x
hex(16)

# Floating point numbers
1.5 + 2.6
1e2 + 1.5e3 + .5
2.5e4
2.5e-2

# complex numbers - 2 components: real + imaginary (ends with j)
cnum = 5 + 7j
type(cnum)
cnum.real
cnum.imag
cnum + (1 - 0.5j)

# Lists - index follows order of sequence in list 
l1 = ['eggs', 'flour', 'butter']
l2 = list([1, 'drink', 10, 'sandwiches', 0.45e-2])
l3 = [1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
print(l1, l2, l3)

# Indexing lists
l1
l1[0]
l1[1]
l1[0] + ' ' + l1[1]

# slicing lists - starts at 0 ends at n-1 so 1:3 returns list elements 1 and 2
l2[1:3]

# sets - unordered, unique, immutable
l1 = [1,1,2,3,5,5,7,9,1]
set(l1)
s1 = set(l1)

# membership testing
1 in s1
100 in s1

# initialize a second set
s2 = {5, 7, 11}

# set operations
s1 - s2 # set difference
s1 | s2 # set union
s1 & s2 # set intersection
s1 ^ s2 # elements not in both sets

# dictionaries - key-value mappings, similar to json
d1 = {'eggs':2, 'milk':3, 'spam':10}

# retrieve items based on key
d1.get('eggs')
d1.get('orange')

# set up items with specific key
d1['orange'] = 25
d1

# viewing keys and values
d1.keys()
d1.values()

# create new dictionary using dict function
d2 = dict({'orange':5, 'melon':17, 'milk':10})

# update dictionary d1 based on new key-values in d2
d1.update(d2)

# complex and nested dictionary
d3 = {'k1':5, 'k2':[1,2,3,4,5], 'k3':{'a':1, 'b':2, 'c':[1,2,3]}}
d3.get('k3')
d3.get('k3').get('c')

# tuples - immutable sequences
# create tuple with single element
single_tuple = (1,)
single_tuple

# original address of tuple
id(single_tuple)

# modifying tuple contents creates new address
single_tuple = single_tuple + (2,3,4,5)
single_tuple

id(single_tuple) # different address indicates new tuple with same name

# tuples immutable - assignment not supported like list
single_tuple[3] = 100

# accessing and unpacking tuples
tup = (['this', 'is', 'list', '1'], ['this', 'is', 'list', '2'])
tup[0]
l1, l2 = tup
print(l1, l2)

# Files - special object types that interface with external objects in filesystem
f = open('text_file.txt', 'w') # open file in write mode
f.write("This is some text\n") # write some text
f.write("Hello world!")
f.close() # closes the file

# list files in the current dir
import os
os.listdir(os.getcwd())

f = open('text_file.txt', 'r') # open file in read mode
data = f.readlines() # reads in all lines from file
print(data)

# control flow in python - if-elif-else, for and while loops, 
#  break-continue-else, try-except

# conditionals - if, elif, else
var = 'spam'
if var == 'spam':
    print('Spam')

var = 'ham'
if var == 'spam':
    print('Spam')
elif var == 'ham':
    print('Ham')

var = 'foo'
if var == 'spam':
    print('Spam')
elif var == 'ham':
    print('Ham')
else:
    print('Neither Spam or Ham')

# Loops - for, while

# for loop
numbers = range(0,5)
for number in numbers:
    print(number)
    
sum = 0    
for number in numbers:
    sum +=  number
    
print(sum)

# trailing else and break
for number in numbers:
    print(number)
else:
    print('loop exited normally')
    
for number in numbers:
    if number < 3:
        print(number)
    else:
        break
else:
    print('loop exited normally')
    
# while loops
number = 5
while number > 0:
    print(number)
    number -= 1 # IMPORTANT else loop keeps running
    
# continue
number = 10
while number > 0:
    if number % 2 != 0:
        number -= 1 # decrement but don't print odd numbers
        continue # return to the beginning of loop for next
        
    print(number) # print number then decrement
    number -= 1
    
# pass
number = 10
while number > 0:
    if number != 0:
        pass # do not print odd numbers
    else:
        print(number)
    number -= 1
    
# exception handling - try, except, finally
    
# try to access item not in list
shopping_list = ['eggs', 'ham', 'bacon']
try:
    print(shopping_list[3])
except IndexError as e:
    print('Exception: ' + str(e) + ' has occurred')
else:
    print('No exceptions occurred')
finally:
    print('I will always execute no matter what!')
    
# smooth code execution without errors
shopping_list = ['eggs', 'ham', 'bacon']
try:
    print(shopping_list[2])
except IndexError as e:
    print('Exception: ' + str(e) + ' has occurred')
else:
    print('No exceptions occurred')
finally:
    print('I will always execute no matter what!')


# Functional programming - definition+signature(name, parameters)+statements
    
# function with single argument
def square(number):
    return number*number

square(5)

# numpy lib function
import numpy as np
np.square(5)

# function with variable number of arguments
def squares(*args):
    squared_args = []
    for item in args:
        squared_args.append(item*item)
    return squared_args

squares(1,2,3,4,5)

# assign keyword based args dynamically
def person_details(**kwargs):
    for key, value in kwargs.items():
        print(key, '->', value)
        
person_details(name='James Bond', alias='007', job='Secret Service Agent')

# Recursive functions (function that calls itself)
def recursive_squares(numbers):
    if not numbers:
        return []
    else:
        return [numbers[0]*numbers[0]] + recursive_squares(numbers[1:])

recursive_squares([1,2,3,4,5])

# anonymous functions (aka lambda functions) - single inline expressions

# simple lambda function to square a number
lambda_square = lambda n: n*n
lambda_square(5)

# map function to square numbers using lambda
map(lambda_square, [1,2,3,4,5])

# lambda function to find square numbers using lambda
lambda_evens = lambda n: n%2 == 0
filter(lambda_evens, [1,2,3,4,5,6,7,8,9,10])

# lambda function to add numbers in reduce function
from functools import reduce
lambda_sum = lambda x, y: x + y
reduce(lambda_sum, [1,2,3,4,5])

# lambda function - make sentence from word tokens using reduce
lambda_sentence_maker = lambda word1, word2: ' '.join([word1, word2])
reduce(lambda_sentence_maker, ['I', 'am', 'making', 'a', 'sentence', 'from', 'words!'])

# Iterators - used to iterate through iterables

# for loop
numbers = range(6)
for number in numbers:
    print(number)

# how the iterator works - NOTE: Py 3 replaced .next() with .__next__()
iterator_obj = iter(numbers)
while True:
    try:
        print(iterator_obj.__next__())
    except StopIteration:
        print('Reached end of sequence')
        break
    
# second call of __next__() returns an exception
iterator_obj.__next__()

# Comprehensions - like for loops but more efficient
numbers = range(6)
numbers

# simple list comprehension to compute squares
[num*num for num in numbers]

# list comprehension - check if numbers divisible by 2
[num%2 for num in numbers]

# set comprehension returns distinct values list comprehension above
set(num%2 for num in numbers)

# dictionary comprehension where key:value is number: square(number)
{num: num*num for num in numbers}

# combined comprehension example
[{'number': num, 'square': num*num, 'type': 'even' if num%2 == 0 else 'odd'} for num in numbers]

# nested list comprehension - flattening a list of lists 
list_of_lists = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
list_of_lists
[item for each_list in list_of_lists for item in each_list] #??? LOOK UP


# Generators - 2 types: functions or expressions 
# - lazy evaluation: yield 1 at a time - memory efficient

numbers = [1,2,3,4,5]

def generate_squares(numbers):
    for number in numbers:
        yield number*number
    
gen_obj = generate_squares(numbers)
gen_obj

for item in gen_obj:
    print(item)
    
# generate expressions
csv_string = 'The,fox,jumps,over,the,dog'

# make sentence with list comprehension
list_cmp_obj = [item for item in csv_string.split(',')]
list_cmp_obj
' '.join(list_cmp_obj)

# make sentence with generator expression
gen_obj = (item for item in csv_string.split(','))
gen_obj
' '.join(gen_obj)

# check out py libs: collections, itertools, functools


# Classes

# class definition
class Animal(object):
    species = 'Animal'
    
    def __init__(self, name):
        self.name = name
        self.attributes = []
        
    def add_attributes(self, attributes):
        self.attributes.extend(attributes) \
        if type(attributes) == list \
        else self.attributes.append(attributes)
        
    def __str__(self):
        return self.name+" is of type "+self.species+" and has attributes:"+str(self.attributes)
    
# instantiating the class
a1 = Animal('Rover')
# invoking instance method
a1.add_attributes(['runs', 'eats', 'dog'])
# user defined string representation of the Animal class
str(a1)

# deriving class Dog from base class Animal
class Dog(Animal):
    species = 'Dog'
    
    def __init__(self, *args):
        super(Dog, self).__init__(*args)
        
# deriving class Fox from base class Animal
class Fox(Animal):
    species = 'Fox'
            
    def __init__(self, *args):
        super(Fox, self).__init__(*args)
            
# creating instance of class Dog
d1 = Dog('Rover')
d1.add_attributes(['lazy', 'beige', 'sleeps', 'eats'])
str(d1)

# creating instance of class Fox
f1 = Fox('Silver')
f1.add_attributes(['quick', 'brown', 'jumps', 'runs'])
str(f1)


# working with text

# String literals

"""
short strings - '' or ""
"""
# long strings - ''' ... ''' or """ ... """
'''
escape sequences - perform backspace interpolation - \n is newline, \t is tab
bytestring - bytes('...') or b'...'
raw string - created for regex - no backspace interpolation
unicode - non-ASCII - u'...' - hexbyte escape sequence - '\uVV' 
 - 16bit '\uVVVV' - 32 bit 'uVVVVVVVV'
'''

# simple string
simple_string = 'hello' + " I'm a simple string"
print(simple_string)

# multi-line string
multi_line_string = """Hello I'm 
a multi-line
string!"""
multi_line_string # \n newline escape character automatically created

print(multi_line_string)

# normal string - escape seq produces wrong file path
escaped_string = "C:\the_folder\new_dir\file.txt"
print(escaped_string)

# raw string - backslashes in normal form
raw_string = r'C:\the_folder\new_dir\file.txt'

# unicode
string_with_unicode = u'H\u00e8llo!'
print(string_with_unicode)

# String operations and methods

# basic operations

# string concatenation
'Hello' + ' and welcome ' + 'to Python!'
'Hello and welcome to Python!'
'Hello' ' and welcome ' 'to Python!'

# concatenation of variables and literals
s1 = 'Python!'
'Hello ' + s1
# can not use this method for concatenation of variable and literal
'Hello ' s1

# more ways to concatenate strings
s2 = '--Python--'
s2*5
s1+s2
(s1+s2)*3

# concatenate many strings in parenthese
s3 = ('This '
      'is another way '
      'to concatenate '
      'several strings!')
s3

# check for substrings in a string
'way' in s3
'python' in s3

# compute total length of string
len(s3)


# indexing and slicing - L toR starts at 0 
# - R to L use neg numbers start with -1
# - slices var[start:stop]

# create a string
s = 'PYTHON'

# string indexes
s[0], s[1], s[2], s[3], s[4], s[5]
s[-1], s[-2], s[-3], s[-4], s[-5], s[-6]

# string slicing
s[:]
s[1:4]
s[:3]
s[3:]
s[-3]
s[:3] + s[3:]
s[:3] + s[-3:]

# string slicing with offsets
s[::1] # no offset
s[::2] # print every 2nd character in string

# strings are immutable hence assignment produces an error
s[0] = 'X'

# create new string
'X' + s[1:]


# methods - check https://docs.python.org/3/library/stdtypes.html#string-methods

# case conversions
s = 'python is great'
s.capitalize()
s.upper()

# string replace
s.replace('python', 'analytics')

# stripping whitespace characters
s = '   I am surrounded by spaces    '
s
s.strip()

# converting to title case
s = 'this is lower case'
s.title()

# formatting - 2 main types: expressions %s and methods '...{}...'.format(values)

# simple string formatting expressions
'Hello %s' %('Python!')
'Hello %s' %('World!')

# formatting expression with different data types
'We have %d %s containing %.2f gallons of %s' %(2, 'bottles', 2.5, 'milk')
'We have %d %s containing %.2f gallons of %s' %(5, 'jugs', 10.867, 'juice')

# formatting using format method
'Hello {} {}, it is a great {} to meet you'.format('Mr', 'Jones', 'pleasure')
'Hello {} {}, it is a great {} to meet you'.format('Sir', 'Arthur', 'honor')

# alternative formatting ways
'I have a {food_item} and a {drink_item} with me'.format(drink_item='soda', food_item='sandwich')
'The {animal} has the following attributes: {attributes}'.format(animal='dog', attributes=['lazy', 'loyal'])

# regular expressions
"""
re module used to create raw string patterns for search and substitution
regex is usually compiled into bytecode and executed by an engine used to match 
strings in text. re contains several flags:
    re.I or re.IGNORECASE
    re.S or re.DOTALL - . matches any char including new lines
    re.U or re.UNICODE - depreciated in python 3
pattern matching rules:
    . match single character
    ^ match start of string
    $ match end of string
    * match 0 or more cases of previous regex before *
    ? match 0 or 1 case of previous regex before ?
    [...] match any character inside []
    [^...] match any character inside [] after ^
    | OR match preceeding or next regex
    + match 1 or more cases of previous regex before +
    \d match decimal digits - also use [0-9]
    \D match non-digits - also use [^0-9]
    \s match white space characters
    \S match non-white space characters
    \w match alphanumeric characters - also use [a-zA-Z0-9_]
    \W match non-alphanumeric characters - also use [^a-zA-Z0-9_]
re module compile methods:
    re.compile()
    re.match() - regex match at beginning of strings
    re.search() - regex match any position in string
    re.findall() - returns all non-overlapping matches
    re.finditer() - returns iterator to find all matches scanned L to R
    re.sub() - substitutes L most pattern in string
"""

# import re module
import re

# regex unicode matching
s = u'H\u00e8llo'
s
print(s)

# does not return unicode even if alphanumeric
re.findall(r'\w+', s)

# need unicode flag
re.findall(r'\w+', s, re.UNICODE) 

# create pattern and sample strings for regex
pattern = 'python'
s1 = 'Python is an excellent language'
s2 = 'I love the Python language. I also use Python to build applications at work!'

# returns match if found at beginning of string
re.match(s1) # use re.IGNORECASE next
re.match(pattern, s1, flags=re.IGNORECASE)

# print matched string and index
m = re.match(pattern, s1, flags=re.IGNORECASE)
print('Found match {} ranging from index {} - {} in the string "{}"'.format(m.group(0), m.start(), m.end(), s1))

# no match if not beginning of string
re.match(pattern, s2, re.IGNORECASE)

# re find and search
re.search(pattern, s2, re.IGNORECASE)
re.findall(pattern, s2, re.IGNORECASE)
match_objs = re.finditer(pattern, s2, re.IGNORECASE)
print("String:", s2)

for m in match_objs:
    print('Found match "{}" ranging from index {} - {}'.format(m.group(0, m.start(), m.end())))
    
# pattern substitution and subn methods
re.sub(pattern, 'Java', s2, flags=re.IGNORECASE)
re.subn(pattern, 'Java', s2, flags=re.IGNORECASE)








    



