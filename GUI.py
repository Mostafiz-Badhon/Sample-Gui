# Template for a GUI module
# Contains AppFrame for creating frame objects. The AppFrame includes functions to display frame and swap between them.
# Add additional functionality to allow you to populate the frames with the GUI widgets you need.
# Expand the class or add additional classes to create the GUI for your coursework.

import tkinter as tk  # This has all the code for GUIs.
from functools import partial  # Partial allows us to fix a certain number of arguments of a function
                               # and generate a new function. It is used here to pass argument in a command clause.


class AppFrame:

    def __init__(self, logo_file, header_text, *args):
        """
        AppFrame creates frame objects and includes functionality to swap between frames.
        Takes 3 arguments:
        logo_file: string with name of png image to display - e.g. "logo.png"
        header_text: string to display in frame header
        *args: 2 variable arguments containing text to appear of frame button and next_frame object

        Use the variable arguments if you need to display more than one frame and swap between them.
        *args are not needed if you only have one frame or the frame is the last frame which contains an exit button.
        """

        # The widgets needed for each frame.
        # First, let's display the logo.
        self.img_logo = tk.PhotoImage(file=logo_file)
        self.app_frame = tk.Frame(root)
        self.lbl_logo = tk.Label(self.app_frame,
                                 image=self.img_logo)

        # Next, comes the heading for this frame.
        self.lbl_heading = tk.Label(self.app_frame,
                                    text=header_text)
        self.lbl_logo.pack()
        self.lbl_heading.pack()

        if len(args)>0:
            self.swap_frame(args[0], args[1])

    def swap_frame(self, button_text, next_frame):
        # And finally, the button to swap between the frames.
        if next_frame == exit_frame:
            self.btn_change_exit = tk.Button(self.app_frame,
                                             text='exit',
                                             command=self.app_frame.quit)
            self.btn_change_exit.pack()
        else:
            self.btn_change_to_next_frame = tk.Button(self.app_frame,
                                                      text=button_text,
                                                      command=partial(self.switch_to, next_frame))
            self.btn_change_to_next_frame.pack()

    def switch_to(self, next_frame):
        self.app_frame.pack_forget()
        next_frame.display_frame()

    def display_frame(self):
        self.app_frame.pack(fill='both', expand=1, )


# Now we get to the program itself:-
# Let's set up the app window ...
root = tk.Tk()
root.title("Example with AppFrame class")
# Set the icon used for your program
root.iconphoto(True,
               tk.PhotoImage(file='logo.png'))

# We create the last exit frame and others frames and display the first frame
exit_frame = AppFrame('logo.png', 'Last Frame')
third_frame = AppFrame('logo.png', 'Third Frame', 'Swap to Last Frame', exit_frame)
second_frame = AppFrame('logo.png', 'Second Frame', 'Swap to Third Frame', third_frame)
first_frame = AppFrame('logo.png', 'First Frame', 'Swap to Second Frame', second_frame)

first_frame.display_frame()

root.state('zoomed')
root.mainloop()
