# model.py
import math

def calculate_mean(marks):
    """Calculate the mean of the marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def calculate_median(marks):
    """Calculate the median of the marks."""
    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    if n % 2 == 0:
        return (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2
    else:
        return sorted_marks[n // 2]

def calculate_mode(marks):
    """Calculate the mode of the marks."""
    if not marks:
        return None
    marks_count = {}
    for mark in marks:
        marks_count[mark] = marks_count.get(mark, 0) + 1
    max_count = max(marks_count.values())
    mode = [key for key, value in marks_count.items() if value == max_count]
    return mode[0] if mode else None

def calculate_standard_deviation(marks):
    """Calculate the standard deviation of the marks."""
    if not marks:
        return 0
    mean = calculate_mean(marks)
    variance = sum((mark - mean) ** 2 for mark in marks) / len(marks)
    return math.sqrt(variance)

def calculate_skewness(marks):
    """Calculate the skewness of the marks."""
    mean = calculate_mean(marks)
    n = len(marks)
    numerator = sum((mark - mean) ** 3 for mark in marks)
    denominator = (n - 1) * (n - 2) * (calculate_standard_deviation(marks) ** 3)
    return numerator / denominator

# view.py
def print_menu():
    """Print the menu options."""
    print("\nMenu:")
    print("1. Enter numbers to the list")
    print("2. Print the mean of the numbers")
    print("3. Print the median of the numbers")
    print("4. Print the mode of the numbers")
    print("5. Go back and enter a NEW set of numbers")
    print("6. Print the skewness of the numbers")
    print("7. Exit the application")

# controller.py
from model import calculate_mean, calculate_median, calculate_mode, calculate_skewness
from view import print_menu

def enter_numbers(marks):
    """Allow the user to enter numbers to the list."""
    while True:
        # Prompt the user to enter a mark
        mark_input = input("Enter a student's mark (or type 'done' to finish): ")
        if mark_input.lower() == 'done':
            # If user types 'done', exit the loop
            break
        try:
            # Convert input to float
            mark = float(mark_input)
            if 0 <= mark <= 100:
                # If the mark is within the valid range, add it to the list of marks
                marks.append(mark)
                print("Number of marks entered:", len(marks))
            else:
                # If the mark is not within the valid range, display an error message
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            # If input cannot be converted to float, display an error message
            print("Please enter a valid numerical mark.")

def main():
    """Main function to orchestrate the interaction between the Model and the View."""
    # Initialize the list of marks
    marks = []
    while True:
        if len(marks) < 2:
            print("Please add at least two numbers before presenting the menu.")
            enter_numbers(marks)
            continue
        
        # Display the menu options
        print_menu()
        # Prompt the user to enter a choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # If user chooses option 1, allow them to enter marks
            enter_numbers(marks)
        elif choice == '2':
            # If user chooses option 2, calculate and print the mean of the marks
            print("Mean of the numbers:", calculate_mean(marks))
        elif choice == '3':
            # If user chooses option 3, calculate and print the median of the marks
            print("Median of the numbers:", calculate_median(marks))
        elif choice == '4':
            # If user chooses option 4, calculate and print the mode of the marks
            mode = calculate_mode(marks)
            if mode is not None:
                print("Mode of the numbers:", mode)
            else:
                print("No unique mode")
        elif choice == '5':
            # If user chooses option 5, clear the list of marks
            marks = []
            print("You have chosen to enter a NEW set of numbers.")
        elif choice == '6':
            # If user chooses option 6, calculate and print the skewness of the marks
            print("Skewness of the numbers:", calculate_skewness(marks))
        elif choice == '7':
            # If user chooses option 7, exit the application
            print("Exiting the application. Goodbye!")
            return
        else:
            # If user enters an invalid choice, display an error message
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    # Call the main function to start the application
    main()
