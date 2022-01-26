# Title : CSV Files Merger
# Author: Jun Kim
# Date: 09/24/2021
# Description: In this program, all the csv files in a directory will be merged into one csv file. 


import os
import glob
import pandas as pd
import numpy as np
import tkinter as tk                                                                        # used as a user friendly tool for the program
from tkinter import *
from tkinter.filedialog import askdirectory                                                 # used to open csv file
from datetime import datetime      


def main():

# =======================================================================================================================================================
#                                                           Script lines for Tkinter GUI
# =======================================================================================================================================================



    window = tk.Tk()                                                                        # creates a tkinter object
    window.geometry('200x200')                                                              # set size of tkinter window

    label = tk.Label(text='CSV Merger')                                                     # sets the text to be dipslayed by tkinter
    label.pack()

    def directory_opener():
        """ this function is used for the button to open the csv file """

        global csv_folder
        csv_folder = askdirectory()                                                         # show an "Open" dialog box and return the path to the selected folder

        end_button = Button(window, text = 'Create', command =window.destroy).pack()        # button to close tkinter window
                                                                    
    csv_button = Button(window, text = 'Open Folder', command = directory_opener).pack()

    window.mainloop()                                                                       # tells Python to run the Tkinter event loop

# =======================================================================================================================================================
#                                                           Main Function Section
# =======================================================================================================================================================


    def csv_merge():
        os.chdir(csv_folder)
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                                                                                    
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])                  # combine all files in the list
        csv_df = pd.DataFrame(combined_csv)    

        dt = datetime.now().strftime('%Y.%m.%d-%I%M%S%p')                                   # year_month_day-hours_minutes_seconds_AM/PM ; used in Title                
        dt_string = str(dt)                                                                 # string of date and time
        file_name = dt_string +" combined.csv"

        script_dir = os.path.dirname(__file__)                                              # absolute directory the script is in
        rel_path = 'Output'
        abs_file_path = os.path.join(script_dir, rel_path)                                  # this joins the absolute path of current script with wanted relative path

        csv_df = csv_df.dropna(axis=1, how='all')                                           # this drops all columns without any values


        # =====================================================================

        last_path = os.path.basename(os.path.normpath(csv_folder))    

        csv_df.to_csv("../../Output/"+ dt_string +" "+ last_path + " combined.csv", index=False, encoding='utf-8-sig')            


    csv_merge()

if __name__ == '__main__':
    main()
