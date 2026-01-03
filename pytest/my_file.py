from collections.abc import Callable


def will_boil(temp):

    if temp > 100:
        return {"passed": True, "reason": f"{temp}°C greater than 100°C"}
    else:
        return {"passed": False, "reason": f"{temp}°C lower or equal to 100°C"}
    

def verify_functions(input, rules: list[Callable[..., dict[str, bool|str]]]) -> list[str]:

    errors = []

    for rule in rules:
        result = rule(input)
        if not result["passed"]:
            errors.append(result["reason"])

    return errors

if __name__ == "__main__":
    rules = [will_boil]
    print(verify_functions(18, rules))
