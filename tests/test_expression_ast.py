import pytest

from flexeval.expression_ast import Literal, Name, Call
from flexeval.functions import Function as Fn
from flexeval.function_map import FUNCTIONS


@pytest.fixture(scope="module")
def expression():
    return Call(Fn.MULTIPLY, Call(Fn.ADD, Name("a"), Name("b")), Literal(2))


def test_string_representation(expression):
    assert str(expression) == "*(+(a, b), 2)"


def test_successful_eval(expression):
    f = expression.compile(FUNCTIONS)
    assert f(a=1, b=2) == 6


def test_failed_eval(expression):
    f = expression.compile(FUNCTIONS)

    with pytest.raises(KeyError) as exc_info:
        f(a=1)

    assert exc_info.value.args[0] == 'b'


