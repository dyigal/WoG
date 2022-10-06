def get_money_interval(difficulty, converted_amount):
    interval =  [(converted_amount - (5 - difficulty)), (converted_amount + (5 - difficulty))]
    return interval


def get_guess_from_user(amount):
    user_guess = float(input(f"How many Shekels are {amount} US Dollars? "))
    return user_guess

def play(difficulty):
    from currency_converter import CurrencyConverter
    import random

    amount = random.randint(1, 100)
    currency = CurrencyConverter()
    converted_amount = currency.convert(amount, 'USD', 'ILS')

    return get_money_interval(difficulty, converted_amount)[0] <= get_guess_from_user(amount) <= get_money_interval(difficulty, converted_amount)[1]




