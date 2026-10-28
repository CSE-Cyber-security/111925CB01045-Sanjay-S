Simple Calculator 🧮
Description

This is a simple calculator program written in Python. It allows users to perform basic arithmetic operations through a menu-driven interface.

Features
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Division-by-zero error handling
Invalid input handling
Continuous calculations until the user chooses to exit
Requirements
Python 3.x
No external libraries required
How to Run
Install Python 3 if it is not already installed.
Save the program in a file named calculator.py.
Open a terminal or command prompt in the folder containing the file.
Run the following command:
bash
python calculator.py


On some systems, you may need to use:

bash
python3 calculator.py

Usage

When you run the program, the following menu appears:

text
===== Simple Calculator =====
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit


Choose an operation by entering a number from 1 to 5.

Example
text
Choose an option (1-5): 1
Enter the first number: 10
Enter the second number: 5
Result: 10 + 5 = 15

Exit the Program

Enter 5 when prompted to choose an option. The program will display Goodbye! and terminate.

Error Handling
Displays an error message if the user enters an invalid menu option.
Rejects non-numeric input.
Prevents division by zero.
Project Structure
text
SimpleCalculator/
├── calculator.py
└── README.md

License

This project is free to use, modify, and distribute for educational and personal purposes.