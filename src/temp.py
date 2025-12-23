import random
from collections.abc import Iterator

class Arithmatique:

    def __init__(self, nb_operations: int, lower_bound: int, upper_bound: int):

        self.n: int = nb_operations
        self.lower_bound: int = lower_bound
        self.upper_bound: int = upper_bound

    def _get_expression(self) -> str:

        n1 = random.randint(self.lower_bound, self.upper_bound)
        n2 = random.randint(self.lower_bound, self.upper_bound)
        op = random.choice(["add", "sub", "mul", "truediv"])

        op_lut = {"add": (n1.__add__(n2), "+"),
                  "sub": (n1.__sub__(n2), "-"),
                  "mul": (n1.__mul__(n2), "×"),
                  "truediv": (n1.__truediv__(n2), "÷")}
        
        operator = op_lut[op][1]
        equal = op_lut[op][0]

        return f"{n1} {operator} {n2} = {equal}"
    
    def _expression_generator(self) -> Iterator[str]:
        for i in range(self.n):
            yield self._get_expression()
    
    def __str__(self) -> str:
        return "\n".join(f"{i}) {expr}" for i, expr in enumerate(self._expression_generator(), start=1))


session = Arithmatique(10, 0, 30)
print(session)












