"""EX04 - Utils."""

__author__ = "730706009"


from typing import List


def all(nums: List[int], target: int) -> bool:
    """Check if all elements in the list are equal to the target.
    
    Args:
        nums (list): A list of integers.
        target (int): The integer to compare against.

    Returns:
        bool: True if all numbers match the indicated number, False otherwise or if the list is empty.
    """
    if not nums:
        return False  # Return False for an empty list
    for num in nums:
        if num != target:
            return False  # Return False if any number is not equal to the target
    return True  # Return True if all numbers are equal to the target


def max(nums: List[int]) -> int:
    """Find the maximum number in a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not nums:
        raise ValueError("max() arg is an empty List")  # Raise a ValueError for an empty list
    max_num = nums[0]  # Initialize max_num with the first element of the list
    for num in nums:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num


def is_equal(list1: List[int], list2: List[int]) -> bool:
    """Check if two lists of integers are equal element-wise.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        bool: True if the lists are equal element-wise, False otherwise.
    """
    if len(list1) != len(list2):
        return False  # Return False if the lengths of the lists are not equal
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False  # Return False if any element at the same index is not equal
    return True  # Return True if all elements at every index are equal