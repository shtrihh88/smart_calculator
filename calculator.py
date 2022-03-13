# write your code here
def check_command(a: str):
    """Check startswith string"""
    if a is not None and a.startswith('/'):
        return correct_command(a)
    return a


def correct_command(a: str):
    """Check correct command"""
    if a == '/help':
        print('This is my smart calculator')
    elif a == '/exit':
        print('Bye!')
        return exit()
    else:
        print('Unknown command')


def check_parentheses(sequence: str):
    """Check correct count brackets"""
    brackets = []
    for i in sequence:
        if i == '(':
            brackets.append(i)
        elif i == ')' and brackets:
            if brackets[-1] == '(':
                brackets.pop()
        elif i == ')' and not brackets:
            print('Invalid expression')
            return None
    if brackets:
        print('Invalid expression')
    else:
        return sequence


def valid_expression(a: str, val: dict):
    if a is not None and '=' in a:
        a = a.split('=')
        key = a[0].strip()
        value = a[1].strip()
        if key.isdigit() or not check_value(key):
            print('Invalid identifier')
        elif len(a) > 2 or not check_value(value):
            print('Invalid assignment')
            return None
        elif value in val:
            val[key] = val[value]
        else:
            try:
                val[key] = int(value)
            except ValueError:
                print('Unknown variable')
        return val if val else None
    return a


def check_value(value):
    count_let = 0
    count_dig = 0
    for letter in value:
        if letter.isalpha():
            count_let += 1
        elif letter.isdigit():
            count_dig += 1
    if count_let and count_dig:
        return False
    return True


def check_input(a: str):
    """Check input"""
    if a == '' or a is None:
        return None
    elif '//' in a:
        print('Invalid expression')
    else:
        a = a.replace('^', '**')
        return a


def calculate(a: str, variable: dict):
    """Result calculate"""
    for value in a:
        if value in variable:
            a = a.replace(value, str(variable[value]))
    try:
        print(int(eval(a)))
    except SyntaxError:
        print('Invalid expression')
    except NameError:
        print('Unknown variable')


def main():
    values_dict = {}
    while True:
        sequence = input().strip()
        sequence = check_parentheses(sequence)
        sequence = check_command(sequence)
        sequence = check_input(sequence)
        sequence = valid_expression(sequence, values_dict)
        if isinstance(sequence, dict):
            values_dict.update(sequence)
            continue
        if sequence is None:
            continue
        calculate(sequence, values_dict)


main()
