#!/usr/bin/python3
""" Working to forma a pascals triangle """
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): Number of rows to generate in the Pascal's triangle.

    Returns:
    list of lists: Pascal's triangle up to the nth row.

    If n is less than or equal to 0, an empty list is returned.
    """
    
    if type(n) is not int or n <= 0:
        return []

    triangle = [[1]]

    
    for i in range(1, n):
        
        prev_row = triangle[-1]
        
        new_row = [1]
        
        for j in range(1, len(prev_row)):

            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)
        
        triangle.append(new_row)

    
    return triangle
