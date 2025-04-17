# Refactor this code to use a loop instead of recursion
# This code calculates the factorial of a number using recursion.
# We will refactor it to use a loop instead.
# Original code using recursion
def factorial(n):
if n == 0 or n == 1:
return 1
else:
return n * factorial(n-1)# Refactor this code to use a loop instead of recursion
# test the refactored code

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   

