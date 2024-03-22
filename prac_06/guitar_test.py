from guitar import Guitar


def test_guitar():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 999.99)
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    vintage_test_guitar = Guitar("Vintage Test", 1974, 5000)
    print(f"50-year old guitar is_vintage() - Expected True. Got {vintage_test_guitar.is_vintage()}")


test_guitar()
