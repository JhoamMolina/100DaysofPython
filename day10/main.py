# def my_funtion():
#     result = 3 * 2
#     return result


# def format_name(f_name, l_name):
#     """Takes first and last name and format it to return a capitalize word"""
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"


# print(format_name("jhoam", "MOLINA"))

# Calculator


def add(n1, n2):
    """ Sums two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """ Subtracts two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """ Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """ Divides two numbers """
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def opearte_number(num1, num2, operator):
    """This function takes 2 number a operator and does the opeartion"""
    calculation_fuction = operations[operator]

    answer = calculation_fuction(num1, num2)

    return answer


def calculator():

    num1 = int(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    operation_symbol = input("Pick an operation from the line aboe: ")
    num2 = int(input("What's the second number?: "))

    answer = opearte_number(num1, num2, operation_symbol)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while True:

        want_to_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

        if want_to_continue == "n":
            break
            calculator()

        operation_symbol = input("Pick an operation: ")
        extra_number = int(input("What's the next number?: "))
        old_first_number = answer
        answer = opearte_number(answer, extra_number, operation_symbol)
        print(f"{old_first_number} {operation_symbol} {extra_number} = {answer}")
