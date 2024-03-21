
# Importing the math module to use math.sqrt function for square root calculation
import math  

"""
 Primary statistical functions implemented within the program.
"""

# Function enter marks to the list
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
        # Prompt the user to enter a mark
        mark_input = input("Enter a Student's Mark (or Type 'done' to Finish.): ") 
        # Check if user wants to finish entering marks
        if mark_input.lower() == "done":  
            # Exit the loop if user inputs 'done'
            break  
        try:
            mark = float(mark_input)  # Convert input to float
            if mark > -1:  # Check if mark is valid (assuming negative marks are not allowed)
                marks.append(mark)  # Append mark to the list
                print("Number Of Marks Entered: ", len(marks))  # Print number of marks entered
            else:
                # Print error message for invalid mark
                print("ERROR. Please Enter a Valid Mark (E.g., 5, 13.5).") 
        except ValueError:
            # Print error message for non-numerical input            
            print("Error. Please Enter a Valid Numerical Mark.")  
            
# Function enter marks to list by commas
def enter_marks_to_list_by_comma(marks):
    """
    This function allows the user to input marks until they choose to stop.
    It validates each input to ensure it is a valid numerical mark.

    Args:
    marks (list): A list to which the entered marks will be appended.

    Returns:
    None
    """    
    while True:  # Start an infinite loop
        # Prompt the user to enter a mark
        mark_input = input("Enter a Student's Mark by Commas (or Type 'done' to Finish): ") 
        # Check if user wants to finish entering marks
        if mark_input.lower() == "done":  
            # Exit the loop if user inputs 'done'
            break  
        elif ',' in mark_input:            
            try:
                # Split the input by commas, convert each substring to float, and add to the marks list
                marks.extend(map(float, mark_input.split(',')))
                # Print the number of marks entered
                print("Number of Marks Entered:", len(marks))  
            except ValueError:
                # Print error message for non-numerical input            
                print("ERROR. Please Enter a Valid Numerical Mark.")  
              
# Define a function named ShowAllMarks that takes a list named marks as input
def Show_All_Marks(marks):
    # Define a function named ShowAllMarks that takes a list named marks as input
    print("Number Of Marks Entered: ", len(marks) ,"\t")
    for mark in marks:
        # Iterate over each element in the marks list        
        print(" ", mark)
        # Convert each element in the marks list to a string using map() and str() functions
        # Then join all the elements together with a space in between using join()
        # Finally, print the result

# Function Calculate the mean of the marks
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

# Function Calculate the median of the marks
def calculate_median(marks):
    """
    Calculate the median of a list of marks.

    Args:
    marks (list): A list of numerical marks.

    Returns:
    float: The median of the marks.
    """
       
    if not marks:  # Check if marks list is empty
        return 0  # Return 0 if list is empty
    
    # Sort the list of marks in ascending order
    sorted_marks = sorted(marks)
    # Get the number of marks in the list
    n = len(sorted_marks)
    
    # Check if the number of marks is even
    if n % 2 == 0:
        # Calculate the median for even-length lists
        # by taking the average of the two middle values
        return (sorted_marks[n // 2 - 1] + sorted_marks[n // 2]) / 2
    else:
        # Calculate the median for odd-length lists
        # by returning the middle value
        return sorted_marks[n // 2]
    
# Function Calculate the mode of the marks
def calculate_mode(marks):
    # Check if the marks list is empty
    if not marks:
        return None  # Return None if the list is empty, as there is no mode
    
    # Create an empty dictionary to store the count of each mark
    marks_count = {}
    
    # Count the occurrences of each mark in the list
    for mark in marks:
        # Increase the count of the current mark by 1
        # Using marks_count.get() to retrieve the count of the current mark, or 0 if not present
        marks_count[mark] = marks_count.get(mark, 0) + 1
    
    # Find the maximum count of occurrences
    max_count = max(marks_count.values())
    
    # Find all marks that have the maximum count (the mode(s))
    mode = [key for key, value in marks_count.items() if value == max_count]
    
    # Return the first mode if it exists, otherwise return None
    return mode[0] if mode else None

# Function Calculate the standard deviation of the marks
def calculate_standard_deviation(marks):
    """
    Calculate the standard deviation of a list of marks.

    Args:
    marks (list): A list of numerical marks.

    Returns:
    float: The standard deviation of the marks.
    """
    
    if not marks:  # Check if the marks list is empty
        return 0  # If the marks list is empty, return 0 as there are no marks to compute the standard deviation
    
    mean = calculate_mean(marks)  # Calculate the mean of the marks using a separate function calculate_mean
    # Above line uses a separate function named calculate_mean to compute the mean of the marks.
    # It's done this way to break down the computation into smaller, more manageable functions.
    
    # Calculate the variance of the marks
    # Variance is the average of the squared differences from the mean
    variance = sum((mark - mean) ** 2 for mark in marks) / len(marks)
    # The above line uses a generator expression to iterate over each mark in the marks list.
    # For each mark, it calculates the squared difference from the mean and sums them up.
    # Then it divides the sum by the total number of marks to get the average squared difference.
    
    # Return the square root of the variance as the standard deviation
    # Standard deviation is the square root of variance
    return math.sqrt(variance)
    # The square root of the variance is returned as the standard deviation.
    # This is because the standard deviation is the measure of how spread out the values in a dataset are.
    # By returning the square root of the variance, we're providing a measure of the spread that is in the same units as the original data.

# Function Calculate the skewness of the marks
def calculate_skewness(marks):
    """
    Calculate the skewness of a list of marks.

    Args:
    marks (list): A list of numerical marks.

    Returns:
    float: The skewness of the marks.
    """
    
    # Check for empty list or insufficient data points
    if len(marks) < 3:
        raise ValueError("Sorry!. Insufficient Data Points To Calculate Skewness(At Leat 3 Marks.")
    #Inssufficient Data Points To Calculate Skewness.
       
    # Calculate the mean of the marks
    # Above line uses a separate function named calculate_mean to compute the mean of the marks.
    # It's done this way to break down the computation into smaller, more manageable functions.
    mean = calculate_mean(marks)  
    
    n = len(marks)  # Get the number of marks
    
    # Calculate the numerator of the skewness formula
    numerator = sum((mark - mean) ** 3 for mark in marks)
    # The above line uses a generator expression to iterate over each mark in the marks list.
    # For each mark, it calculates the cubed difference from the mean and sums them up.
    
    # Calculate the denominator of the skewness formula
    denominator = (n - 1) * (n - 2) * (calculate_standard_deviation(marks) ** 3)
    # The denominator of the skewness formula involves the cube of the standard deviation,
    # which is calculated using the calculate_standard_deviation function.
    # The formula also depends on the number of elements in the list.
    
    # Check for division by zero
    if denominator == 0:
        raise ValueError("ERROR: Must Have At  leat One Mark is greater Than Zero In the List.")
       
    
    # Return the skewness value
    return numerator / denominator
    # The skewness value is calculated by dividing the numerator by the denominator,
    # following the skewness formula.

# Read data from a file and populate the list of marks.
def read_data_from_file(filename):
    """
    Read data from a file and populate the list of marks.

    Args:
    filename (str): The name of the file to read data from.

    Returns:
    list: A list containing the numerical marks read from the file.
    """
    try:
        # Attempt to open the file for reading
        with open(filename, "r") as file:
            # Read the contents of the file
            data = file.read()
            if data != '':
                print("Great!. The File Was Read Successfully.")
                # Split the data by commas and convert each element to a float, then store in a list
                marks = list(map(float, data.split(',')))
                # Return the list of marks
                return marks
            else:
                print("Sorry!. The File Has No Data.")
                return ""
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{filename}' Not Found Or Please Provide The File Name As An Argument.")
        # Return an empty list
        return []
    except ValueError:
        # Handle the case where the file contains invalid numerical data
        print("Error: File contains invalid numerical data.")
        # Return an empty list
        return []

