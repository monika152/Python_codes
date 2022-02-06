# Annotation (Hinweis)
# Function Documentation


def addieren(x:int , y:int =0) -> int:
    """ THis will add two different numbers to

    Args:
        x(int): The first number
        y(int,optional): The second number.

    Returns:
        int: The result of sum
    """
    result = x+y
    return result


addieren(5,6)

addieren("Spagetti","Apfel")

addieren(5,6)
