import random
import operator


class Arithmatique:
    def __init__(self, nb_operations: int, low_bound: int, up_bound: int):
        self.n: int = nb_operations

        self.low_bound: int = low_bound
        self.up_bound: int = up_bound

        self.op_LUT = {
            "+": operator.add,
            "-": operator.sub,
            "x": operator.mul,
            "/": operator.truediv,
        }

    def is_integer(self, num):
        return num % 1 == 0

    def get_random_operator(self) -> str:
        return random.choice(list(self.op_LUT.keys()))

    def get_random_integers(self):
        pass

    def get_valid_expression(self):
        pass

    def get_n_expressions(self):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    session = Arithmatique(10, 0, 200)
    print(session)
