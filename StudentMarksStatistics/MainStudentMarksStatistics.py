# Importing main function from Controllers module
from Controllers.student_mark_controller import main

"""
This line calls the main function that was imported.
The print() function is used to display the return value 
of the main function, if any.
By calling main(), the script executes the main logic 
of the student marks statistics application defined in the main function.
"""
# Call the main function when the script is executed
print(main())  