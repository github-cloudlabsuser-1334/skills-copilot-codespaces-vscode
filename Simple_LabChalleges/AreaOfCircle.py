# Function that calculates the area of a circle from a given radius.    
#
def AreaOfCircle(radius):   
    """
    Calculate the area of a circle given its radius.

    :param radius: Radius of the circle
    :return: Area of the circle
    """
    pi = 3.14159  # Value of pi
    return pi * (radius ** 2)  # Area formula: πr²  

# Example usage 
if __name__ == "__main__":
    radius = 5  # Example radius
    area = AreaOfCircle(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")  # Output with 2 decimal places    

