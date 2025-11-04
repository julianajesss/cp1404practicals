"""
Estimate: 30mins
Actual: start 14.53
"""
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new "
        "project\n- (U)pdate project\n- (Q)uit")
DEFAULT_FILE = "projects.txt"


def main():
    """A menu with options to:
    load projects from a file,
    save projects to a file,
    display projects,
    filter projects by date,
    add new projects,
    and update projects."""

    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    start_length = len(projects)
    print(f"Loaded {start_length} projects from {DEFAULT_FILE}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_file = input("File to load from: ")
            projects.appened(load_projects(in_file))
            print(f"Loaded {len(projects) - start_length} projects from {in_file}")
            start_length = len(projects)
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    will_you_save = input("Would you like to save to projects.txt? ").upper()
    if will_you_save == "YES":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects(DEFAULT_FILE):
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects():
    pass


def add_project():
    pass


def update_project():
    pass


main()
