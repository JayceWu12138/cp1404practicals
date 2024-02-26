MINIMUM_LIMIT = 0
MAXIMUM_LIMIT = 100
HIGH_THRESHOLD = 90
LOW_THRESHOLD = 50


def main():
    score = None
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if score is None:
                print("Please get a valid score first.")
            else:
                result = category(score)
                print(f"The result is: {result}")
        elif choice == 'S':
            if score is None:
                print("Please get a valid score first.")
            else:
                show_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < MINIMUM_LIMIT or score > MAXIMUM_LIMIT:
        print("Invalid score. The score must be between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score


def category(score):
    if score >= HIGH_THRESHOLD:
        return "Excellent"
    elif score >= LOW_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


main()
