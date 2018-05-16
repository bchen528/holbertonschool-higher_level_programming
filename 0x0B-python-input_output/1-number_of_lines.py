#!/usr/bin/python3
def number_of_lines(filename=""):
    """find number of lines in file
    Args:
        filename(str): filename
    Returns:
        number of lines in file
    """
    line_count = 0
    with open(filename, mode="r", encoding="utf-8") as a_file:
        for a_line in a_file:
            line_count += 1
    return line_count
