import pytest
from prefix_to_infix_logic import prefix_to_infix

def test_valid_expressions():
    assert prefix_to_infix("+ - 13 4 55") == "((13 - 4) + 55)"
    assert prefix_to_infix("+ 2 * 2 - 2 1") == "(2 + (2 * (2 - 1)))"
    assert prefix_to_infix("+ + 10 20 30") == "((10 + 20) + 30)"
    assert prefix_to_infix("- 1 2") == "(1 - 2)"
    assert prefix_to_infix("/ + 3 10 * + 2 3 - 3 5") == "((3 + 10) / ((2 + 3) * (3 - 5)))"

def test_empty_expression():
    with pytest.raises(ValueError):
        prefix_to_infix("")

def test_invalid_tokens():
    with pytest.raises(ValueError):
        prefix_to_infix("+ 2 a 3")
    with pytest.raises(ValueError):
        prefix_to_infix("* 2 3 &")

def test_insufficient_operands():
    with pytest.raises(ValueError):
        prefix_to_infix("+ 2")
    with pytest.raises(ValueError):
        prefix_to_infix("+ + 2 3")

def test_mismatched_operators_and_operands():
    with pytest.raises(ValueError):
        prefix_to_infix("+ 2 3 4")

if __name__ == "__main__":
    pytest.main()
