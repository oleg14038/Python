# Алгоритм - написание калькулятор
#1) Ввести число 
#2) Действие 
#3) Ввести второе число 
#4) вывести результат 


operation_list = ['+', '-', '/', '*']


def calculate(num_1, math_, num_2):
    """Prints to console result"""

    match math_:
        case '+':
            if '.' in (num_1 + num_2):
                result = float(num_1).__add__(float(num_2))
            else:
                result = int(num_1).__add__(int(num_2))     
            print(f'\n{num_1} {math_} {num_2} = {result}\n')
        case '-':
            if '.' in (num_1 + num_2):
                result = float(num_1).__sub__(float(num_2))
            else:
                result = int(num_1).__sub__(int(num_2))
            print(f'\n{num_1} {math_} {num_2} = {result}\n')
        case '/':
            result = float(num_1).__truediv__(float(num_2))
            result = int(result) if str(result)[-1] == '0' else float(result)
            print(f'\n{num_1} {math_} {num_2} = {result}\n')
        case '*':
            if '.' in (num_1 + num_2):
                result = float(num_1).__mul__(float(num_2))
            else:
                result = int(num_1).__mul__(int(num_2))
            print(f'\n{num_1} {math_} {num_2} = {result}\n')
        case _:
            print('unknown operation')


def check_input_data(n1, opr, n2):
    """Check incoming data"""
    pass


def run_calc():
    num_1 = input('Input first number:')
    operation = input('Input an math operation(+,-,/,*): ')
    num_2 = input('Input second number:')
    calculate(num_1, operation, num_2)


run_calc()



