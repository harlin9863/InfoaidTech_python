import tkinter as tk
from tkinter import ttk

def add_item():
    # Get the text from the entry field
    text = entry.get()
    # Add the text to the listbox
    listbox.insert(tk.END, text)
    # Clear the entry field
    entry.delete(0, tk.END)

def remove_item():
    # Get the selected item from the listbox
    selected_item = listbox.get(tk.ANCHOR)
    # Remove the selected item from the listbox
    listbox.delete(tk.ANCHOR)

def save_list():
    # Get the items from the listbox
    items = listbox.get(0, tk.END)
    # Save the items to a file
    with open("to-do-list.txt", "w") as file:
        for item in items:
            file.write(item + "\n")

def load_list():
    # Clear the current listbox
    listbox.delete(0, tk.END)
    # Load items from a file
    try:
        with open("to-do-list.txt", "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        print("File not found.")

# Create the main window
window = tk.Tk()
window.title("To-Do List App")

# Create a frame for the to-do list
frame = ttk.Frame(window)
frame.pack()

# Create a label for the to-do list
label = ttk.Label(frame, text="To-Do List")
label.pack()

# Create an entry widget for user input
entry = ttk.Entry(frame)
entry.pack()

# Create a listbox for the to-do list
listbox = tk.Listbox(frame)
listbox.pack()

# Create buttons for adding, removing, saving, and loading
add_button = ttk.Button(frame, text="Add", command=add_item)
add_button.pack()

remove_button = ttk.Button(frame, text="Remove", command=remove_item)
remove_button.pack()

save_button = ttk.Button(frame, text="Save", command=save_list)
save_button.pack()

load_button = ttk.Button(frame, text="Load", command=load_list)
load_button.pack()

# Start the Tkinter event loop
window.mainloop()
