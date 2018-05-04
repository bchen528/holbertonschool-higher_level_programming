>>> say_my_name = __import__('3-say_my_name').say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Bob")
My name is Bob 
>>> say_my_name("Bob", 12)
Traceback (most recent call last):
TypeError: last_name must be a string
>>> say_my_name("", "")
My name is  
>>> say_my_name()
Traceback (most recent call last):
TypeError: say_my_name() missing 1 required positional argument: 'first_name'
>>> say_my_name(12, "Bob")
Traceback (most recent call last):
TypeError: first_name must be a string
>>> say_my_name(Tomato)
Traceback (most recent call last):
NameError: name 'Tomato' is not defined
