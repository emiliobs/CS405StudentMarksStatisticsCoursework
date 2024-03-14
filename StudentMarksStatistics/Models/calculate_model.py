def enter_marks_to_list(marks):
    """
    This function allows the user to input marks until they choose to stop.
    It validates each input to ensure it is a valid numerical mark.

    Args:
    marks (list): A list to which the entered marks will be appended.

    Returns:
    None
    """
    while True:  # Start an infinite loop
        mark_input = input("Enter a Student's Mark (or Type 'done' to Finish.): ")  # Prompt user for input
        if mark_input.lower() == "done":  # Check if user wants to finish entering marks
            break  # Exit the loop if user inputs 'done'
        try:
            mark = float(mark_input)  # Convert input to float
            if mark > -1:  # Check if mark is valid (assuming negative marks are not allowed)
                marks.append(mark)  # Append mark to the list
                print("Number Of Marks Entered: ", len(marks))  # Print number of marks entered
            else:
                print("Please Enter a Valid Mark (E.g., 5, 13.5).")  # Print error message for invalid mark
        except ValueError:
            print("Please Enter a Valid Numerical Mark.")  # Print error message for non-numerical input

def calculate_mean(marks):
    """
    This function calculates the mean of the entered marks.

    Args:
    marks (list): A list of numerical marks.

    Returns:
    float: The mean of the marks. If the list is empty, returns 0.
    """
    if not marks:  # Check if marks list is empty
        return 0  # Return 0 if list is empty
    return sum(marks) / len(marks)  # Calculate mean of marks and return it

