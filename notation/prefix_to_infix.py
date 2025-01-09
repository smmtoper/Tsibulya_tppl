def prefix_to_infix(expression: str) -> str:
    if not expression.strip():
        raise ValueError("The input expression is empty.")

    tokens = expression.split()
    stack = []

    for token in reversed(tokens):
        if token.isdigit():
            stack.append(token)
        elif token in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                raise ValueError(f"Invalid expression: operator '{token}' has insufficient operands.")
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
        else:
            raise ValueError(f"Invalid token: '{token}'. Only numbers and operators +, -, *, / are allowed.")

    if len(stack) != 1:
        raise ValueError("Invalid expression: mismatched operators and operands.")

    return stack[0]
