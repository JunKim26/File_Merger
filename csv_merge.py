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
        
# =======================================================================================================================================================
#                                                           Main Function Section
# =======================================================================================================================================================

    def rename_column(rename_df):
        
        rename_df.rename(columns={
                        'cs_hid' : 'Household ID', 
                        'profile_url': 'Linkedin Link', 
                        'email':"Email",
                        'full_name':"Household Name",
                        'first_name':"First Name",
                        'last_name':"Last Name",
                        'avatar':"LinkedIn Profile Picture URL",
                        'location_name':"Location",
                        'industry':"Industry",
                        'address':"Address",
                        'birthday':"Birthdate",
                        'organization_1':"Employed By",
                        'organization_title_1':"Title",
                        'organization_start_1':"Hire Date",
##                      'organization_2':"",
##                      'organization_title_2':"",
##                      'organization_3':"",
##                      'organization_title_3':"",
                        'education_1':"Education",
##                      'education_degree_1':"",
##                      'education_fos_1':"",
                        'education_start_1':"Education Start Date",
                        'education_end_1':"Education End Date",
##                      'education_2':"",
##                      'education_degree_2':"",
##                      'education_fos_2':"",
##                      'education_start_2':"",
##                      'education_end_2':"",
##                      'education_3':"",
##                      'education_degree_3':"",
##                      'education_fos_3':"",
##                      'education_start_3':"",
##                      'education_end_3':"",
##                      'language_1':"Language",
##                      'language_proficiency_1':"",
##                      'language_2':"",
##                      'language_proficiency_2':"",
##                      'language_3':"",
##                      'language_proficiency_3':"",
                        'languages':"Languages",
                        'phone_1':"Phone",
                        'phone_type_1':"Phone Type",
##                      'phone_2':"",
##                      'phone_type_2':"",
##                      'mutual_first_fullname':"",
##                      'mutual_second_fullname':""
                        'address': 'location',
                        'City': 'Billing City', 
                        'State': 'Billing State/Province'
                            }, inplace=True
                        )
