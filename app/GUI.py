import tkinter as tk
from tkinter import messagebox # extra import

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

import logging




class MyGui:

    def __init__(self,data,unique_track_ids,track_id_col_name):
    
        self.data = data
        self.unique_track_ids = unique_track_ids
        self.track_id_col_name = track_id_col_name
        
        # Define the main window
        self.root = tk.Tk()
        
        # Define the title of the window
        self.root.title("Plot tracks")
        
        # Set the size of the window
        self.root.geometry("1000x1000")
        
        # Add some information
        self.label = tk.Label(self.root, text='Upon closure of this window,\ndata for selected tracks will be passed on to the next App', font=('Arial', 20))
        self.label.pack(ipadx=10, ipady=10)
        
        # Add the figure
        fig = Figure(figsize = (4.5,4.5))
        self.ax = fig.add_subplot()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.plot_tracks(self.data,self.track_id_col_name,self.ax)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()
        
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.get_tk_widget().pack()
        
        # Make a check button for each of the tracks
        self.label = tk.Label(self.root, text='Select tracks', font=('Arial', 20))
        self.label.pack(ipadx=10, ipady=10)
        self.include_track = dict(zip(self.unique_track_ids,[0]*len(self.unique_track_ids)))
        for i in self.unique_track_ids:
            self.include_track[i] = tk.IntVar(value=1)
            self.check = tk.Checkbutton(self.root, text=i, font=('Arial', 16), variable=self.include_track[i])
            self.check.pack()
        
        # Add a button to save the data for the selected tracks
        self.button = tk.Button(self.root, text="Save data for selected tracks", font=('Arial', 18), command=self.save_tracks)
        self.button.pack(padx=10, pady=10)
            
        # Check whether one of the checkboxes has changed and update the plot if it did
        for i in self.unique_track_ids:
            self.include_track[i].trace("w",self.update_data)
        
        # Close the window if asked
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def update_data(self,*args):
        # Check which tracks are selected and save them in a list
        include_track = []
        for i in self.unique_track_ids:
            if self.include_track[i].get() == 1:
                include_track.append(i)
        
        # Updata the data to only include selected individuals
        updated_data = self.data[self.data[self.track_id_col_name].isin(include_track)]
        logging.info("One of the individuals was selected/unselected")
        self.plot_tracks(updated_data,self.track_id_col_name,self.ax)
        
    
    def plot_tracks(self,data,track_id_col_name,ax):
        ax.clear()
        if len(data) > 0:
            data.plot(ax=ax,column=track_id_col_name,alpha=0.5)
        self.canvas.draw()
        
    def save_tracks(self):
        return self.data
        
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
        

if __name__ == "__main__":
    MyGui()