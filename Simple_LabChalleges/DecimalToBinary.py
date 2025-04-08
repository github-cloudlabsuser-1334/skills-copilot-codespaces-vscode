#write a function that converts a decimal number to binary.
# The function takes a decimal number as input and returns its binary representation as a string.   
#
def decimal_to_binary(n):
    """
    Convert a decimal number to binary.

    :param n: Decimal number
    :return: Binary representation as a string
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    binary = ""
    if n == 0:
        return "0"
    
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary   

# Example usage
if __name__ == "__main__":
    decimal_number = 999
    binary_representation = decimal_to_binary(decimal_number)
    print(f"The binary representation of {decimal_number} is: {binary_representation}")  

