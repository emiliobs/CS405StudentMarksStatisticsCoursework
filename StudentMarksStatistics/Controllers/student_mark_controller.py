# Importing necessary functions from Models module
from Models.calculate_model import calculate_mean, enter_marks_to_list, calculate_median, calculate_mode, calculate_skewness
# Importing print_menu function from Views module
from Views.menu_view import print_menu  

# Main function that calls all statistical functions and the menu
def main():
    # Initialize an empty list to store marks
    marks = []  
    # Start an infinite loop for displaying the menu and handling user choices
    while True:  
        # Display the menu options
        print_menu()  
        # Prompt the user to enter their choice
        choice = input("Enter Your Choice: ")  
        # Print a blank line
        print("\n")
         # If user chooses option 1
        if choice == '1': 
            print("------------------- Entering Marks ----------------------")
            # Call enter_marks_to_list function to input marks
            enter_marks_to_list(marks)  
            print("---------------------------------------------------------")
            # Print a blank line
            print("\n")
            # If user chooses option 2
        elif choice == "2":  
            print("----------- Result The Means ---------")
             # Check if there are marks entered
            if marks: 
                # Print mean of the entered marks
                print("Mean Of The Numbers: ", calculate_mean(marks))  
            else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.")  
            print("--------------------------------------")
            # Print a blank line
            print("\n")
        elif choice == '3':
            print("----------- Result The Median ---------")
            # Check if there are marks entered
            if marks: 
                # Print mean of the entered marks 
                print("Median Of The Numbers: ", calculate_median(marks))  
                # Inform the user if no marks have been entered
            else:
                print("No marks entered yet.")  
            print("--------------------------------------")
            # Print a blank line
            print("\n")
        elif choice == '4':
            print("----------- Result The Mode ---------")
            # Check if there are marks entered
            if marks:  
                 # Print mean of the entered marks
                print("Mode Of The Numbers: ", calculate_mode(marks)) 
            else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.")  
            print("--------------------------------------")
            # Print a blank line
            print("\n")
        elif choice == '5':
            print("----------------- Reset The List --------------")
            # Initialize an empty list named 'marks'
            # This line creates a new list named 'marks' with no elements.
            # The square brackets [] denote an empty list in Python.
            # Later in the program, this list can be filled with numerical marks.
            marks = []        
            print("You Have Choosen To Enter a New Set Of Numbers.")
            print("-----------------------------------------------")
            # Print a blank line
            print("\n")
        elif choice == '6':
             print("----------- Result The Skewness ---------")
             # Check if there are marks entered
             if marks:  
                 # Print mean of the entered marks
                print("Skewness Of The Numbers: ", calculate_skewness(marks))  
             else:
                # Inform the user if no marks have been entered
                print("No marks entered yet.") 
                print("--------------------------------------")
                # Print a blank line
                # The "\n" is an escape sequence representing a newline character,
                # which moves the cursor to the next line when printed.
                # Therefore, this line prints an empty line in the console output.
                print("\n")               
        # If user chooses option 6
        elif choice == '7': 
            print("======================================")
            print("=                                    =") 
            print("=                                    =") 
            print("=                                    =") 
            print("=                                    =") 
            print("= Exiting The Application. Goodbye!  =") 
            print("=                                    =") 
            print("=                                    =") 
            print("=                                    =") 
            print("=                                    =") 
            print("======================================")
            print("\n")
            # Exit the function and the program
            return  
         # If user inputs an invalid choice
        else: 
            # Print error message
            print("Invalid Choice. Please Enter A Number From 1 To 6.")  
            

