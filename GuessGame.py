def generate_number(difficulty):
    import random
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = int(input(f"Enter your guess between 1 and {difficulty}: "))
    return user_guess


def compare_results(user_guess, secret_number):
    if user_guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    return compare_results(generate_number(difficulty),get_guess_from_user(difficulty))


