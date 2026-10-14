def calc():
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    num_3 = int(input('Арифметикалык оператор киргиз(+, -, *): '))

    if num_3 == '+':
        print(num_1 + num_2)
    elif num_3 == '-':
        print(num_1 - num_2)
    elif num_3 == '*':
        print(num_1 * num_2)
    elif num_3 == '/':
        print(num_1 / num_2)

calc()