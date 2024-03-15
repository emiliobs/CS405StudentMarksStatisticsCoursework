# model.py
import math

def calculate_mean(marks):
    """Calculate the mean of the marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def calculate_standard_deviation(marks):
    """Calculate the standard deviation of the marks."""
    if not marks:
        return 0
    mean = calculate_mean(marks)
    variance = sum((mark - mean) ** 2 for mark in marks) / len(marks)
    return math.sqrt(variance)

def calculate_skewness(marks):
    """
    Calculate the skewness of a list of marks.

    Args:
    marks (list): A list of numerical marks.

    Returns:
    float: The skewness of the marks.
    """
    try:
        # Check for empty list or insufficient data points
        if len(marks) < 3:
            raise ValueError("Insufficient data points to calculate skewness")

        # Calculate the mean of the marks
        mean = calculate_mean(marks)  

        n = len(marks)  # Get the number of marks
        
        # Calculate the numerator of the skewness formula
        numerator = sum((mark - mean) ** 3 for mark in marks)
        
        # Calculate the denominator of the skewness formula
        denominator = (n - 1) * (n - 2) * (calculate_standard_deviation(marks) ** 3)
        
        # Check for division by zero
        if denominator == 0:
            raise ValueError("Cannot divide by zero")

        # Return the skewness value
        return numerator / denominator

    except ValueError as ve:
        print("Error:", ve)
        # Halt the program by re-raising the caught exception
        raise ve

def read_data_from_file(filename):
    """Read data from a file and populate the list of marks."""
    try:
        with open(filename, 'r') as file:
            data = file.read()
            marks = list(map(float, data.split(',')))
        return marks
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except ValueError:
        print("Error: File contains invalid numerical data.")
        return []


# controller.py
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
    print("8. Add more numbers to the list")
    print("9. Read data from a file")  # New menu choice

def enter_numbers(marks):
    """Allow the user to enter numbers to the list."""
    while True:
        mark_input = input("Enter student's marks separated by commas (or type 'done' to finish): ")
        if mark_input.lower() == 'done':
            break
        elif ',' in mark_input:
            try:
                marks.extend(map(float, mark_input.split(',')))
                print("Number of marks entered:", len(marks))
            except ValueError:
                print("Please enter valid numerical marks.")
        else:
            try:
                mark = float(mark_input)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    print("Number of marks entered:", len(marks))
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Please enter a valid numerical mark.")

def main():
    """Main function to orchestrate the interaction between the Model and the View."""
    marks = []
    while True:
        if len(marks) < 2:
            print("Please add at least two numbers before presenting the menu.")
            enter_numbers(marks)
            continue
        
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            enter_numbers(marks)
        elif choice == '2':
            print("Mean of the numbers:", calculate_mean(marks))
        elif choice == '3':
            pass  # Implement printing median
        elif choice == '4':
            pass  # Implement printing mode
        elif choice == '5':
            marks = []
            print("You have chosen to enter a NEW set of numbers.")
        elif choice == '6':
            pass  # Implement printing skewness
        elif choice == '7':
            print("Exiting the application. Goodbye!")
            return
        elif choice == '8':
            enter_numbers(marks)
        elif choice == '9':
            filename = input("Enter the filename to read data from: ")
            marks = read_data_from_file(filename)
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
