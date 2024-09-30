import tkinter as tk
from tkinter import messagebox # extra import

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

import logging

#Following tutorial here: https://www.youtube.com/watch?v=ibf5cx221hk


class MyGui:

    def __init__(self,fig):

        # Define the main window
        self.root = tk.Tk()
        
        # Define the title of the window
        self.root.title("Plot tracks")
        
        # Set the size of the window
        self.root.geometry("1000x750")
        
        # Add a figure
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()
        
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        '''
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close without question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        '''
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.mainloop()

    def show_message(self):
        logging.info("Hello World") # print "Hello World" if the button is clicked
        logging.info(self.check_state.get()) # If the checkbox is checked and the button clicked -> 1, if the checkbox is not checked and the button clicked -> 0

        if self.check_state.get() == 0:
            logging.info(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        logging.info(event.keysym)
        logging.info(event.state)

        if event.state == 12 and event.keysym == "Return":
            logging.info("Hello")
            self.show_message()

    def on_closing(self):
        logging.info("Hello World")
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        
    
        

if __name__ == "__main__":
    MyGui()