while True:
    num1 = input('Enter First Number: ')

    operator = input('Enter Operator (+, -, *, /): ')

    num2 = input('Enter Second Number: ')

    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    else:
        result = 'Invalid Operator'

    print(f'Result: {result}')

    choice = input('Do you want to continue?(Yes/No): ')
    if choice.lower() == 'no':
        break
