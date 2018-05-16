#!/usr/bin/python3
def append_write(filename="", text=""):
    """append a string at the end of text file
    Args:
        filename(str): filename
        text(str): text to be appended
    Returns:
        number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
