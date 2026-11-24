# Todo List Manager

## 1. Project Overview

The Todo List Manager is a command-line interface (CLI) application developed using Python. It helps users organize and manage their daily tasks through a simple menu-driven interface.

Users can add tasks, view existing tasks, mark tasks as completed and remove tasks. The application uses JSON file handling to store task information so that tasks remain available even after the program is closed.

## 2. Objectives

- Develop a functional command-line task management application.
- Apply core Python programming concepts.
- Implement modular programming using functions.
- Understand file handling and JSON data storage.
- Handle invalid inputs and unexpected errors.
- Write clean, readable and maintainable code.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Data Storage:** JSON
- **Concepts:** Functions, Lists, Dictionaries, Loops, Conditional Statements, File Handling, Exception Handling and Input Validation.

## 4. Project Architecture

The application follows a modular structure by separating the main menu and task management operations into different Python files.

### Project Structure

```text
todo-list-manager/
│
├── main.py
├── todo.py
├── tasks.json
└── README.md
```

### Module Description

**main.py**
- Displays the menu to the user.
- Accepts and validates menu choices.
- Calls the appropriate task management functions.

**todo.py**
- Contains the task management functions.
- Handles adding, viewing, completing and removing tasks.
- Saves and loads task information using JSON.
- Performs task data validation.

**tasks.json**
- Stores task information in JSON format.
- Maintains task IDs, titles and completion status.

## 5. Core Features

1. **Add Tasks:** Allows users to create tasks with unique IDs and titles.
2. **View Tasks:** Displays all available tasks along with their IDs and completion status.
3. **Mark as Completed:** Updates the completion status of a selected task.
4. **Remove Tasks:** Deletes a task using its ID.
5. **Persistent Storage:** Saves task information in a JSON file.
6. **Error Handling:** Handles missing files, invalid JSON data and invalid task structures.

## 6. Design Decisions

- **Modular Programming:** Functions are used to separate individual operations, making the application easier to understand, maintain and modify.
- **Lists and Dictionaries:** A list stores multiple tasks, while dictionaries represent individual tasks using keys such as `id`, `title` and `completed`.
- **JSON File Handling:** JSON was selected as a lightweight storage format because it allows task information to be stored and retrieved without requiring a database.
- **Unique Task IDs:** New task IDs are generated based on the maximum existing ID to avoid reusing IDs after task deletion.
- **Exception Handling:** Specific exceptions are handled to prevent the application from terminating unexpectedly when encountering common file or input errors.

## 7. Application Logic Flow

The application follows this general sequence:

```text
       Start
         |
         v
    Load Tasks
         |
         v
     Display Menu
         |
         v
    Get User Choice
         |
         v
   Validate Choice
         |
         v
   Perform Operation
         |
    +----+----------------+
    |    |       |        |
    v    v       v        v
   Add  View   Complete  Remove
    |    |       |        |
    +----+-------+--------+
         |
         v
    Save Changes
         |
         v
   Return to Menu
         |
         v
    Exit Selected?
      /       \
    No         Yes
    |           |
    v           v
  Menu         End
```

## 8. Installation and Execution

### Prerequisites

- Python 3 installed on your system.
- A code editor or terminal to execute the application.

### Dependencies

The application uses Python's built-in `json` module. No external libraries or additional package installations are required.

### Steps to Run

1. Download or clone the project repository.
2. Open the project folder in your terminal.
3. Ensure that `main.py`, `todo.py` and `tasks.json` are present.
4. Execute the following command:

```bash
python3 main.py
```

5. Follow the menu displayed in the terminal to manage your tasks.

## 9. Testing Scenarios

The following scenarios can be used to test the application manually.

| Test Scenario | Expected Result |
|---|---|
| Add a new task | Task is added successfully |
| Enter an empty task title | Application requests a valid title |
| View existing tasks | All tasks are displayed |
| Mark a valid task ID as completed | Completion status changes to True |
| Enter a non-numeric task ID | Application displays an error and requests input again |
| Enter a non-existing task ID | Task not found message is displayed |
| Remove an existing task | Task is removed successfully |
| Restart the application | Previously saved tasks are loaded |

## 10. Conclusion

The Todo List Manager demonstrates the practical application of fundamental Python programming concepts through a functional command-line application. It provides essential task management operations while emphasizing modular design, data persistence, input validation and exception handling.

This project helped develop a better understanding of writing structured Python programs and designing applications that are simple, maintainable and reliable.