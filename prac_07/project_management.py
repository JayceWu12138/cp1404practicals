from project import Project
import datetime


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            projects.append(Project(*line.strip().split('\t')))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(complete, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_input, "%d/%m/%y").date()
    filtered = [project for project in projects if project.start_date > date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        selected_project.completion_percentage = int(new_percentage)
    if new_priority:
        selected_project.priority = int(new_priority)


def main():
    projects = load_projects('projects.txt')
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")

    actions = {"l": load_projects, "s": save_projects, "d": display_projects,
               "f": filter_projects_by_date, "a": add_new_project, "u": update_project}

    while True:
        print(
            "- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == "q":
            if input("Would you like to save to projects.txt? (yes/no): ").lower() == "yes":
                save_projects('projects.txt', projects)
            break
        elif choice in actions:
            action = actions[choice]
            if choice in ["l", "s"]:
                filename = input("Filename: ")
                action(filename, projects) if choice == "s" else action(filename)
            else:
                action(projects)

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
