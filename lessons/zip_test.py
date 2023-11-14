"""Test my zip function."""

__author__ = "730706009"


from typing import List, Dict


def zip(str_list: List[str], int_list: List[int]) -> Dict[str, int]:
    """Combining a list of strings with a list of integers to create a dictionary."""
    if len(str_list) != len(int_list) or not str_list:
        return {}

    return {str_list[i]: int_list[i] for i in range(len(str_list))}


def test_zip_edge_case_empty_lists() -> None: 
    """Test zip function with empty input lists."""
    str_list = []
    int_list = []
    result = zip(str_list, int_list)
    assert result == {}  # Expected an empty dictionary for empty lists


def test_zip_use_case() -> None:
    """Test zip function with two use cases."""
    # Use Case 1: Matching lists of strings and integers
    str_list = ["apple", "banana", "cherry"]
    int_list = [1, 2, 3]
    result = zip(str_list, int_list)
    assert result == {"apple": 1, "banana": 2, "cherry": 3}  # Use Case 1 failed

    # Use Case 2: Lists of different lengths
    str_list = ["one", "two", "three"]
    int_list = [1, 2]
    result = zip(str_list, int_list)
    assert result == {}  # Use Case 2 failed due to lists of different lengths


def test_zip_edge_case_single_element() -> None: 
    """Test zip function with lists containing a single element."""
    str_list = ["apple"]
    int_list = [5]
    result = zip(str_list, int_list)
    assert result == {"apple": 5}  # Edge Case: Single element test failed


if __name__ == "__main__":
    """Running all the tests and printing if they passed."""
    test_zip_edge_case_empty_lists()
    test_zip_use_case()
    test_zip_edge_case_single_element()
    print("All tests passed!")