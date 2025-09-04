def calculate_sum():

    def get_nums():
        a = int(input("Enter first слагаемое: "))
        b = int(input("Enter second слагаемое: "))
        return a, b

    def calc_sum(a, b):
        sum = a + b
        return sum

    def print_output():
        a, b = get_nums()
        print("Summa = ", calc_sum(a, b))

    print_output()

def check_nums_for_parity():
    def get_count():
        count = int(input("Введите число: "))
        return count

    def check_count(count):
        if count in (228, 69, 1488):
            output = 'Иди нахуй'
        elif count % 2 == 0:
            output = 'Четное, намана'
        else:
            output = 'Нечетное, бывает'
        return output

    def print_output():
        count = get_count()
        print(check_count(count))

    print_output()

def make_tablice_umnojeniya():
    for i in range(2, 10):
        for k in range(2, 10):
            print(i, " * ", k, " = ", i * k)

def game_guess_number():
    def make_number():
        import random
        num = random.randint(1, 10)
        return num
    
    def game():
        game_num = make_number()
        try:
            player_num = int(input("Угадай число от 1 до 10: "))
            if player_num in (228, 1488, 69) or player_num not in range(1, 11):
                print('Иди нахуй')
            elif player_num == game_num:
                print('Ебать ты ферзь')
            else:
                print('Неверно, правильный ответ - ', game_num)
        except ValueError:
            print('ЧИСЛО А НЕ ЭТУ ХНЙЮ')

    game()

def calculate_something():

    def split_for_calc():
        input_text = input('Введите рассчитываемое выражение в формате a [действе] b: ')
        task = input_text.split(' ')
        return task

    def calculator(task):
        try:
            a, b = float(task[0]), float(task[2])
            if task[1] == '+':
                result = a + b
            elif task[1] == '-':
                result = a - b
            elif task[1] in ('*', 'x'):
                result = a * b
            elif task[1] == '/':
                result = a / b
            else:
                result = 'Че ты высрал'
            return result
        except ValueError:
            return 'Нормально блядь напиши'
        except ZeroDivisionError:
            return 'На ноль делить нельзя'

    def print_result():
        result = calculator(split_for_calc())
        if result is not None:
            print(result)
        else:
            print('Пидор')

    print_result()
