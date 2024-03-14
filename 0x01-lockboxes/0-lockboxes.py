#!/usr/bin/env python3
""" Implementing a python function for lock boxes """
def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of boxes
        where each box is represented by a list of integers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxies[box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
