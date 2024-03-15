# Importing necessary functions from Models module
from Models.calculate_model import calculate_mean, enter_marks_to_list, calculate_median, calculate_mode, calculate_skewness
# Importing print_menu function from Views module
from Views.menu_view import print_menu, autor_welcome, goodbye_user

"""Main function to orchestrate the interaction between the Model and the View."""
def main():
    
    # Display welcome from Author message and information about the program
    autor_welcome()
    
    # Initialize an empty list to store marks
    marks = []  
    # Start an infinite loop for displaying the menu and handling user choices
    while True:  
        # Check if the length of the 'marks' list is less than 2
        # If there are less than 2 numbers in the list, prompt the user to add at least two numbers before presenting the menu
        if len(marks) < 2:
        # Print a blank line
          print("\n")
          print("--------------------------- Enter Marks ----------------------------")
         # This line prints the message to the console, informing the user to add more numbers.
          print("Please Add At Least Two Or More Numbers Before Presenting The Menu.")
          enter_marks_to_list(marks)
        # The 'continue' statement is used to skip the rest of the loop's code block and move to the next iteration.
        # In this context, it ensures that the program does not proceed to present the menu if there are not enough numbers in the list.
        # Instead, it goes back to the beginning of the loop to allow the user to add more numbers.
          print("--------------------------------------------------------------------")
          continue    
          
        # Display the menu options
        print_menu()  
        # Prompt the user to enter their choice
        choice = input("Enter Your Choice: ")  
        # Print a blank line
        print("\n")
        # If user chooses option 1, allow them to enter marks
        if choice == '1': 
            print("------------------- Entering Marks ----------------------")
            # Call enter_marks_to_list function to input marks
            enter_marks_to_list(marks)  
            print("---------------------------------------------------------")
            # Print a blank line
            print("\n")
            # If user chooses option 2
        elif choice == "2":  
            print("--------------- Result The Means -------------")
             # Check if there are marks entered
            if marks: 
                # Print mean of the entered marks
                print("Mean Of The Numbers: ", calculate_mean(marks))  
            else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.")  
            print("----------------------------------------------")
            # Print a blank line
            print("\n")
            # If user chooses option 3
        elif choice == '3':
            print("-------------- Result The Median--------------")
            # Check if there are marks entered
            if marks: 
                # Print mean of the entered marks 
                print("Median Of The Numbers: ", calculate_median(marks))  
                # Inform the user if no marks have been entered
            else:
                print("No marks entered yet.")  
            print("----------------------------------------------")
            # Print a blank line
            print("\n")
            # If user chooses option 4
        elif choice == '4':
            print("---------------- Result The Mode -------------")
            # Check if there are marks entered
            if marks:  
                 # Print mean of the entered marks
                print("Mode Of The Numbers: ", calculate_mode(marks)) 
            else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.")  
            print("----------------------------------------------")
            # Print a blank line
            print("\n")
            # If user chooses option 5
        elif choice == '5':
             print("------------- Result The Skewness ------------")
             # Check if there are marks entered
             if marks:  
                 # Print mean of the entered marks
                print("Skewness Of The Numbers: ", calculate_skewness(marks))  
             else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.") 
             print("----------------------------------------------")
                # Print a blank line
                # The "\n" is an escape sequence representing a newline character,
                # which moves the cursor to the next line when printed.
                # Therefore, this line prints an empty line in the console output.
             print("\n")   
             # If user chooses option 6            
        elif choice == '6':
            print("---------------- Reset The List --------------")
            # Initialize an empty list named 'marks'
            # This line creates a new list named 'marks' with no elements.
            # The square brackets [] denote an empty list in Python.
            # Later in the program, this list can be filled with numerical marks.
            marks = []        
            print("You Have Choosen To Enter a New Set Of Numbers.")
            print("----------------------------------------------")
            # Print a blank line
            print("\n")            
        # If user chooses option 7
        elif choice == '7': 
           # Exit the function and the program
           goodbye_user()
           print("\n")            
           return  
         # If user inputs an invalid choice
        else: 
            # Print error message
            print("Invalid Choice. Please Enter A Number From 1 To 6.")  
            

