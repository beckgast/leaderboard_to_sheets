import json
from calendar import monthrange
import pandas as pd
import datetime
import requests
import numpy as np
import csv
from bs4 import BeautifulSoup as soup 
from datetime import datetime
from dateutil import parser

from helper import get_assigned_date


def write_daily_scores_to_file(scores_array):
    lr = len(scores_array)-1
    last_month = int(scores_array[lr][1])
    last_day = int(scores_array[lr][2])
    first_month = int(scores_array[0][1])
    first_day = int(scores_array[0][2])
    month_increment = first_month
    num_days = monthrange(2022, month_increment)[1]
    day_increment = 1
    
    print(num_days)
    firstdate = (datetime(scores_array[0][0], scores_array[0][1], scores_array[0][2], scores_array[0][3], scores_array[0][4], 0).timetuple().tm_yday)   
    lastdate = (datetime(scores_array[lr][0], scores_array[lr][1], scores_array[lr][2], scores_array[lr][3], scores_array[lr][4], 0).timetuple().tm_yday)       
        
    x=0
    while x <= lr:
            thedate =  firstdate = (datetime(scores_array[x][0], scores_array[x][1], scores_array[x][2], scores_array[x][3], scores_array[x][4], 0).timetuple().tm_yday)       
            
            x = x + 1
        
        

def write_to_clean_output(arrayline):
    with open('cleanoutput.csv', 'a') as g:
        s = ", ".join(map(str, arrayline))
        g.write(s)
    g.close()

def create_array_from_file():
    array2D = []
    with open('output.csv', 'r') as f:
        for line in f.readlines():
            if len(line)>1:
                dateandtime, name, score = (str(x) for x in line.split(','))
                if len(score)>1:
                    thisdate, thistime = (str(x) for x in dateandtime.split(' '))
                    year, month, day = (int(x) for x in thisdate.split('-'))
                    hour = int(thistime[:2])
                    minute = int(thistime[3:5])
                    date = parser.parse(dateandtime)
                    day, month = get_assigned_date(date)
                    arrayline = [year, month, day, hour, minute, name, score]
                    array2D.append(arrayline)            
    f.close()
    return array2D
        
#boom
if __name__ == '__main__':
    scores_array = create_array_from_file()
    write_daily_scores_to_file(scores_array)