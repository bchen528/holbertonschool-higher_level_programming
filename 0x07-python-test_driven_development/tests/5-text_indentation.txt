>>> text_indentation = __import__('5-text_indentation').text_indentation
>>> text_indentation("tomato     .   ,,,,/\?00")
tomato     .
<BLANKLINE>
,,,,/\?
<BLANKLINE>
00
>>> text_indentation("....")
.
<BLANKLINE>
.
<BLANKLINE>
.
<BLANKLINE>
.
<BLANKLINE>
>>> text_indentation("")

>>> text_indentation(" .? ")
.
<BLANKLINE>
?
<BLANKLINE>
>>> text_indentation("     .     . ")
.
<BLANKLINE>
.
<BLANKLINE>
>>> text_indentation("  ")

>>> text_indentation(""")
Traceback (most recent call last):
SyntaxError: EOF while scanning triple-quoted string literal
