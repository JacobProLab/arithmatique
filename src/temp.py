import sys
import random
import operator
import logging
import pandas as pd
import math

from pprint import pprint
from fractions import Fraction

f = Fraction(20, 95)

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

class Arithmatique:

    def __init__(self, nb_operations: int, low_bound: int, up_bound: int):

        self.n: int = nb_operations

        self.low_bound: int = low_bound
        self.up_bound: int = up_bound

        self.op_LUT = {
            "+": operator.add,
            "-": operator.sub,
            "x": operator.mul,
            "/": operator.truediv
        }

    def is_integer(self, num):
        return num % 1 == 0
    
    def get_random_integers(self) -> tuple[int, int]:

        max_val = int(math.sqrt(max(abs(self.low_bound), abs(self.up_bound))))
        a = 0
        b = 0

        while a == 0 or b == 0:
            a = random.randint(-max_val, max_val)
            b = random.randint(-max_val, max_val)

        return (a, b)
    
    def get_random_operator(self) -> str:
        return random.choice(list(self.op_LUT.keys()))

    def get_valid_expression(self, operator) -> dict[str, int|str]:

        # Make sure result is in [low; up] and is an integer
        result = self.low_bound - 1
        while not (self.low_bound <= result <= self.up_bound and self.is_integer(result)):
            a, b = self.get_random_integers()
            result = self.op_LUT[operator](a, b)

        return {"num1": a,
                "operator": operator,
                "num2": b,
                "result": f"{result:.0f}"}
    
    def get_n_expressions(self):
        
        # Make sure returned expression list have about the same count for each type
        quotient, remainder = divmod(self.n, len(self.op_LUT))

        expressions = []
        for op_symbol in self.op_LUT.keys():
            for j in range(quotient):
                expressions.append(self.get_valid_expression(op_symbol))
        for i in range(remainder):
            expressions.append(self.get_valid_expression(self.get_random_operator()))

        random.shuffle(expressions)
        
        return expressions
    
    def __str__(self) -> str:

        expressions = self.get_n_expressions()

        max_i = len(str(self.n))

        df = pd.DataFrame(expressions)
        cols = ['num1', 'num2', 'result']
        max_lens = df[cols].astype(str).map(len).max().to_dict()
        
        result = []
        for i, values in enumerate(expressions, start=1):
            string = "{:>{i}}) {:>{num1}}{:^3}{:<{num2}} = {:>{result}}".format(i, *values.values(), i=max_i, **max_lens)
            result.append(string)

        return "\n".join(expr for expr in result)


if __name__ == "__main__":
    session = Arithmatique(10, 0, 200)
    print(session)


