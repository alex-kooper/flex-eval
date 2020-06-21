from operator import add, sub, mul, truediv, neg

FUNCTIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    'neg': neg
}


class Literal:
    def __init__(self, value):
        self.value = value

    def compile(self, _functions):
        return lambda **env: self.value

    def __str__(self):
        return str(self.value)

    repr = __str__


class Name:
    def __init__(self, name):
        self.name = name

    def compile(self, _functions):
        return lambda **env: env[self.name]

    def __str__(self):
        return self.name

    repr = __str__


class Call:
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"{self.name}({', '.join(str(a) for a in self.args)})"

    def compile(self, functions):
        func = functions[self.name]
        compiled_args = [a.compile(functions) for a in self.args]
        return lambda **env: func(*[a(**env) for a in compiled_args])

    repr = __str__
