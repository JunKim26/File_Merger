# Title : CSV Files Merger
# Author: Jun Kim
# Date: 09/24/2021
# Description: In this program, all the csv files in a directory will be merged into one csv file. 


import os
import glob
import pandas as pd
import numpy as np
from datetime import date                                                                   # used to get the current date
from datetime import datetime      
import tkinter as tk                                                                        # used as a user friendly tool for the program
from tkinter.filedialog import askdirectory                                                 # used to open csv file
from tkinter import StringVar                                                           
from tkinter import *


def main():

# =======================================================================================================================================================
#                                                           Script lines for Tkinter GUI
# =======================================================================================================================================================



    window = tk.Tk()                                                                        # creates a tkinter object
    window.geometry('200x200')                                                              # set size of tkinter window

    label = tk.Label(text='CSV Merger')                                                     # sets the text to be dipslayed by tkinter
    label.pack()

    def csv_opener():
        """ this function is used for the button to open the csv file """

        global csv_folder
        csv_folder = askdirectory()                                                         # show an "Open" dialog box and return the path to the selected folder

        end_button = Button(window, text = 'Create', command =window.destroy).pack()        # button to close tkinter window
                                                                    
    csv_button = Button(window, text = 'Open Folder', command = csv_opener).pack()

    window.mainloop()                                                                       # tells Python to run the Tkinter event loop

# =======================================================================================================================================================
#                                                           Main Function Section
# =======================================================================================================================================================
