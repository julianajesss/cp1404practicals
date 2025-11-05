"""
Estimate: 30mins
Actual: start 14.53
"""
from prac_07.project import Project
import datetime

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
    projects = []
    projects = load_projects(DEFAULT_FILE, projects)
    start_length = len(projects)
    print(f"Loaded {start_length} projects from {DEFAULT_FILE}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_file = input("File to load from: ")
            projects.append(load_projects(in_file, projects))
            print(f"Loaded {len(projects) - start_length} projects from {in_file}")
            start_length = len(projects)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    will_you_save = input("Would you like to save to projects.txt? ").upper()
    if will_you_save == "YES":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects(in_file, projects):
    """Load projects from in_file and append them to projects."""
    projects = projects
    f = open(in_file, "r")
    f.readline()
    for line in f:
        parts = line.strip().split("\t")
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        projects.append(Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4])))
    f.close()
    projects.sort()
    return projects


def save_projects(projects):
    pass


def display_projects(projects):
    not_completed_projects = []
    completed_projects = []
    for project in projects:
        if project.completion == 100:
            completed_projects.append(project)
        else:
            not_completed_projects.append(project)
    if not_completed_projects:
        print("Incomplete projects: ")
        for not_completed_project in not_completed_projects:
            print(not_completed_project)
    if completed_projects:
        print("Completed projects:")
        for completed_project in completed_projects:
            print(completed_project)


def filter_projects(projects):
    pass


def add_project(projects):
    """Add a new project to list projects."""
    print("Let's add a new project")
    try:
        name = input("Name: ")
        date_string = input("Start date (dd/mm/yy): ")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        cost = float(input("Cost estimate: "))
        completion = int(input("Percent complete: "))
        projects.append(Project(name, date, priority, cost, completion))
    except ValueError:
        print("Invalid input.")
    projects.sort()
    return projects


def update_project(projects):
    """Update the percentage and or completion of a project in projects from user input."""
    project_count = 0
    for project in projects:
        project_count += 1
        print(project)
    possible_indexes = project_count - 1
    project_choice = int(input("Project choice: ")) - 1
    if project_choice > possible_indexes:
        print("Not a valid index")
        return projects
    print(projects[project_choice])
    try:
        new_percentage = int(input("New Percentage: "))
        projects[project_choice].completion = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        projects[project_choice].priority = new_priority
    except ValueError:
        pass
    projects.sort()
    return projects


main()
