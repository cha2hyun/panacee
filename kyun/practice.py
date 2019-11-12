def plus(a, b):
    if type(a) == 'str' or type(b) is str:
        return "input is string"
    else:
        return f"{int(a)} + {int(b)}"


def minus(a, b):
    return int(a) - int(b)


def mul(a, b):
    return int(a) * int(b)


def dev(a, b):
    return int(a) / int(b)


print(plus(10,3))
a= "aaa"
print(a,a)
print(type(a))