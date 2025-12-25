import sys
import random
import logging


logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

class Arithmatique:

    def __init__(self, nb_operations: int, lower_bound: int, upper_bound: int):

        self.n: int = nb_operations
        self.lower_bound: int = lower_bound
        self.upper_bound: int = upper_bound

    def _get_expression(self) -> tuple:

        # Retrieve random variables' values
        n1 = random.randint(self.lower_bound, self.upper_bound)
        n2 = 0
        while n2 == 0:
            n2 = random.randint(self.lower_bound, self.upper_bound)
        op = random.choice(["add", "sub", "mul", "truediv"])

        op_lut = {"add": (n1.__add__(n2), "+"),
                  "sub": (n1.__sub__(n2), "-"),
                  "mul": (n1.__mul__(n2), "×"),
                  "truediv": (n1.__truediv__(n2), "÷")}
        
        operator = op_lut[op][1]
        equal = op_lut[op][0]

        # Assert only whole number results are given if operator == truediv
        if equal % 1:
            while equal % 1:
                n2 = 0
                while n2 == 0:
                    n2 = random.randint(self.lower_bound, self.upper_bound)
                equal = n1.__truediv__(n2)

        return (n1, operator, n2, int(equal))
    
    def __str__(self) -> str:

        expressions = [self._get_expression() for i in range(self.n)]

        max_i = len(str(self.n))
        max_a = max(len(str(values[0])) for values in expressions)
        max_b = max(len(str(values[2])) for values in expressions)
        max_e = max(len(str(values[-1])) for values in expressions)
        
        result = []
        for i, values in enumerate(expressions, start=1):
            string = "{:>{i}}) {:>{a}}{:^3}{:<{b}} = {:>{e}}".format(i, *values, i=max_i, a=max_a, b=max_b, e=max_e)
            result.append(string)

        return "\n".join(expr for expr in result)


if __name__ == "__main__":
    session = Arithmatique(10, 0, 50)
    print(session)












