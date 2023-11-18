from tkinter import Tk, Canvas, Frame, Entry, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble:
    """A simple pen drawing application"""

    def __init__(self):
        master = Tk()
        master.title("Scribble")

        # Mouse coordinates and the drawing color are instance variable
        self.oldx, self.oldy = 0, 0
        self.color = "#8000FF"

        # Create canvas 800 X 500
        self.canvas = Canvas(master, height=500, width=800)

        # Bind mouse events to handlers:
        # -- Pressing the left mouse button
        self.canvas.bind("<Button-1>", self.begin)
        # -- Moving the mouse while holding/pressing left mouse button
        self.canvas.bind("<Button1-Motion>", self.draw)

        self.canvas.pack(expand=True, fill=BOTH)

        # Create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)

        self.bt_clear = Button(frame1, text="CLEAR", fg="white", bg="red", command=self.delete)
        self.bt_clear.pack(side=LEFT, padx=5)

        self.bt_color = Button(frame1, text="COLOR", bg=self.color, command=self.change_color)
        self.bt_color.pack(side=LEFT, padx=5)

        ### ADDITION: PEN SIZE
        frame2 = Frame(frame1)
        frame2.pack(side=LEFT, padx=5)

        size_label = Label(frame2, text="Canvas Size: ")
        size_label.pack(side=LEFT)

        self.size = Entry(frame2, width=5)
        self.size.insert("1", "10")
        self.size.pack(side=LEFT)

        self.message = Label(master, text="Press and drag the left mouse-button to draw")
        self.message.pack(side=BOTTOM)

        # Start the event loop
        master.mainloop()

    def begin(self, event):
        """Handle left button click by recording mouse position
            as the start of the curve"""
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        """Handle mouse motion, while pressing left button, by
            connecting the previous mouse position to the new one"""
        self.canvas.create_line((self.oldx, self.oldy, event.x, event.y), fill=self.color,
                                width=int(self.size.get()), capstyle="round")
        self.begin(event)

    def delete(self):
        """Clear the canvas"""
        self.canvas.delete("all")

    def change_color(self):
        """
        Change the drawing color using the color chooser,
        also change the background color of the color button
        """
        color = askcolor()
        self.color = color[-1]
        self.bt_color["bg"] = self.color

        # Change the color of the text for visibility
        percentage = sum(color[0]) / 756
        self.bt_color["fg"] = "black" if percentage >= .5 else "white"

if __name__ == "__main__":
    Scribble()