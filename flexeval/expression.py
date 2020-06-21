import ast

from .expression_ast import Literal, Name, Call
from .built_in_functions import *
from .function_map import FUNCTIONS

BINARY_OP_MAP = {
    ast.Add: ADD,
    ast.Sub: SUBTRACT,
    ast.Mult: MULTIPLY,
    ast.Div: DIVIDE
}

UNARY_OP_MAP = {
    ast.UAdd: POSITIVE,
    ast.USub: NEGATE
}


class Expression:
    def __init__(self, expr_str):
        self.expr_str = expr_str

    def parse(self):
        root_node = ast.parse(self.expr_str, mode="eval")
        return self._convert_node(root_node.body)

    def compile(self, functions=FUNCTIONS):
        return self.parse().compile(functions)

    def _convert_node(self, node):
        if isinstance(node, ast.Num):
            return Literal(node.n)

        if isinstance(node, ast.Str):
            return Literal(node.s)

        if isinstance(node, ast.Name):
            return Name(node.id)

        if isinstance(node, ast.BinOp):
            return Call(
                BINARY_OP_MAP[type(node.op)],
                self._convert_node(node.left),
                self._convert_node(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return Call(UNARY_OP_MAP[type(node.op)], self._convert_node(node.operand))
