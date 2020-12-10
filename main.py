import tkinter as tk

# Initialize our main window, huzzah!
window = tk.Tk()

# Create our frames so we can organize all our elements
# All our labels, dropdowns and entry boxes will go into the frame_inputs frame.
# The listbox will go into the frame_outputs frame.
frame_inputs = tk.Frame(window)
frame_outputs = tk.Frame(window)

frame_inputs.grid(row=0, column=0, padx=10,pady=10)
frame_outputs.grid(row=0, column=1, padx=10, pady=10)

# Initialize variables that will be used to hold data later on.
# Bacteria_selection will be used for our Bacteria Dropdown menu.
bacteria_selection = tk.StringVar()
medicine_selection = tk.StringVar()

# Set the title of our window
window.title("Bacteria Culture-tron")

# Setup our labels and inputs
cultureid_label = tk.Label(frame_inputs, text="Culture ID: ")
cultureid_input = tk.Entry(frame_inputs)

# Here's the setup for our dropdown...
# First we create a list of options for the dropdown menu.
bacteria_list = ["Coccus", "Bacillus", "Spirillum", "Rickettsia", "Mycoplasma"]
bacteria_label = tk.Label(frame_inputs, text="Bacteria Type: ")
bacteria_dropdown = tk.OptionMenu(frame_inputs, bacteria_selection, *bacteria_list)
# Set the default option to the first element in the list
bacteria_selection.set(bacteria_list[0])

# And here's the setup for our medicine dropdown
medicine_list = ["Control", "Formula-FD102", "Formula-FD201", "Formula-FD202", "Formula-FD505"]
medicine_label = tk.Label(frame_inputs, text="Medicine: ")
medicine_dropdown = tk.OptionMenu(frame_inputs, medicine_selection, *medicine_list)
medicine_selection.set(medicine_list[0])

# Next we'll setup our 6am and 6pm bacteria count inputs
morning_label = tk.Label(frame_inputs, text="Bacteria Count (6AM): ")
morning_input = tk.Entry(frame_inputs)

evening_label = tk.Label(frame_inputs, text="Bacteria Count (6PM): ")
evening_input = tk.Entry(frame_inputs)

# And finally we'll setup our Confirm button
confirm_button = tk.Button(frame_inputs, text="Confirm")

# Next up is the listbox, but this will be placed on the frame_outputs frame
listbox = tk.Listbox(frame_outputs, width=25)


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

confirm_button.grid(row=5, column=0, columnspan=2, padx=6, pady=6, sticky="E")

listbox.grid(row=0, column=0, padx=6, pady=6, sticky="NSEW")

window.mainloop()


