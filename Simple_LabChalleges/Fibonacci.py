#
# Below function is to returns the nth Fibonacci number.
def fibonacci(n):
    #initiate the first two Fibonacci numbers.
    a, b = 0, 1
    # Loop to calculate the Fibonacci numbers.
    # The loop runs n times to generate the Fibonacci sequence.
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Return the nth Fibonacci number.
# Example usage:    
fibonacci(10) 
