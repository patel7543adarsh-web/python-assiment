import tkinter as tk
from tkinter import messagebox
import re

# 1. DEFINE BASIC MATH OPERATIONS & GLOBAL TRACKING
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b == 0:
        return "Error (Div by 0)"
    return a / b

# Global variable to track the calculator's state/history
calculation_history = []

def calculate_expression(expression_str):
    global calculation_history
    expression_str = expression_str.replace(" ", "")
    
    if not expression_str:
        return ""

    try:
        tokens = re.findall(r'(?<!\d)-?\d+\.\d+|(?<!\d)-?\d+|[+\-*/]', expression_str)
        
        if not tokens:
            return "Error"

        # Check if the expression starts with an accidental dangling operator
        if tokens[0] in ['+', '-', '*', '/']:
            return "Error"
            
        # sequential calculation starting with the first number
        result = float(tokens[0])
        
        #  sequentially from left to right
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            
            # Validation check for  operators
            if i + 1 >= len(tokens):
                return "Error"
                
            next_number = float(tokens[i + 1])
            
            # calculations custom math functions
            if operator == '+': 
                result = add(result, next_number)
            elif operator == '-': 
                result = subtract(result, next_number)
            elif operator == '*': 
                result = multiply(result, next_number)
            elif operator == '/': 
                res = divide(result, next_number)
                if isinstance(res, str):  # Checks if "Error (Div by 0)" was returned
                    return res
                result = res
            else:
                return "Error"
            
            i += 2  # Jump to the next operator pair

        # If it's a clean whole number, '.0'
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        # Update our global history variable
        calculation_history.append(f"{expression_str} = {result}")
        print(f"Global History Log: {calculation_history}") # Verifies state changes in console
        
        return result
            
    except (ValueError, IndexError, Exception):
        return "Error"

# 3. TKINTER BUTTON  LOGIC
def on_button_click(char):
    """Appends characters to the display screen."""
    entry_box.insert(tk.END, char)

def on_clear():
    """Clears the display screen entirely."""
    entry_box.delete(0, tk.END)

def on_equal_press():
    """Triggers the custom parsing logic and displays the result."""
    current_text = entry_box.get()             
    result = calculate_expression(current_text) 
    entry_box.delete(0, tk.END)                 
    entry_box.insert(0, str(result))          

# 4. GUI LAYOUT SETUP
root = tk.Tk()
root.title("Custom Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Entry text box display
entry_box = tk.Entry(root, width=15, font=('Arial', 24), justify='right', bd=10, insertwidth=4)
entry_box.grid(row=0, column=0, columnspan=4, pady=15, padx=10)

# Button layout configurations (Added '.' for decimal support)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3), 
]

# Generate and place buttons programmatically
for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14, 'bold'), bg="#d9534f", fg="white", command=on_clear)
    else:
        # Determine unique button highlighting styles
        if text in ['+', '-', '*', '/']:
            bg_color, fg_color = "#f0ad4e", "white"
        elif text == '.':
            bg_color, fg_color = "#eeeeee", "black"
        else:
            bg_color, fg_color = "#f9f9f9", "black"

        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), bg=bg_color, fg=fg_color,
                        command=lambda t=text: on_button_click(t))
        
    btn.grid(row=row, column=col, padx=5, pady=5)

# Big Equal Button at the bottom spanning across rows
equal_btn = tk.Button(root, text="=", font=('Arial', 14, 'bold'), bg="#5cb85c", fg="white", command=on_equal_press)
equal_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10, sticky="ew")

# Make rows and columns
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()