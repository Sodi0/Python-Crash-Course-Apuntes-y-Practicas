import math
# Task 1
def number_max(num1, num2):
    """Returns the maximum of two numbers.
    Parameters:
    num1 (int, float): The first number.
    num2 (int, float): The second number.

    Returns:
    int, float: The maximum of the two numbers.

    Example:
    >>> number_max(10, 20)
    20
    """
    if num1 > num2:
        return num1
    else:
        return num2

print("Task 1:")
print(number_max(10, 20))  # Output: 20

# Task 2
def calculate_area(figure):
    if figure == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")
    elif figure == "2":
        radius = float(input("Enter the radius of the circle: "))
        area = area_circle(radius)
        print(f"The area of the circle is: {area}")
    elif figure == "3":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_triangle(base, height)
        print(f"The area of the triangle is: {area}")
    else:
        print("Invalid option. Please select 1, 2, or 3.")

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius ** 2

def area_triangle(base, height):
    return 0.5 * base * height

print("\nTask 2:")
figure_choice = input("Select a figure to calculate area (1: Rectangle, 2: Circle, 3: Triangle): ")
while figure_choice not in ["1", "2", "3"]:
    figure_choice = input("Invalid option. Please select 1, 2, or 3: ")
calculate_area(figure_choice)


# Task 3
def calculate_number_characters(string):
    characters = {}
    for char in string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

print("\nTask 3:")
user_string = input("Enter a string: ")
num_characters = calculate_number_characters(user_string)
print(f"The number of characters in the string is: {num_characters}")