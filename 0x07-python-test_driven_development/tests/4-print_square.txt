>>> print_square = __import__('4-print_square').print_square
>>> print_square(4)
####
####
####
####
>>> print_square(-1)
Traceback (most recent call last):
ValueError: size must be >= 0
>>> print_square(2.0)
Traceback (most recent call last):
TypeError: size must be an integer
>>> print_square(0)

>>> print_square(.999)
Traceback (most recent call last):
TypeError: size must be an integer
>>> print_square(0.00)
Traceback (most recent call last):
TypeError: size must be an integer
>>> print_square(-1.0)
Traceback (most recent call last):
TypeError: size must be an integer
>>> print_square(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>> print_square('a')
Traceback (most recent call last):
TypeError: size must be an integer
>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'
>>> print_square(2a)
Traceback (most recent call last):
SyntaxError: invalid syntax
