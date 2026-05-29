# Tkinter Arithmetic Calculator

A custom graphical user interface (GUI) calculator built in Python using the `tkinter` module. 
This project ignore the eval ()
When the user requests an evaluation (`=`):
1. The string is read from the input layout module.
2. The custom string parser iterates over the expression to establish explicit boundary markers for operand substrings while safely managing leading negative symbols.
3. Isolated substrings are cast into functional numeric floats.
4. Calculations are systematically routed to dedicated math modules (`add`, `subtract`, `multiply`, `divide`).

## How to Run

1. Verify that your machine has Python 3.x installed.
2. Open your terminal, command line interface, or your IDE terminal window.
3. Target the local directory housing your project files:
   ```bash
    "d:/Python-Program/python assiment/simpletkinter/tk.py"