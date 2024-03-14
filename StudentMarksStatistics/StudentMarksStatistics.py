marks = []

def enter_marks_to_list():
   while True: 
    mark_input = input("Enter a Student's Mark (or Type 'done' to Finish.): ")
    if mark_input.lower() == "done":
        break
    try:
        mark = float(mark_input)
        if mark > -1:
            marks.append(mark)
            print("Number Of Marks Entered: ", len(marks))
        else:
            print("Please Enter a Valid Mark (E.j 5, 13.5.5).")
    except ValueError:
        print("Please Enter a Valid Mark Numerical Mark.")        
        
def calculate_mean(mark):
    if not marks:
        return 0
    return sum(marks) / len(marks)        

def print_menu():
    print("\n============== MENU ==============")
    print("1. ENTER MARKS TO THE LIST.      =")
    print("2. PRINT THE MEAN OF THE NUMBERS.=")
    print("6. EXIT THE APPLICATION.         =")
    print("==================================")
    
def main():
    while True:
        print_menu()
        choice = input("Enter Yout Choice: ")   
        print("\n")
        
        if choice == '1':
             print("----------- Entering Marks ------------")
             enter_marks_to_list()
             print("---------------------------------------")
             print("\n")
        elif choice == "2":
             print("----------- Showinf The Means ------------")
             print("MEans Of The Numbers: ", calculate_mean(marks))
             print("---------------------------------------")
             print("\n")
        elif choice == '6':
            print("----------------------------------")
            print("Exiting The Application. Goodbye!") 
            print("----------------------------------")
            print("\n")
            return
        else:
            print("Invalid Choice. Please Enter A Number From 1 To 6.")
            
            
main()