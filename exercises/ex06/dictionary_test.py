"""Importing Dictionary Functions."""

__author__ = "730706009"

# test_dictionary.py

import pytest

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Unit tests for invert function
def test_invert_expected_use_case():
    """Test the invert function with an expected use case."""
    d = {'a': '1', 'b': '2', 'c': '3'}
    inverted = invert(d)
    assert inverted == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_edge_case():
    """Test the invert function with an edge case where duplicate values are encountered."""
    d = {'a': '1', 'b': '1'}
    with pytest.raises(KeyError):
        invert(d)


def test_invert_empty_dict():
    """Test the invert function with an empty dictionary."""
    d = {}
    inverted = invert(d)
    assert inverted == {}


# Unit tests for favorite_color function
def test_favorite_color_expected_use_case():
    """Test the favorite_color function with an expected use case."""
    colors = {'Alice': 'Red', 'Bob': 'Blue', 'Carol': 'Red'}
    most_popular = favorite_color(colors)
    assert most_popular


def test_favorite_color_edge_case():
    """Test the favorite_color function with an edge case where the input dictionary is empty."""
    colors = {}
    most_popular = favorite_color(colors)
    assert most_popular is None


def test_favorite_color_tiebreaker():
    """Test the favorite_color function with a tiebreaker scenario."""
    colors = {'Alice': 'Red', 'Bob': 'Blue', 'Carol': 'Blue', 'David': 'Green'}
    most_popular = favorite_color(colors)
    assert most_popular == 'Blue'


# Unit tests for count function
def test_count_expected_use_case():
    """Test the count function with an expected use case."""
    values = ['a', 'b', 'a', 'c', 'b', 'a']
    value_counts = count(values)
    assert value_counts == {'a': 3, 'b': 2, 'c': 1}


def test_count_edge_case():
    """Test the count function with an edge case where the input list is empty."""
    values = []
    value_counts = count(values)
    assert value_counts == {}


def test_count_duplicate_values():
    """Test the count function with a case where there are duplicate values."""
    values = ['a', 'b', 'a', 'c', 'b', 'a', 'c', 'a']
    value_counts = count(values)
    assert value_counts == {'a': 4, 'b': 2, 'c': 2}


# Unit tests for alphabetizer function
def test_alphabetizer_expected_use_case():
    """Test the alphabetizer function with an expected use case."""
    words = ['apple', 'banana', 'avocado', 'cherry', 'blueberry']
    categorized = alphabetizer(words)
    assert categorized == {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}


def test_alphabetizer_edge_case():
    """Test the alphabetizer function with an edge case where the input list is empty."""
    words = []
    categorized = alphabetizer(words)
    assert categorized == {}


def test_alphabetizer_numbers_and_symbols():
    """Test the alphabetizer function with a case containing numbers and symbols."""
    words = ['apple', '123banana', '@avocado', 'cherry', '!blueberry']
    categorized = alphabetizer(words)
    assert categorized == {'a': ['apple', '@avocado'], 'b': ['123banana', '!blueberry'], 'c': ['cherry']}


# Unit tests for update_attendance function
def test_update_attendance_expected_use_case():
    """Test the update_attendance function with an expected use case."""
    attendance_log = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Carol']}
    updated_log = update_attendance(attendance_log, 'Monday', 'Eve')
    assert updated_log == {'Monday': ['Alice', 'Bob', 'Eve'], 'Tuesday': ['Carol']}


def test_update_attendance_edge_case():
    """Test the update_attendance function with an edge case where the input log is empty."""
    attendance_log = {}
    updated_log = update_attendance(attendance_log, 'Wednesday', 'Frank')
    assert updated_log == {'Wednesday': ['Frank']}


def test_update_attendance_no_repeated_names():
    """Test that the same name is not repeated within a day."""
    attendance_log = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Carol']}
    updated_log = update_attendance(attendance_log, 'Monday', 'Alice')
    assert updated_log == {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Carol']}  # Alice is not repeated


if __name__ == '__main__':
    pytest.main()