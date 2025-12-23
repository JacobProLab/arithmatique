import random

class Arithmatique:
    def __init__(self):
        self.entries: dict[str, tuple[int, int]] = {}
        self.number_of_questions: int = 4

    def addition(self) -> None:
        
        p, q = 0, 100
        n = 10
        lst = []
        
        for i in range(n):
            a = random.randint(p, q)
            b = random.randint(p, q)
            k = random.choice(["add", "sub", "mul", "div"])
            e = a.operator(k)(b)
            lst.append((a, k, b, e))
    
    def __str__(self) -> None:
        
        for i, values in enumerate(lst, start=1):
            a, k, b, e = values
            string = "{}) {}{}{} = {}".format(i, *values)
            print(string)


if __name__ == "__main__":
    session = Arithmatique()
    session.addition()
    print(session.validate_answers())
