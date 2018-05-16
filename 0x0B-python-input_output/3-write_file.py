#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename(str): filename
        text(str): text to write
    Returns:
        number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
