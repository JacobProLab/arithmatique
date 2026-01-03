from my_file import will_boil, verify_functions

def fake_will_boil(temp):
    return {"passed": False, "reason": f"{temp}°C lower or equal to 100°C"}

def test_verify_functions():
    
    # Arrange
    fake_temp = 90
    fake_rules = [fake_will_boil]
    
    # Act
    errors = verify_functions(fake_temp, fake_rules)

    # Assert
    assert errors[0] == f"{fake_temp}°C lower or equal to 100°C"

