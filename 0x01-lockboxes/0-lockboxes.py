#!/usr/bin/python3
"""
n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Write a method that determines
    if all the boxes can be opened
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
