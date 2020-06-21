
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
    def __init__(self, function, *args):
        self.function = function
        self.args = args

    def __str__(self):
        return f"{self.function.value}({', '.join(str(a) for a in self.args)})"

    def compile(self, functions):
        func = functions[self.function]
        compiled_args = [a.compile(functions) for a in self.args]
        return lambda **env: func(*[a(**env) for a in compiled_args])

    repr = __str__
