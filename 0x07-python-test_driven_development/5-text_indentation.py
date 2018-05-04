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

    flag = 0
    new = ""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ' ' and i == 0:
            new += ""
            flag = 1
        elif text[i] == ' ' and flag == 1:
            new += ""
        elif text[i] == ' ' and i - 1 >= 0 and flag == 0\
            and (text[i - 1] == '.' or text[i - 1] == '?'
                 or text[i - 1] == ':'):
            new += ""
        else:
            new += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{:s}".format(new))
            print()
            new = ""
    print("{:s}".format(new), end="")
