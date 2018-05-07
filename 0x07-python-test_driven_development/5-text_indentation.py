#!/usr/bin/python3
"""
prints text in special format
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text (str): a string

    Raises:
        TypeError: if text is not a string
    """
    new = ""
    substring = ""
    temp = [] * 2
    flag = 0
    count = 0
    space = [] * 2

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if i < len(text) and text[i] == '.' or text[i] == '?'\
           or text[i] == ':':
            if flag == 0:
                temp = text.split(text[i], 1)
                flag = 1
            else:
                temp = substring.split(text[i], 1)
            new += temp[0].lstrip(' ') + text[i]
            substring = temp[1]
            print("{:s}".format(new))
            print()
            new = ""
    print("{:s}".format(substring.lstrip(' ')), end="")
