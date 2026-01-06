from collections.abc import Callable


class PasswordVerifier:

    def __init__(self):
        self.rules: list[Callable] = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def verify(self, input):

        errors: list[str] = []

        for rule in self.rules:
            result = rule(input)
            if not result.get('passed'):
                errors.append(result.get('reason'))
        
        return errors

    

if __name__ == "__main__":
    pass
