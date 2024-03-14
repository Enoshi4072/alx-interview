#!/usr/bin/python3
""" Coding lock boxes """
from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (list of list of int): A list of boxes
    where each box is represented by a list of integers.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
