"""Practicing dictionary functions."""

__author__ = "730706009"


def invert(d: dict[str, str]) -> dict[str, str]: 
    """Inverts a dictionary where keys become values and values become keys."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("Duplicate value encountered while inverting dictionary")
        inverted[value] = key
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Finds the most popular color from a dictionary of names and favorite colors."""
    color_count: dict[str, int] = {}
    for name, color in colors.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # This line should be dedented so that it's not part of the for loop
    most_popular_color = max(color_count, key=lambda x: color_count[x], default=None)
    return most_popular_color


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of each value in a list and returns a dictionary."""
    value_counts: dict[str, int] = {}
    for value in values:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    return value_counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes a list of words into different lists by their first letter."""
    categorized_words: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in categorized_words:
            categorized_words[first_letter].append(word)
        else:
            categorized_words[first_letter] = [word]
    return categorized_words


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance log with a student's attendance for a specific day without repeating names."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log