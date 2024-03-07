#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): Number of rows to generate in the Pascal's triangle.

    Returns:
    list of lists: Pascal's triangle up to the nth row.

    If n is less than or equal to 0, an empty list is returned.
    """
    """ Checking if n is less than or equal to 0"""
    if n <= 0:
        return []

    """ Initializing Pascal's triangle with the first row [1]"""
    triangle = [[1]]

    """ Iterating to generate subsequent rows """
    for i in range(1, n):
        """ Geting the previous row """
        prev_row = triangle[-1]
        """ Initializing a new row with the first element as 1 """
        new_row = [1]
        """ Iterating through the previous row to calculate new elements """
        for j in range(1, len(prev_row)):
            """ Calculating each element by summing the elements
            in the previous row and adjacent to the current element """
            new_row.append(prev_row[j - 1] + prev_row[j])
        """ Adding the last element to the new row """
        new_row.append(1)
        """ Add the new row to the triangle """
        triangle.append(new_row)

    """ Returning the Pascal's triangle up to the nth row"""
    return triangle
