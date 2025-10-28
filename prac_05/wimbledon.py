"""
Wimbledon
Estimate: 20 minutes
Actual:   43 minutes
"""


def main():
    """Get wimbledon winners from file and print winners of wimbledon"""
    winners_to_wins, countries = format_winners()
    print_winners(countries, winners_to_wins)


def print_winners(countries, winners_to_wins):
    """Print winners or wimbledon"""
    print("Wimbledon Champions:")
    for winner in winners_to_wins:
        print(f"{winner} {winners_to_wins[winner]}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def format_winners():
    """Format winners of wimbledon"""
    winners_to_wins = {}
    countries = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            winner_data = line.split(",")
            del winner_data[0]
            extra_fields = len(winner_data) - 2
            for i in range(extra_fields):
                del winner_data[-1]

            if winner_data[1] in winners_to_wins:
                winners_to_wins[winner_data[1]] += 1
            else:
                winners_to_wins[winner_data[1]] = 1
            if winner_data[0] not in countries:
                countries.append(winner_data[0])
            countries.sort()
    return winners_to_wins, countries


main()
