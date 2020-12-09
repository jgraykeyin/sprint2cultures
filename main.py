import tkinter as tk

# Initialize our main window, huzzah!
window = tk.Tk()

# Set the title of our window
window.title("Bacteria Culture-tron")

# Setup our first label
cultureid_label = tk.Label(window, text="Culture ID: ")

# Setup another label

# Stick that label into the grid!
cultureid_label.grid(row=1, column=1)

window.mainloop()


