from prac_06.guitar import Guitar

tehe = Guitar("tehe", 1000, 0)
tehehe = Guitar("tehehe", 2025, 400000000000.055)
print(tehe)
print(tehehe)
print(f"{tehe.name}, get_age() - expected 1025 got {tehe.get_age()}")
print(f"{tehehe.name}, get_age() - expected 0 got {tehehe.get_age()}")
print(f"{tehe.name}, is_vintage() - expected True got {tehe.is_vintage()}")
print(f"{tehehe.name}, is_vintage() - expected False got {tehehe.is_vintage()}")