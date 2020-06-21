from operator import add, sub, mul, truediv, neg, pos
from .functions import Function

FUNCTIONS = {
    Function.ADD: add,
    Function.SUBTRACT: sub,
    Function.MULTIPLY: mul,
    Function.DIVIDE: truediv,
    Function.NEGATE: neg,
    Function.POSITIVE: pos
}
