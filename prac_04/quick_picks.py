import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_LINE))


def display_quick_picks(num_quick_picks):
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


display_quick_picks(NUM_QUICK_PICKS)
