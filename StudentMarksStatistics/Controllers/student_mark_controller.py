# Importing necessary functions from Models module
from Models.calculate_model import *
#calculate_mean, enter_marks_to_list, calculate_median, calculate_mode, calculate_skewness, 
# ShowAllMarks,enter_marks_to_list_by_comma
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
        # If there are less than 2 numbers in the list, prompt the user to add at least two numbers 
        # before presenting the menu
        if len(marks) < 2:
        # Print a blank line
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
        # Print a blank line
        print("\n")
        # If user chooses option 1, allow them to enter marks
        
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
        
        if choice in switch:
            switch[choice](marks)
        else:
            print("Invalid Choice. Please Enter A Number From 1 To 10.")

def add_marks(marks):
    print("------------------- Adding Marks ----------------------")
    enter_marks_to_list(marks)
    print("---------------------------------------------------------")
    print("\n")

def show_marks(marks):
    print("----------------- Show Marks -----------------")
    if marks:
        Show_All_Marks(marks)  
    else:
        print("No marks entered yet.")  
    print("----------------------------------------------")
    print("\n")

def show_mean(marks):
    print("--------------- Result The Means -------------")
    if marks: 
        print("Mean Of The Numbers: ", calculate_mean(marks))  
    else:
        print("No marks entered yet.")  
    print("----------------------------------------------")
    print("\n")

def show_median(marks):
    print("-------------- Result The Median--------------")
    if marks: 
        print("Median Of The Numbers: ", calculate_median(marks))  
    else:
        print("No marks entered yet.")  
    print("----------------------------------------------")
    print("\n")

def show_mode(marks):
    print("---------------- Result The Mode -------------")
    if marks:  
        print("Mode Of The Numbers: ", calculate_mode(marks)) 
    else:
        print("No marks entered yet.")  
    print("----------------------------------------------")
    print("\n")

def show_skewness(marks):
    try:
        print("------------- Result The Skewness ------------")  
        print("Skewness Of The Numbers: ", calculate_skewness(marks))
        print("----------------------------------------------")
    except ValueError as ve:
        print(ve)
        enter_marks_to_list(marks)                  

def add_marks_by_comma(marks):
    try:                
        print("---------- Adding Marks In by Comma ----------")
        enter_marks_to_list_by_comma(marks)
        print("----------------------------------------------")
    except ValueError as ve:
        print(ve)
        print("----------------------------------------------")
        print("\n")

def enter_new_set(marks):
    print("--- Enter a New Set Of Numbers In The List ---")
    # Initialize an empty list named 'marks'
    # This line creates a new list named 'marks' with no elements.
    # The square brackets [] denote an empty list in Python.
    # Later in the program, this list can be filled with numerical marks.
    marks.clear()    
    print("You Have Choosen To Enter a New Set Of Numbers(Empty List).")    
    print("----------------------------------------------")
    # Print a blank line
    print("\n")      
    return marks
def read_from_file(marks):
    try:                
        print("---------= Reading Data From A File ----------")
        filename = input("Enter The Filename To Read Data From: ")       
        marks += read_data_from_file(filename)        
        print("")
        Show_All_Marks(marks)
        print("----------------------------------------------")
        print("\n") 
        return marks       
    except ValueError as ve:
        print(ve)
        print("----------------------------------------------")

def exit_program(marks):
    marks=[]
    goodbye_user()
    print("\n")
    
      
        
        
            

