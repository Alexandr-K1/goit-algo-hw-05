from collections.abc import Callable
import re

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

def generator_numbers(text: str):
    # робимо шаблон для дійсних чисел
    pattern = r'\d+\.\d+'
    # шукаємо дійсні числа в тексті
    numbers = re.findall(pattern, text)
    # проходимо по кожному дійсному числу
    for number in numbers:
        # перетворюємо отримані числа з строки в дійсні числа для подальшого сумування
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}')
