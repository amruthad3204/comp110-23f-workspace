"""Combining two lists into a dictionary."""

__author__ = "730706009"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Combining a list of strings with a list of integers to create a dictionary."""
    if len(str_list) != len(int_list) or not str_list:
        return {}

    return {str_list[i]: int_list[i] for i in range(len(str_list))}