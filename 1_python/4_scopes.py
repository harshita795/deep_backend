# Python Scope
# Concepts practiced:
# - Local scope
# - Global scope
# - Function parameters and scope
# - Local vs global variables


# Local scope
def calculate_salary():
    salary = 50000
    print(salary)


calculate_salary()


# Global scope
developer_name = "Harshita"


def introduce_developer():
    print(developer_name)


introduce_developer()


# Function parameters have local scope
def calculate_experience(years):
    print(f"Experience: {years} year")


calculate_experience(1)


# Local and global variables with the same name
language = "Python"


def show_language():
    language = "JavaScript"
    print(language)


show_language()
print(language)