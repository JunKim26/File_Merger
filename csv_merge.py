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
