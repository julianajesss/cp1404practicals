from prac_07.guitar import Guitar


def main():
    """Read guitars and store them in a list of Guitar objects"""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()

    guitars = add_guitars(guitars)

    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    """Add guitar to collection."""
    guitars_count = -1
    for guitar in guitars:
        guitars_count += 1
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        guitars_count += 1
        print(f"{guitars[guitars_count]} added.")
        name = input("Name: ")
    guitars.sort()
    return guitars


main()
