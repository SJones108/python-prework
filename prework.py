# QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
 
 name = user_name.upper()
 print("Hello_" + name + "!")

hello_name("Shirley")

# QUESTION 2
# Write a python function, first_odds that prints the odd 
# numbers from 1-100 and returns nothing
 
def first_odds(odd_n):
    for n in range(1, 101):
        if n % 2 == 1:
            print(n)

# QUESTION 3
# Please write a Python function, max_num_in_list to return the max number 
# of a given list. The first line of the code has been defined as below.

def max_num_in_list( a_list):
    mn = max(a_list)
    print(mn)

list =  [24, 88, 98, 112, 441, 34]
max_num_in_list(list)

# QUESTION 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it 
# is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year): 
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("What year is it? "))
print(is_leap_year(year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
# consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
   print(sorted(con_list) == list(range(min(con_list), max(con_list)+1)))

con_list = [1, 2, 3, 4, 5, 6, 7, 8]
is_consecutive(con_list)


