import re

def generator_numbers(text:str):
    pattern = r"\b\d+\.\d+\b|\b\d+\b"
    num = re.findall(pattern, text)
    for i in num:
        yield float(i)


def sum_profit(text: str, func: callable):
    number_generator = func(text)
    total = sum(number_generator)
    return total


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    main()  