import random
MINIMUM_LIMIT = 0
MAXIMUM_LIMIT = 100
HIGH_THRESHOLD = 90
LOW_THRESHOLD = 50


def main():
    user_score = float(input("Enter score: "))
    print(category(user_score))

    random_score = random.uniform(MINIMUM_LIMIT, MAXIMUM_LIMIT)
    print(f"Random score: {random_score:.2f} - {category(random_score)}")


def category(score):
    if score < MINIMUM_LIMIT or score > MAXIMUM_LIMIT:
        return "Invalid score"
    elif score >= HIGH_THRESHOLD:
        return "Excellent"
    elif score >= LOW_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
