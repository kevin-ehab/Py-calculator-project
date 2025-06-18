# 🧮Py-calculator-project

This project is a simple GUI calculator built using **Python's Tkinter library**. It supports basic arithmetic operations like addition, subtraction, multiplication, and division.

## ✨ Features

- Clickable buttons for digits (0-9) and operations (`+`, `-`, `*`, `/`)
- `=` button to evaluate the expression
- `Clear` button to reset the input field
- Error handling for invalid expressions

## 🛠 Tech Stack

- **Python**
- **Tkinter**

## 📋 How It Works:

### 🦾GUI Components

- **Entry widget**: Displays the current input and result.
- **Buttons**: Digit buttons (0-9), operation buttons, clear, and equals.

### ⚙️Logic

- The `Click()` function handles all input:
  - Adds digits and operations to the entry field.
  - Evaluates the expression when `=` is clicked using Python’s `eval()` function.
  - Clears the entry when `C` is clicked.
  - Shows `"Error"` if the expression is invalid.
## 🚀 How to Run

1. Make sure you have Python installed.
2. Save the code in a file named `calculator.py`.
3. Run the file.
## 📝 Author Notes

- This was one of my early projects in Python and GUI programming.
- It helped me understand event-driven programming and GUI layout using `grid()`.
