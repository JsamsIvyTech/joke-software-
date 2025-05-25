# program name: going no where fast
# author: jrs
# created: 2025-05-25
# This is a sample tkinter program that creates a GUI with buttons and labels.
# NO CODING ASSISTANCE WAS USED IN THE CREATION OF THIS PROGRAM

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Test Software")
root.geometry("600x400")

# first window that opens when the button is clicked
def open_window():
    window = tk.Toplevel(root)
    window.title("stoopid")
    window.geometry("400x300")
    label_open = tk.Label(window, text="nothing happened haha!!", padx=40, pady=40)
    label_open.pack()
    button_open = tk.Button(window, text="Click me to actually work this time", padx=5, pady=5, command=newer_window)
    button_open.pack()

# next window that opens with the other window
def newer_window():
    window = tk.Toplevel(root)
    window.title("again stoopid")
    window.geometry("400x300")
    label_open = tk.Label(window, text="nothing happened haha, i feel bad", padx=40, pady=40)
    label_open.pack()
    button_open = tk.Button(window, text="Click me to close this one", padx=5, pady=5, command=window.destroy)
    button_open.pack()

# the label that initaties the first window
label = tk.Label(root, text="Please click this button!!", padx=20, pady=20)
label.pack()

# Create a button that opens the first window
button = tk.Button(root, text="Click me NOWWW!!", padx=5, pady=5, command=open_window)
button.pack()


# Run the Tkinter event loop
root.mainloop()