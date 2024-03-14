def calculate_mean(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    if n % 2 == 0:
        return (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2
    else:
        return sorted_marks[n // 2]

def calculate_mode(marks):
    if not marks:
        return None
    marks_count = {}
    for mark in marks:
        marks_count[mark] = marks_count.get(mark, 0) + 1
    max_count = max(marks_count.values())
    mode = [key for key, value in marks_count.items() if value == max_count]
    return mode[0] if mode else None

def print_menu():
    print("\nMenu:")
    print("1. Enter Marks to the list")
    print("2. Print the mean of the numbers")
    print("3. Print the median of the numbers")
    print("4. Print the mode of the numbers")
    print("5. Go back and enter a NEW set of numbers")
    print("6. Exit the application")

def main():
    marks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                mark_input = input("Enter a student's mark (or type 'done' to finish): ")
                if mark_input.lower() == 'done':
                    break
                try:
                    mark = float(mark_input)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        print("Number of marks entered:", len(marks))
                    else:
                        print("Please enter a valid mark between 0 and 100.")
                except ValueError:
                    print("Please enter a valid numerical mark.")
        elif choice == '2':
            print("Mean of the numbers:", calculate_mean(marks))
        elif choice == '3':
            print("Median of the numbers:", calculate_median(marks))
        elif choice == '4':
            mode = calculate_mode(marks)
            if mode is not None:
                print("Mode of the numbers:", mode)
            else:
                print("No unique mode")
        elif choice == '5':
            marks = []
            print("You have chosen to enter a NEW set of numbers.")
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            return
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
