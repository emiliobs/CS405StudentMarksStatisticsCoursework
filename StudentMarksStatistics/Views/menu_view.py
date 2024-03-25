
# Display a welcome message and information about the program
def autor_welcome():
    # Print a blank line for spacing
    print("")

    # Print a decorative line of equal signs
    print("\n" + "=" * 48)

    # Print the welcome message and program details
    print("=                    WELCOME                   =")
    print("=                                              =")
    print("=                      TO                      =")
    print("=                                              =")
    print("=           SPRING COURSEWORK PYTHON           =")
    print("=                                              =")
    print("=                                              =")
    print("=     STUDENTS MARKS STATISTICS APPLICATION    =")
    print("=                                              =")
    print("=                      BY                      =")
    print("=                                              =")
    print("=           EMILIO BARRERA SEPULVEDA           =")
    print("=                   22047090                   =")
    print("=                                              =")
    print("=                                              =")
    print("=        LONDON METROPOLITAN UNIVERSITY        =")
    print("=                 BSC COMPUTING                =")
    print("=        CS4051 FUNDAMENTALS OF COMPUTING      =")
    print("=                     LONDON                   =")
    print("=                   2023 - 2024                =")

    # Print another decorative line of equal signs
    print("=" * 48)
    

# This function prints the menu options for the application.
def print_menu():
    """
    Prints the menu options for the application.

    Returns:
        None
    """
    print("\n================= MENU ========================")  # Print menu header
    print("=                                             =")  # Print menu head
    print("=                                             =")  # Print menu head
    print("= 1.  ADD MARKS TO THE LIST.                  =")  # Print option 1
    print("= 2.  SHOW ALL MARKS IN THE LIST.             =")  # Print option 2
    print("= 3.  PRINT THE MEAN OF THE NUMBERS.          =")  # Print option 3
    print("= 4.  PRINT THE MEDIAN OF THE NUMBERS.        =")  # Print option 4
    print("= 5.  PRINT THE MODE OF THE NUMBERS.          =")  # Print option 5
    print("= 6.  PRINT THE SKEWNESS OF THE NUMBERS.      =")  # Print option 6
    print("= 7.  ADD MORE NUMBERS TO THE LIST BY COMMAS. =")  # Print option 7
    print("= 8.  GO BACK AND ENTER A NEW SET OF NUMBERS. =")  # Print option 8
    print("= 9.  READ DATA FROM A FILE.                  =")  # Print option 9
    print("= 10. EXIT THE APPLICATION.                   =")  # Print option 10
    print("=                                             =")  # Print menu footer
    print("=                                             =")  # Print menu footer
    print("===============================================")  # Print menu footer



# Exit the function and the program
def goodbye_user():    
     # Print a decorative line
    print("==============================================")
    print("=                                            =")
    print("=                                            =")
    print("=                THANK YOU!                  =")
    print("=                                            =")
    print("=          EXITING THE APPLICATION.          =")
    print("=                                            =")
    print("=                  GOODBYE!                  =")
    print("=                                            =")
    print("=                     :)                     =")
    print("=                                            =")
    print("=                                            =")
    print("==============================================")
    # Print a newline character for better formatting
    print("\n")
    # Exit the program
    exit()
    
    """
    Prints a farewell message and exits the application.

    Returns:
        None
    """