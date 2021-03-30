
from ESandED import parseSequences,wagner_fischer

from tkinter import *

from tkinter import filedialog


# Create the root window
window = Tk()

# Set window title
window.title('Differencing Tool')

# Set window size
window.geometry("700x500")

# Set window background color
window.config(background = "white")

# Labels
label_file_explorer = Label(window,
                            text = "Edit Distance and Edit Script Generator",
                            width = 100, height = 4,
                            fg = "black",bg='#fcfc03',
                            justify= CENTER,
                            )

label_dist=Label(window, text="Distance: Not Calculated Yet",
                 width=100,height=4,
                 justify=CENTER)

label_sim=Label(window, text="Similarity: Not Calculated Yet",
                width=100,height=4,
                justify=CENTER)



# functions to be used with buttons
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("XML files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: ")
    sequences=parseSequences(filename)
    a,dist,sim=wagner_fischer(sequences[0],sequences[1])
    label_dist.configure(text="Distance: "+str(dist))
    label_sim.configure(text="Similarity: "+str(sim))

# Buttons
button_explore = Button(window,
                        text = "Get Edit Script",
                        command = browseFiles)


# Grids
label_file_explorer.grid(column = 1, pady=10,row = 1)

button_explore.grid(column = 1, pady=10,row = 2)

label_dist.grid(column=1,pady=10,row=3)

label_sim.grid(column=1,pady=10,row=4)

# Let the window wait for any events
window.mainloop()


