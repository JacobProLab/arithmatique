from my_file import PasswordVerifier
from re import search, IGNORECASE

def fake_rule(temp):
    return {"passed": False, "reason": "fake reason"}


def test_verify_functions():

    verifier = PasswordVerifier()
    fake_input = 'any value'
    verifier.add_rule(fake_rule)

    errors = verifier.verify(fake_input)

    for error in errors:
        assert search(r'fake reason', error, IGNORECASE)


def test_divide():
    pass
