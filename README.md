# To-Do-List-Source-Code-
This Python script creates a simple To-Do List application using the Tkinter library. The application interface consists of five tasks, each with a corresponding checkbox and text entry field. The tasks can be marked as complete using the checkboxes and saved using a "Save" button. The script captures the text from the entry fields and prints it in the console when the "Save" button is pressed.

Key Components

Checkbuttons: Allow users to mark tasks as complete.
Entry Widgets: Provide input fields for users to type their tasks.
Button: Triggers the get_text function to save and print the entered tasks.
Layout

The layout is managed using the grid method, with each task and its checkbox arranged in a row.
The window has a title "To Do List" and is set to a size of 500x500 pixels.
Functionality

The get_text function retrieves the text from each entry widget and stores it in a dictionary called entry_data.
When the "Save" button is clicked, the get_text function is executed, and the task data is printed in the console.
How to Run

Ensure you have Python installed on your system.
Save the script as to_do.py.
Run the script using the command:
python to_do.py
A window will appear with five entry fields and corresponding checkboxes.
Enter your tasks in the fields and click "Save" to print the tasks to the console.
This project provides a basic yet functional example of how to create a GUI application with Tkinter.
