import tkinter as tk
from datetime import datetime

class UTCTimeDisplay(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = tk.Label(self, text="  UTC time: {}".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')), font="Roboto 12")
        self.label.pack(side="left")
        self.quit_button = tk.Button(self, text="  X  ", font="Arial 10 bold", fg="red", highlightthickness=0, bd=0, command=root.quit)
        self.quit_button.pack(side="right")
        self.update_display()

    def update_display(self):
        self.label.config(text="UTC time: {}".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')))
        self.after(1000, self.update_display) # update every second

root = tk.Tk()
root.overrideredirect(True) # remove the title bar and borders
root.geometry("+{}+{}".format(root.winfo_screenwidth()-450, root.winfo_screenheight()-150)) # set the window location to the bottom right corner
root.wm_attributes("-topmost", 1) # make the window always stay on top
root.lift()

app = UTCTimeDisplay(master=root)
app.pack()

# bind the <B1-Motion> event to the root window to enable dragging
root.bind("<B1-Motion>", lambda event: root.geometry("+{}+{}".format(event.x_root, event.y_root)))
root.bind("<ButtonPress-1>", lambda event: root.focus_set())

root.mainloop()
