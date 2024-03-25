import csv


def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = [row for row in reader]
    return data


def count_champions_wins(data):
    wins = {}
    for row in data:
        champion = row[2]
        if champion in wins:
            wins[champion] += 1
        else:
            wins[champion] = 1
    return wins


def get_unique_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champions_wins = count_champions_wins(data)
    unique_countries = get_unique_countries(data)
    print("Wimbledon Champions:")
    for champion, wins in champions_wins.items():
        print(f"{champion} {wins}")
    sorted_countries = sorted(unique_countries)
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted_countries))


if __name__ == "__main__":
    main()
