from guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year
    guitars.sort()

    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
