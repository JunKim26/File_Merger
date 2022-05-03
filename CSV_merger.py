# Title : CSV Files Merger
# Author: Jun Kim
# Date: 09/24/2021
# Description: In this program, all the csv files in a directory will be merged into one csv file. 


import os
import glob
import pandas as pd
import numpy as np
import tkinter as tk                                                                        
from tkinter import *
from tkinter.filedialog import askdirectory                                                 
from datetime import datetime      


def main():

    # initialize Tkinter GUI
    window = tk.Tk()                                                                        
    window.geometry('200x200')                                                              

    label = tk.Label(text='CSV Merger')                                                    
    label.pack()

    def directory_opener():
        """ this function is used for the button to open the csv file """

        global csv_folder
        csv_folder = askdirectory()                                                         

        end_button = Button(window, text = 'Create', command =window.destroy).pack()        
                                                                    
    csv_button = Button(window, text = 'Open Folder', command = directory_opener).pack()

    window.mainloop()                                                                       


    def csv_merge():
        """ merges csv files in a folder """
        
        os.chdir(csv_folder)
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        
        # combine all files in the list         
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])                  
        csv_df = pd.DataFrame(combined_csv)    
        
        # year_month_day-hours_minutes_seconds_AM/PM ; used in Title   
        dt = datetime.now().strftime('%Y.%m.%d-%I%M%S%p')                                              
        dt_string = str(dt)                                                               
        file_name = dt_string +" combined.csv"

        script_dir = os.path.dirname(__file__)                                              
        rel_path = 'Output'
        
        # this joins the absolute path of current script with wanted relative path
        abs_file_path = os.path.join(script_dir, rel_path)                
        
        csv_df = csv_df.dropna(axis=1, how='all')                                          

        last_path = os.path.basename(os.path.normpath(csv_folder))    

        csv_df.to_csv("../../Output/"+ dt_string +" "+ last_path + " combined.csv", index=False, encoding='utf-8-sig')            


    csv_merge()

if __name__ == '__main__':
    main()
