import pytest

from flexeval.expression_ast import Literal, Name, Call
from flexeval.built_in_functions import ADD, MULTIPLY
from flexeval.function_map import FUNCTIONS


@pytest.fixture(scope="module")
def expression():
    return Call(MULTIPLY, Call(ADD, Name("a"), Name("b")), Literal(2))


def test_string_representation(expression):
    assert str(expression) == "*(+(a, b), 2)"


def test_failed_compile():
    expr = Call("unknown", Call(ADD, Name("a"), Name("b")), Literal(2))

    with pytest.raises(NameError) as exc_info:
        expr.compile(FUNCTIONS)

    assert "'unknown'" in exc_info.value.args[0]


def test_successful_eval(expression):
    f = expression.compile(FUNCTIONS)
    assert f(a=1, b=2) == 6


def test_failed_eval(expression):
    f = expression.compile(FUNCTIONS)

    with pytest.raises(TypeError) as exc_info:
        f(a=1)

    assert "'b'" in exc_info.value.args[0]
