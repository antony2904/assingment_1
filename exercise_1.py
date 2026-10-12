# 1. What is indentation in Python, and why is it important?
# ------------------------------------------------------------------------------
"""
Answer:
Indentation refers to the leading spaces or tabs at the beginning of a line of code.
In Python, indentation defines code blocks and scope (for functions, loops, if-statements, etc.)
instead of curly braces {}.

Importance:
- Enforces code readability and consistent structure.
- Determines the logical hierarchy and flow of execution.
- Missing or inconsistent indentation raises an IndentationError.
"""


# 2. Explain the difference between syntax errors and runtime errors?
# ------------------------------------------------------------------------------
"""
Answer:
- Syntax Errors: Detected by the Python parser before running the script.
  Caused by invalid grammar (e.g., missing colon, unclosed parenthesis).
  The code will not execute at all.
- Runtime Errors (Exceptions): Occur while the program is actively executing.
  The syntax is valid, but an invalid operation occurs (e.g., dividing by zero,
  accessing an out-of-range index).
"""


# 3. How do you assign a value to a variable?
# ------------------------------------------------------------------------------
# Answer: Using the assignment operator (=), with the variable name on the left.
x = 10
name_val = "Python"


# 4. What is the difference between mutable and immutable data types?
# ------------------------------------------------------------------------------
"""
Answer:
- Mutable: Objects whose value can be modified in place after creation without 
  changing their identity/memory address (e.g., list, dict, set).
- Immutable: Objects whose value cannot be changed once created. Any modification 
  creates a new object in memory (e.g., int, float, str, tuple).
"""


# 5. What is a lambda function? When is it useful?
# ------------------------------------------------------------------------------
"""
Answer:
A lambda function is an anonymous, single-line function defined using the `lambda` keyword.
Syntax: lambda arguments: expression

When it is useful:
- For short, throwaway operations where defining a standard `def` function is unnecessary.
- Frequently used with higher-order functions like map(), filter(), and sorted(key=...).
"""
square = lambda x: x * x


# 6. Write a program to generate the first n Fibonacci numbers and print their sum.
# ------------------------------------------------------------------------------
def fibonacci_sum(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    fib_lst = [0, 1][:n]
    while len(fib_lst) < n:
        nxt_fib = fib_lst[-1] + fib_lst[-2]
        fib_lst.append(nxt_fib)
        
    print(f"First {n} Fibonacci numbers: {fib_lst}")
    print(f"Sum: {sum(fib_lst)}")

fibonacci_sum(12)


# 7. Create 3 variables name, age and city. Assign your details and print them in one sentence.
# ------------------------------------------------------------------------------
name = "Antony"
age = 23
city = "Thrissur"

print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# 8. Write a program that swaps the values of two variables.
# ------------------------------------------------------------------------------
a = 55
b = 100
a, b = b, a

print("a:", a, "b:", b)


# 9. Write a program to calculate the area of a rectangle using variables length and width.
# ------------------------------------------------------------------------------
length = 260
width = 150
area = length * width

print(f"The area of the rectangle is {area}")


# 10. Write a Python program that converts a string “50” into an integer and add 100 to it.
# ------------------------------------------------------------------------------
string_num = "50"
result = int(string_num) + 100

print("Result:", result)


# 11. Create a tuple of 3 elements and try to change one element. Observe and explain the error.
# ------------------------------------------------------------------------------
tuple_lst = (23, 56, 45)

try:
    tuple_lst[0] = 10
except TypeError as e:
    print(f"Observed Error: {e}")

"""
Explanation:
Tuples are immutable in Python. Once created, their items cannot be modified,
reassigned, or appended, which raises a TypeError when item assignment is attempted.
"""


# 12. Write a program that checks if two lists have at least one element in common using sets.
# ------------------------------------------------------------------------------
lst_1 = [1, 2, 3, 4]
lst_2 = [4, 5, 6, 7]

if set(lst_1) & set(lst_2):
    print("The lists have at least one common element.")
else:
    print("No common elements.")


# 13. Write a function is_prime(n) that checks whether a number is prime or not.
# ------------------------------------------------------------------------------
def function_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 121 prime?:", function_is_prime(121))


# 14. Write a function is_palindrome(word) that returns True if the word is palindrome.
# ------------------------------------------------------------------------------
def function_is_palindrome(word):
    word = str(word).lower()
    return word == word[::-1]

print("Is 'car' palindrome?:", function_is_palindrome("car"))


# 15. Write a python program to create a simple calculator using functions.
# ------------------------------------------------------------------------------
def addition(x, y): 
    return x + y

def subtraction(x, y): 
    return x - y

def multiplication(x, y): 
    return x * y

def division(x, y): 
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num_1, num_2 = 10, 2
print("Addition:", addition(num_1, num_2))
print("Subtraction:", subtraction(num_1, num_2))
print("Multiplication:", multiplication(num_1, num_2))
print("Division:", division(num_1, num_2))


# 16. Write a function check_even_odd(num) that takes a number and prints whether its even or odd.
# ------------------------------------------------------------------------------
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

check_even_odd(257)


# 17. Write a function reverse_number(n) that returns the reverse of a number.
# ------------------------------------------------------------------------------
def reverse_number(n):
    return int(str(n)[::-1])

print("Reversed number:", reverse_number(56789))


# 18. Write a program using try, except, else and finally together.
# ------------------------------------------------------------------------------
def divide_number(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print("Error: you cannot divide by zero!")
    else:
        print(f"Success, the result is {res}")
    finally:
        print("Execution of divide_number is completed.\n")

divide_number(10, 2)
divide_number(10, 0)