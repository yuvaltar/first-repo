def main():
    num1 = float(input('write your first number: '))
    action = input('write you desired action. +, -, *, /')
    num2 = float(input('write your second number: '))
    result = 0
    calculator(num1, action, num2)

def calculator(num1, action, num2):
    if action == '+':
        result = round(num1 + num2,2)
        print(f'{result:,}')
    elif action == '-':
        result = round(num1 - num2,2)
        print(f'{result:,}')
    elif action == '*':
        result = round(num1 * num2,2)
        print(f'{result:,}')
    else:
        result = round(num1 / num2,2)
        print(f'{result:,}')

    print('hi this is your calculator. please enter, 1 number, 1 action and a, 2 number')
main()


