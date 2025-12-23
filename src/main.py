import random

class Arithmatique:
    
    def __init__(self):
        
        self.entries: dict[str, tuple[int, int]] = {}
        self.number_of_questions: int = 4

    def addition(self) -> list[tuple[int, int, int, int]]:
        
        p, q = 0, 100
        n = 10
        lst = []
        
        for i in range(n):
            a = random.randint(p, q)
            b = random.randint(p, q)
            k = random.choice(["add", "sub", "mul", "div"])
            e = a.operator(k)(b)
            lst.append((a, k, b, e))

        return lst


if __name__ == "__main__":

    session = Arithmatique()
    print(session.addition())




