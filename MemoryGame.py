def generate_sequence(difficulty):
    import random
    import time
    generated_list = random.sample(range(1, 101), difficulty)
    print(generated_list, end="")
    time.sleep(0.7)
    print("\r", end="", flush=True)
    return generated_list


def get_list_from_user(difficulty):
    user_generated_list = []
    for i in range(1, difficulty + 1):
        user_list_item = int(input(f"Enter number #{i}: "))
        user_generated_list.append(user_list_item)
    return user_generated_list


def is_list_equal(generated_list, user_generated_list):
    if generated_list == user_generated_list:
        return True
    else:
        return False


def play(difficulty):
    return is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
