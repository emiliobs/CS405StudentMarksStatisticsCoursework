# Importing necessary functions from Models module
from Models.calculate_model import calculate_mean, enter_marks_to_list, calculate_median 
# Importing print_menu function from Views module
from Views.menu_view import print_menu  

def main():
    marks = []  # Initialize an empty list to store marks
    while True:  # Start an infinite loop for displaying the menu and handling user choices
        print_menu()  # Display the menu options
        choice = input("Enter Your Choice: ")  # Prompt the user to enter their choice
        print("\n")
        if choice == '1':  # If user chooses option 1
            print("------------------- Entering Marks ----------------------")
            enter_marks_to_list(marks)  # Call enter_marks_to_list function to input marks
            print("---------------------------------------------------------")
            print("\n")
        elif choice == "2":  # If user chooses option 2
            print("----------- Result The Means ---------")
            if marks:  # Check if there are marks entered
                print("Mean Of The Numbers: ", calculate_mean(marks))  # Print mean of the entered marks
            else:
                print("No marks entered yet.")  # Inform the user if no marks have been entered
            print("--------------------------------------")
            print("\n")
        elif choice == '3':
            print("----------- Result The Median ---------")
            if marks:  # Check if there are marks entered
                print("Median Of The Numbers: ", calculate_median(marks))  # Print mean of the entered marks
            else:
                print("No marks entered yet.")  # Inform the user if no marks have been entered
            print("--------------------------------------")
            print("\n")
        elif choice == '6':  # If user chooses option 6
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
            return  # Exit the function and the program
        else:  # If user inputs an invalid choice
            print("Invalid Choice. Please Enter A Number From 1 To 6.")  # Print error message
            

