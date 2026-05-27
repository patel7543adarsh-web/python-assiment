import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.configure(bg="#1e1e24")  # Dark background
root.resizable(False, False)

# Global variable to store the expression
expression = ""


def press(num):
    """Appends the pressed button value to the expression."""
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    """Evaluates the final expression."""
    global expression
    try:
        # eval calculates the string expression directly
        total = str(eval(expression))
        equation.set(total)
        expression = total  # Keep the result for further calculations
    except ZeroDivisionError:
        equation.set("Error: Div by 0")
        expression = ""
    except Exception:
        equation.set("Error")
        expression = ""


def clear():
    """Clears the display."""
    global expression
    expression = ""
    equation.set("")


# StringVar to update the entry widget dynamically
equation = tk.StringVar()

# Display Screen
display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    bg="#2a2a35",
    fg="#ffffff",
    bd=0,
    justify="right",
)
display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# Button configurations
button_config = {
    "font": ("Arial", 14, "bold"),
    "fg": "#ffffff",
    "activebackground": "#4a4a5a",
    "activeforeground": "#ffffff",
    "bd": 0,
    "height": 2,
    "width": 5,
}

# Frame to hold the buttons
button_frame = tk.Frame(root, bg="#1e1e24")
button_frame.pack()

# Define layout and specific button colors
buttons = [
    ("C", 0, 0, "#d9534f"),
    ("/", 0, 3, "#f0ad4e"),
    ("7", 1, 0, "#3a3a45"),
    ("8", 1, 1, "#3a3a45"),
    ("9", 1, 2, "#3a3a45"),
    ("*", 1, 3, "#f0ad4e"),
    ("4", 2, 0, "#3a3a45"),
    ("5", 2, 1, "#3a3a45"),
    ("6", 2, 2, "#3a3a45"),
    ("-", 2, 3, "#f0ad4e"),
    ("1", 3, 0, "#3a3a45"),
    ("2", 3, 1, "#3a3a45"),
    ("3", 3, 2, "#3a3a45"),
    ("+", 3, 3, "#f0ad4e"),
    ("0", 4, 0, "#3a3a45"),
    (".", 4, 1, "#3a3a45"),
    ("=", 4, 2, "#5cb85c"),
]

# Create and place buttons dynamically using grid
for text, row, col, color in buttons:
    # Assign specific actions based on the button type
    if text == "C":
        action = clear
    elif text == "=":
        action = equalpress
    else:
        action = lambda x=text: press(x)

    # Specific tweak to make '=' stretch across two columns
    if text == "=":
        btn = tk.Button(
            button_frame, text=text, bg=color, command=action, **button_config
        )
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
    else:
        btn = tk.Button(
            button_frame, text=text, bg=color, command=action, **button_config
        )
        btn.grid(row=row, column=col, padx=5, pady=5)

# Start the application loop
root.mainloop()