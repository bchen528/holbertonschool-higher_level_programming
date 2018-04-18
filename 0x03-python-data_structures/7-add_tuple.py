
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_c = []
    for tuple_a, tuple_b in zip(list_a, list_b):
        tuple_c = tuple(a+b for a, b in zip(list_a, list_b))
        list_c.append(tuple_c)
    print (list_c)
