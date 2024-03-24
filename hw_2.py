
import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    gen = func(text)
    return sum(gen)

# Example usage
text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
result = sum_profit(text, generator_numbers)
print(result)

