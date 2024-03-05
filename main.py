def add_numbers(a,b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        int or float: The sum of the two numbers.
        
    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats.")
    return a+b
result=add_numbers('5',5)
print(result)
