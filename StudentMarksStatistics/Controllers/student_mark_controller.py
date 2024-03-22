# Importing necessary functions from Models module
from Models.calculate_model import *

# Importing print_menu function from Views module
from Views.menu_view import print_menu, autor_welcome, goodbye_user

"""Main function to orchestrate the interaction between the Model and the View."""
def main():   
     
    # Display welcome message and information about the program
    autor_welcome()  
      
    # Initialize an empty list to store marks
    marks = []  
    
    # Start an infinite loop for displaying the menu and handling user choices
    while True:  
        
        # Check if the length of the 'marks' list is less than 2
        # If there are less than 2 numbers in the list, prompt the user to add at least two numbers
        # before presenting the menu
        if len(marks) < 2:
            # Prompt the user to add at least two numbers before presenting the menu
            print("\n")
            print("--------------------------- Enter Marks ----------------------------")
           # This line prints the message to the console, informing the user to add more numbers.
            print("Please Add At Least Two Or More Numbers Before Presenting The Menu.")
            enter_marks_to_list(marks)
            print("--------------------------------------------------------------------")
            continue              
        
        # Display the menu options
        print_menu()  
      
        # Prompt the user to enter their choice
        choice = input("Enter Your Choice: ")  
        print("\n")        
       
        # Dictionary to map user choices to corresponding functions
        switch = {
            '1': add_marks,
            '2': show_marks,
            '3': show_mean,
            '4': show_median,
            '5': show_mode,
            '6': show_skewness,
            '7': add_marks_by_comma,
            '8': enter_new_set,
            '9': read_from_file,
            '10': exit_program,
        }        
      
       # Execute the chosen function based on the user's input
        if choice in switch:
         # If the user's choice is a valid option in the menu, the corresponding function is called 
         # with 'marks' list as argument
         switch[choice](marks)
        else:
        # If the user's choice is not valid, an error message is displayed
         print("Invalid Choice. Please Enter A Number From 1 To 10.")    

# Function to add marks to the list
def add_marks(marks):
    # Print a message indicating that marks are being added
    print("------------------- Adding Marks ----------------------")    
    # Call the function to allow the user to input marks and add them to the list
    enter_marks_to_list(marks)    
    # Print a separator line for better readability
    print("---------------------------------------------------------")    
    # Print a newline character for better formatting
    print("\n")

# Function to display the entered marks
def show_marks(marks):
    # Print a message indicating that the marks are being shown
    print("----------------- Show Marks -----------------")
    
    # Check if there are any marks in the list
    if marks:
        # If marks are present, call the function to display all marks
        Show_All_Marks(marks)  
    else:
        # If no marks are present, print a message indicating so
        print("No marks entered yet.")
    
    # Print a separator line for better readability
    print("----------------------------------------------")
    
    # Print a newline character for better formatting
    print("\n")


 # Function to calculate and display the mean of the marks

# Function to calculate and display the mean of the marks
def show_mean(marks):
    # Print a message indicating that the mean is being calculated
    print("--------------- Result The Means -------------")
    
    # Check if there are any marks in the list
    if marks: 
        # If marks are present, calculate and print the mean
        print("Mean Of The Numbers: ", calculate_mean(marks))  
    else:
        # If no marks are present, print a message indicating so
        print("No marks entered yet.")
    
    # Print a separator line for better readability
    print("----------------------------------------------")
    
    # Print a newline character for better formatting
    print("\n")

    
 # Function to calculate and display the median of the marks

# Function to calculate and display the median of the marks
def show_median(marks):
    # Print a message indicating that the median is being calculated
    print("-------------- Result The Median--------------")
    
    # Check if there are any marks in the list
    if marks: 
        # If marks are present, calculate and print the median
        print("Median Of The Numbers: ", calculate_median(marks))  
    else:
        # If no marks are present, print a message indicating so
        print("No marks entered yet.")
    
    # Print a separator line for better readability
    print("----------------------------------------------")
    
    # Print a newline character for better formatting
    print("\n")

# Function to calculate and display the mode of the marks
def show_mode(marks):
    # Print a message indicating that the mode is being calculated
    print("---------------- Result The Mode -------------")
    
    # Check if there are any marks in the list
    if marks:  
        # If marks are present, calculate and print the mode
        print("Mode Of The Numbers: ", calculate_mode(marks)) 
    else:
        # If no marks are present, print a message indicating so
        print("No marks entered yet.")
    
    # Print a separator line for better readability
    print("----------------------------------------------")
    
    # Print a newline character for better formatting
    print("\n")

# Function to calculate and display the skewness of the marks
def show_skewness(marks):
    try:
        # Print a message indicating that the skewness is being calculated
        print("------------- Result The Skewness ------------")  
        
        # Calculate and print the skewness of the marks
        print("Skewness Of The Numbers: ", calculate_skewness(marks))
        
        # Print a separator line for better readability
        print("----------------------------------------------")
    except ValueError as ve:
        # If there's a ValueError (likely due to insufficient data), print the error message
        print(ve)
        # Prompt the user to enter more marks
        enter_marks_to_list(marks)

# Function to add marks to the list using comma-separated input
def add_marks_by_comma(marks):
    try:
        # Print a message indicating that marks are being added using comma-separated input
        print("---------- Adding Marks In by Comma ----------")
        
        # Call the function to allow the user to input marks using comma-separated input and add them to the list
        enter_marks_to_list_by_comma(marks)
        
        # Print a separator line for better readability
        print("----------------------------------------------")
    except ValueError as ve:
        # If there's a ValueError (likely due to incorrect input format), print the error message
        print(ve)
        # Print another separator line for better readability
        print("----------------------------------------------")
        # Print a newline character for better formatting
        print("\n")

# Function to clear the list and enter a new set of marks
def enter_new_set(marks):
    # Print a message indicating that a new set of marks is being entered
    print("--- Enter a New Set Of Numbers In the List ---")
    
    # Clear the existing marks list
    marks.clear()
    
    # Print a message indicating that the marks list is now empty
    print("You Have Chosen To Enter a New Set Of Numbers (Empty List).")
    
    # Print a separator line for better readability
    print("----------------------------------------------")
    
    # Print a newline character for better formatting
    print("\n")
    
    # Return the empty marks list
    return marks

# Function to read marks from a file and add them to the list
def read_from_file(marks):
    try:
        # Print a message indicating that data is being read from a file
        print("---------= Reading Data From A File ----------")
        
        # Prompt the user to enter the filename from which data will be read
        filename = input("Enter The Filename To Read Data From: ")
        
        # Read data from the file and add it to the marks list
        marks += read_data_from_file(filename)
        
        # Print a newline character for better formatting
        print("")
        
        # Show all the marks in the list
        Show_All_Marks(marks)
        
        # Print a separator line for better readability
        print("----------------------------------------------")
        
        # Print a newline character for better formatting
        print("\n")
        
        # Return the updated marks list
        return marks
    except ValueError as ve:
        # If there's a ValueError (likely due to incorrect input), print the error message
        print(ve)
        # Print a separator line for better readability
        print("----------------------------------------------")

# Function to exit the program
def exit_program(marks):
    # Clear the marks list
    marks = []
    
    # Call the function to display a goodbye message to the user
    goodbye_user()
    
    # Print a newline character for better formatting
    print("\n")

    
