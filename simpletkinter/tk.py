import tkinter as tk
# 1. Define all the operator with function
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

def calculate_expression(expression_str):
    # Remove any accidential whitespace
    expression_str = expression_str.replace(" ", "")
    
    operators = ['+', '-', '*', '/']
    chosen_operator = None
    operator_index = -1
    
    # Loop through the string to find the operator. 
    # i > 0  we don't  mistake a starting negative sign for the operator.
    for i, char in enumerate(expression_str):
        if i > 0 and char in operators:
            chosen_operator = char
            operator_index = i
            break
            
    if not chosen_operator:
        return "Error"
    
    try:
        # Split into operands based on the operator's exact position
        num1 = float(expression_str[:operator_index])
        num2 = float(expression_str[operator_index+1:])
        
        # Route to your custom functions
        if chosen_operator == '+': return add(num1, num2)
        if chosen_operator == '-': return subtract(num1, num2)
        if chosen_operator == '*': return multiply(num1, num2)
        if chosen_operator == '/': return divide(num1, num2)
            
    except (ValueError, IndexError):
        return "Error"

# 2. TKINTER BUTTON INTERACTION LOGIC
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


# 3. GUI LAYOUT SETUP

root = tk.Tk()
root.title("Custom Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry text box display
entry_box = tk.Entry(root, width=16, font=('Arial', 24), justify='right', bd=10, insertwidth=4)
entry_box.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout configurations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Generate and place buttons programmatically
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),command=on_equal_press)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),command=on_clear)
    elif text in ['+', '-', '*', '/']:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),command=lambda t=text: on_button_click(t))
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),command=lambda t=text: on_button_click(t))
        
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()