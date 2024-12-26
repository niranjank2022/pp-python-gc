from typing import List


MEMORY = [None] * 10
REFERENCES = dict()

def evaluate_expression(infix: List[str]):
    ...
    # postfix = []
    # stack = []
    # for token in infix:
    #     # if token 

def run_program():


    """
    Note that each input is of the grammar:
    stat : id = expr
    expr :      expr + expr
            |   expr - expr
            |   expr * expr
            |   expr / expr
            |   -expr
            |   ( expr )
            |   id
    """
    while True:

        print(">>", end=" ")
        input_line = input()
        tokens = input_line.split(" ")
        lhs = tokens[0]
        rhs = evaluate_expression(tokens[2:])
