from flexeval.expression import Expression


def test_successful_parse():
    assert str(Expression("(a + b) * -2").parse()) == "*(+(a, b), negate(2))"
    assert str(Expression("'a' + 'b'").parse()) == "+('a', 'b')"


def test_compile():
    f = Expression("(a + b) * 2").compile()
    assert f(a=1, b=2) == 6
