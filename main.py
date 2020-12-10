import tkinter as tk

# Initialize our main window, huzzah!
window = tk.Tk()

# Initialize variables that will be used to hold data later on.
# Bacteria_selection will be used for our Bacteria Dropdown menu.
bacteria_selection = tk.StringVar()
medicine_selection = tk.StringVar()

# Set the title of our window
window.title("Bacteria Culture-tron")

# Setup our labels and inputs
cultureid_label = tk.Label(window, text="Culture ID: ")
cultureid_input = tk.Entry(window)

# Here's the setup for our dropdown...
# First we create a list of options for the dropdown menu.
bacteria_list = ["Coccus", "Bacillus", "Spirillum", "Rickettsia", "Mycoplasma"]
bacteria_label = tk.Label(window, text="Bacteria Type: ")
bacteria_dropdown = tk.OptionMenu(window, bacteria_selection, bacteria_list)
# Set the default option to the first element in the list
bacteria_selection.set(bacteria_list[0])

# And here's the setup for our medicine dropdown
medicine_list = ["Control", "Formula-FD102", "Formula-FD201", "Formula-FD202", "Formula-FD505"]
medicine_label = tk.Label(window, text="Medicine: ")
medicine_dropdown = tk.OptionMenu(window, medicine_selection, medicine_list)
medicine_selection.set(medicine_list[0])

# Next we'll setup our 6am and 6pm bacteria count inputs
morning_label = tk.Label(window, text="Bacteria Count (6AM): ")
morning_input = tk.Entry(window)

evening_label = tk.Label(window, text="Bacteria Count (6PM): ")
evening_input = tk.Entry(window)

# Setup our grid placements for the labels & inputs
# Sticky=W means keep the element stuck to the west side of the window
# padx and pady adds empty space around the element to make it look nicer
# (I tend to put all my grid placements together to keep things nice and tidy)
cultureid_label.grid(row=0, column=0, padx=6, pady=6, sticky="W")
cultureid_input.grid(row=0, column=1, padx=6, pady=6, sticky="W")

bacteria_label.grid(row=1, column=0, padx=6, pady=6, sticky="W")
bacteria_dropdown.grid(row=1, column=1, padx=6, pady=6, sticky="W")

medicine_label.grid(row=2, column=0, padx=6, pady=6, sticky="W")
medicine_dropdown.grid(row=2, column=1, padx=6, pady=6, sticky="W")

morning_label.grid(row=3, column=0, padx=6, pady=6, sticky="W")
morning_input.grid(row=3, column=1, padx=6, pady=6, sticky="W")

evening_label.grid(row=4, column=0, padx=6, pady=6, sticky="W")
evening_input.grid(row=4, column=1, padx=6, pady=6, sticky="W")

window.mainloop()


