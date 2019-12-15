#ask user for expression
def main():
    expr = input("Enter an expression: ")
    variables = dict()

    if program(expr, variables):
        for variables, value in variables.items():
            print(variables + " = " + str(value))

    else:
        print("error")

#parse program
def program(expr,variables):
    while len(expr) > 0:
        exp = assignment(expr, variables)
    if expr is False:
        return False
    return True

# parse assigmnet
def assignment(expr, variables):
    expr = expr.lstrip()

    new_expr, new_identifier = identifier(expr)

    if new_expr is False:
        return False
    expr = new_expr.lstrip()
    if expr[0] != '=':
        return False
    expr = expr[1:]

    new_expr, value = expression(expr,variables)

    if new_expr is False:
        return False

    expr = new_expr.lstrip()

    if expr.startwith(','):
        variables[identifier] = value
        return expr[1:]
    return False

#parse expression
def expression(expr,variables):
    expr = expr.lstrip()

    expr, value = term(expr, variables)

    if expr is not False:
        expr = expr.lstrip()
    if expr.startswith("+"):
        new_expr, next_value = expression(expr[1:], variables)
    if new_expr is not False:
        return new_expr, value + next_value

    if expr.startswith("-"):
        new_expr, next_value = expression(expr[1:], variables)
    if new_expr is not False:
        return new_expr, value - next_value
    return expr, value
    return False, None

# parse term
def term(expr, variables):
    expr = expr.lstrip()
    expr, value = fact(expr, variables)

    if expr is not False:
        expr = expr.lstrip()
    if expr.startswith("*"):
        new_expr, next_value = term(expr[1:], variables)
    if new_expr is not False:
        return new_expr, value * next_value
    return expr, value
    return False, None

# parse fact
def fact(expr, variables):
    expr = expr.lstrip()
    if expr.startswith('('):
        new_expr, value = expression(expr[1:], variables)
    if new_expr is not False and new_expr.startswith(')'):
        return new_expr[1:], value
    if expr.startswith('-') or expr.startswith('+'):
        new_expr, value = fact(expr[1:], variables)
    if new_expr is not False:
        if expr.startswith('-'):
            return new_expr, -value
    else:
        return new_expr, value
    new_expr, value = literal(expr)
    if new_expr is not False:
        return new_expr, value
    new_expr, new_identifier = identifier(expr)
    if identifier not in variables.keys():
        print(identifier + " is not initialized")
        return False, None
    if new_expr is not False:
        return new_expr, variables[identifier]
    return False, None

# parse literal
def literal(expr):
    expr = expr.lstrip()
    if expr.startswith('0'):
        return expr[1:], 0
    if len(expr) == 0 or not '1' <= expr[0] <= '9':
        return False, None
    literal = expr[0]
    expr = expr[1:]
    while len(expr) > 0 and '0' <= expr[0] <= '9':
        literal += expr[0]
        expr = expr[1:]
        return expr, int(literal)
# parse identifier
def identifier(expr):
    expr = expr.lstrip()
    identifier = ""
    if not ('a' <= expr[0] <= 'z') and not ('A' <= expr[0] <= 'Z'):
        return False, None

    identifier += expr[0]
    expr = expr[1:]

    while len(expr) > 0:
        if 'a' <= expr[0] <= 'z' or 'A' <= expr[0] <= 'Z' or '0' <= expr[0] <= '9' or expr[0] == '_':
            identifier += expr[0]
            expr = expr[1:]
            continue
            break
            return expr, identifier

        if __name__ == '__main__':
            main()




















