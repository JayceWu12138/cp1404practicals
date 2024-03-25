COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff",
    "BlueViolet": "#8a2be2",
}
print("Enter a colour name to get its hexadecimal code. Leave blank to stop.")
colour_name = input("Colour Name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} => {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Colour Name: ").title()
