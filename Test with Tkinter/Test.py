from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class Test(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Scratch Golf Course")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "Scratch Bar and Grill",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "fallGolf.png")
        imageLabel["image"] = self.image

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"


        self.addLabel(text = "Menu", row = 2, column = 0, columnspan = 1, rowspan = 1, background = "white", foreground = "orange", sticky = "NSEW")
        self.addLabel(text = "Hot Dog", row = 3, column = 0, columnspan = 1, rowspan = 1)
        
        

        




















        self.setBackground("gray1")

        

if __name__ == "__main__":
    Test().mainloop()



        

