import tkinter as tk
import tkinter.simpledialog
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


# Initialize our main window, huzzah!
window = tk.Tk()
# Set the title of our window
window.title("Bacteria Culture-tron")

# This function waits for the exit button to be pressed to end the program
def exit_button_press():
    exit()

# This function is used to read data from a file and return a list of all the content in that file
def get_file_data(file):
    data = []
    filename = file + ".dat"
    file = open(filename, "r")
    contents = file.readlines()

    for line in contents:
        data.append(line)

    return data


# Function to remove the selected entry from the listbox when the remove button is pressed
def remove_button_press():

    # Command to delete the currently selected item
    delete_entry = listbox.delete((listbox.curselection()))

    # Remove graph image if it's there
    img_label["image"] = ""
    img_label.image = ""

    # And let's disable some of the buttons since we know the currently selected item is gone now
    remove_button["state"] = "disable"
    linear_button["state"] = "disable"
    save_button["state"] = "disable"


# This function looks a little intense, it could probably be improved a little bit...
# But it's meant to fill in all the fields when you click a data-line that's been added to a listbox.
def list_item_selected(msg):

    # If an item has been selected in the listbox, we should also enable the linear button and delete buttons
    linear_button["state"] = "normal"
    remove_button["state"] = "normal"

    data = listbox.get(listbox.curselection())

    items = data.split(":")

    cultureid_input.set(items[0])

    # Overly complicated way of finding out which bacteria was selected.
    # There's probably a much better way of doing this...
    x=0
    bacteria_index = 0
    while x <= len(bacteria_list):
        if items[1] == bacteria_list[x]:
            bacteria_index = x
            break
        x+=1

    # And do it again for the medicine.
    x=0
    medicine_index = 0
    while x <= len(medicine_list):
        if items[2] == medicine_list[x]:
            medicine_index = x
            break
        x+=1

    bacteria_selection.set(bacteria_list[bacteria_index])
    medicine_selection.set(medicine_list[bacteria_index])
    morning_input.set(items[3])
    evening_input.set(items[4])



# This function will generate a linear graph when button is pressed.
# It asks the user for a start value and end value.
# It then calculates the points by using y = a*x+b based on our evening and morning readings.
def linear_button_press():
    # Setup empty lists for holding our x and y plotting data
    x_points = []
    y_points = []

    # Ask the user for the start and end range values
    start_x = tk.simpledialog.askfloat("Start Range", "Enter Starting x Value")
    end_x = tk.simpledialog.askfloat("End Range", "Enter Ending x Value")

    # Get the morning and evening readings from our inputs
    # This probably needs validation to make sure actual numbers were entered
    #morning = float(morning_input.get())
    #evening = float(evening_input.get())
    data = listbox.get(listbox.curselection())
    items = data.split(":")
    morning = float(items[3])
    evening = float(items[4])

    # Set the a & b values according to the instructions provided
    a = (evening - morning) / 12
    b = morning

    # Apply the linear equation to every point between start_x and end_x
    # Save each x & y value into lists so they can be used for plotting.
    x = start_x
    while x < end_x:
        y = a * x + b

        x_points.append(x)
        y_points.append(y)
        x+=1

    # Plot all our points onto a graph and save it as graph.png
    plt.plot(x_points, y_points)
    plt.savefig("graph.png")
    # This command clears the area so the next graph won't overlap it, keeping things tidy.
    plt.clf()

    # Then we can take that same image and load it into our img_label
    img = Image.open("graph.png")
    photo = ImageTk.PhotoImage(img)
    img_label["image"] = photo
    img_label.image = photo


# Just a little function to clear all inputs that we can use anytime we need it.
def clear_inputs():
    cultureid_input.set("")
    bacteria_selection.set(bacteria_list[0])
    medicine_selection.set(medicine_list[0])
    morning_input.set("")
    evening_input.set("")


# This function will trigger each time the confirm button is pressed.
# All information entered by user will be added to the listbox.
def confirm_button_press():
    # Save the user inputs into variables so they're easier to play with.
    culture_id = cultureid_input.get()
    bacteria_type = bacteria_selection.get()
    medicine_type = medicine_selection.get()

    # We have to make sure these values are floats so we can do math things.
    morning_reading = float(morning_input.get())
    evening_reading = float(evening_input.get())

    # Calculate the rate of change in the readings, for science.
    rate_change = (evening_reading / morning_reading) - 1

    # Create a string that contains all the above values
    data_string = culture_id + ":" + bacteria_type + ":" + medicine_type + ":" + str(morning_reading) + ":" + str(
        evening_reading) + ":" + str(rate_change)

    # Now let's send that big string over to your list box
    listbox.insert(0, data_string)

    # And clear out all the values to reset the inputs
    clear_inputs()

    # Make sure we enable the save button now that we have data added into the listbox
    save_button["state"] = "normal"


# This function will trigger when the save button is pressed.
# All data inside the listbox will be saved into a file.
def save_button_press():

    # Save the contents of the listbox into our own list
    list_contents = listbox.get(0,tk.END)

    # Ask user to provide a filename
    user_filename = tk.simpledialog.askstring("Save", "Please enter a filename: ")

    # Open a file that we'll use to save the data
    save_file = open(user_filename, "w")

    # Loop through our list and write each line into our save file
    for item in list_contents:
        save_file.write(item + "\n")

    # Close the file and say goooood-bye
    save_file.close()


# Create our frames so we can organize all our elements
# All our labels, dropdowns and entry boxes will go into the frame_inputs frame.
# The listbox will go into the frame_outputs frame.
frame_inputs = tk.Frame(window)
frame_outputs = tk.Frame(window)
frame_input_buttons = tk.Frame(window)
frame_output_buttons = tk.Frame(window)
frame_graphs = tk.Frame(window)

frame_inputs.grid(row=0, column=0, padx=10,pady=10)
frame_outputs.grid(row=0, column=1, padx=10, pady=10)
frame_input_buttons.grid(row=1, column=0, padx=10, pady=10)
frame_output_buttons.grid(row=1, column=1, padx=10, pady=10)
frame_graphs.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Initialize variables that will be used to hold data later on.
# Each of these variables will be attached to elements in our window (usually set with textvariable)
cultureid_input = tk.StringVar()
bacteria_selection = tk.StringVar()
medicine_selection = tk.StringVar()
morning_input = tk.StringVar()
evening_input = tk.StringVar()
list_data = tk.StringVar()


# Setup our labels and inputs
cultureid_label = tk.Label(frame_inputs, text="Culture ID: ")
cultureid_entry = tk.Entry(frame_inputs, textvariable=cultureid_input)

# Here's the setup for our dropdown...
# First we create a list of options for the dropdown menu.
bacteria_list = get_file_data("bacteria")

bacteria_label = tk.Label(frame_inputs, text="Bacteria Type: ")
bacteria_dropdown = tk.OptionMenu(frame_inputs, bacteria_selection, *bacteria_list)
# Set the default option to the first element in the list
bacteria_selection.set(bacteria_list[0])

# And here's the setup for our medicine dropdown
medicine_list = get_file_data("medicine")
medicine_label = tk.Label(frame_inputs, text="Medicine: ")
medicine_dropdown = tk.OptionMenu(frame_inputs, medicine_selection, *medicine_list)
medicine_selection.set(medicine_list[0])

# Next we'll setup our 6am and 6pm bacteria count inputs
morning_label = tk.Label(frame_inputs, text="Bacteria Count (6AM): ")
morning_entry = tk.Entry(frame_inputs, textvariable=morning_input)

evening_label = tk.Label(frame_inputs, text="Bacteria Count (6PM): ")
evening_entry = tk.Entry(frame_inputs, textvariable=evening_input)

# Next up is the listbox, but this will be placed on the frame_outputs frame
# This will probably be the only element in it's frame, it's lonely but it's still cool.
listbox = tk.Listbox(frame_outputs, width=40, listvariable=list_data)
listbox.bind('<<ListboxSelect>>',list_item_selected)

# And finally we'll setup our buttons into a button frame.
confirm_button = tk.Button(frame_input_buttons, text="Confirm", command=confirm_button_press)
clear_button = tk.Button(frame_input_buttons, text="Clear Inputs", command=clear_inputs)
exit_button = tk.Button(frame_input_buttons, text="Exit", command=exit_button_press)

save_button = tk.Button(frame_output_buttons, text="Save", command=save_button_press, state="disable")
linear_button = tk.Button(frame_output_buttons, text="Linear Projection", command=linear_button_press, state="disable")
remove_button = tk.Button(frame_output_buttons, text="Remove Reading", command=remove_button_press, state="disable")

# Setup an empty label that we can use to display a graph after it's been created
img_label = tk.Label(frame_graphs)

# Setup our grid placements for the labels & inputs
# Sticky=W means keep the element stuck to the west side of the window
# padx and pady adds empty space around the element to make it look nicer
# (I tend to put all my grid placements together to keep things nice and tidy)
cultureid_label.grid(row=0, column=0, padx=6, pady=6, sticky="W")
cultureid_entry.grid(row=0, column=1, padx=6, pady=6, sticky="W")

bacteria_label.grid(row=1, column=0, padx=6, pady=6, sticky="W")
bacteria_dropdown.grid(row=1, column=1, padx=6, pady=6, sticky="W")

medicine_label.grid(row=2, column=0, padx=6, pady=6, sticky="W")
medicine_dropdown.grid(row=2, column=1, padx=6, pady=6, sticky="W")

morning_label.grid(row=3, column=0, padx=6, pady=6, sticky="W")
morning_entry.grid(row=3, column=1, padx=6, pady=6, sticky="W")

evening_label.grid(row=4, column=0, padx=6, pady=6, sticky="W")
evening_entry.grid(row=4, column=1, padx=6, pady=6, sticky="W")

listbox.grid(row=0, column=0, padx=6, pady=6, sticky="NSEW")

confirm_button.grid(row=0, column=0, padx=6, pady=6)
clear_button.grid(row=0, column=1, padx=6, pady=6)
exit_button.grid(row=0, column=2, padx=6, pady=6)

save_button.grid(row=0, column=0, padx=6, pady=6)
linear_button.grid(row=0, column=1, padx=6, pady=6)
remove_button.grid(row=0, column=2, padx=6, pady=6)

img_label.grid(row=0, column=0)

window.mainloop()


