import tkinter as tk

# Function to handle button clicks
def click_button(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

# Function to clear the display
def clear():
    entry_var.set("")

# Function to calculate the result
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")


# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Variable for display
entry_var = tk.StringVar()

# Display screen
display = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.pack(fill="both", padx=10, pady=10, ipady=15)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")

    for button in row:
        if button == "C":
            command = clear
        elif button == "=":
            command = calculate
        else:
            command = lambda value=button: click_button(value)

        btn = tk.Button(
            row_frame,
            text=button,
            font=("Arial", 20),
            command=command
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Run the application
root.mainloop()