# Алгоритм - написание калькулятор
#1) Ввести число 
#2) Действие 
#3) Ввести второе число 
#4) вывести результат 

num_1 = float(input('>:'))
num_2 = float(input('>:'))
operation = input('>:')

print(operation)
if operation == '+':
    result = num_1 + num_2 
    print(int(result))
elif operation == '-':
    result = num_1 - num_2
    print(int(result))


