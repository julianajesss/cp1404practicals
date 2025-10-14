COLOUR_TO_HEX = {
    "Amethyst": "#9966cc",
    "BlueViolet": "#8a2be2",
    "Bright Lavender": "#bf94e4",
    "Bright Ube": "#d19fe8",
    "Byzantium": "#702963",
    "Dark Byzantium": "#5d3954",
    "Dark Lavender": "#734f96",
    "DarkOrchid": "#9932cc",
    "DarkOrchid4": "#68228b",
    "DarkViolet": "#9400d3",
}
# print(COLOUR_TO_HEX)

colour_name = input("Enter the colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Colour not found in dictionary")
    colour_name = input("Enter the colour name: ").title()

# for colour in COLOUR_TO_HEX:
#     print(f"{colour:15} is {COLOUR_TO_HEX[colour]}")
