from tkinter import *
from ESandED import patchtoInitial,patchtoTarget

# import filedialog module
from tkinter import filedialog

# Create the root window
window = Tk()

# Set window title
window.title('Patching Gui')

# Set window size
window.geometry("700x500")

# Set window background color
window.config(background = "white")

# input
sequenceInput = Entry(window)



# functions

def toTarget():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("XML files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))
    print(sequenceInput.get())
    target = patchtoTarget(sequenceInput.get().upper(),filename)
    patched_sequence.configure(text=target)


def toInitial():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("XML files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))
    print(sequenceInput.get())
    initial=patchtoInitial(sequenceInput.get(),filename)
    patched_sequence.configure(text=initial)


# Labels
label_file_explorer = Label(window,
                            text = "Bidirectional Patching Tool",
                            width = 100, height = 4,bg='#8bed8e',
                            fg = "black",
                            justify= CENTER
                            )


patched_sequence = Label(window,
                         text = "Output Sequence",
                         width = 100, height = 5,
                         fg = "black",
                         justify= CENTER

                         )

# buttons
button_explore = Button(window,
                        text = "Initial To Target",
                        command = toTarget)

button_exit = Button(window,
                     text = "Target to Initial",
                     command = toInitial)



# Grids
label_file_explorer.grid(column = 1, pady=10,row = 1)

sequenceInput.grid(column=1,pady=10,row=2)

button_explore.grid(column = 1, pady=10,row = 3)

button_exit.grid(column = 1,pady=10,row = 4)

patched_sequence.grid(column=1,pady=10,row=5,columnspan=4,sticky=N+S+W+E)

# Let the window wait for any events
window.mainloop()