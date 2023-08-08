#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:59:13 2022

Algorithm
Main:
    Initializes variables to certain values
    References open_file function to recieve input of file name to be opened
    Opens file using filepointer
    Skips two lines for table headers
    Reads each line in a for loop:
        Sets variables to values from data file
        Sets the max and min based off of values
        Adds to total and adds to count, calculates average
        References best_surf to change to best values if the current values are better
        Outputs all the data in correct format
"""

def open_file():
    '''
    Initializes file_year to input
    While loop that continues until a file is able to be read:
        adds the file_year to the file name
        tries to open the file and return the file name if it does
        if error, error statement and prompts for another file name
    '''
    file_year = input("Input a year: ")#prompts for input of year
    n=0#used to exit while loop 
    while n == 0:  
        file_name = 'wave_data_'+file_year+'.txt'#creates full file name by adding the year
        #tries to open the file, if it is able to, returns the file name and exits loop
        try :
            fp = open(file_name,'r')
            return file_name
            n=1#used to exit loop once try statement worls
        #if unable to open file, prints error statement and prompts for another year
        except FileNotFoundError :
            print("File does not exist. Please try again.")
            file_year = input("Input a year: ")
def get_month_str(mm):
    '''
    Sets an number string to an abbreviation of a month
    mm : the two digit number string  
    returns: Three digit form of month based off of mm
    '''
    #returns month based off of two digit number string parameter
    if mm == '01':
        return 'Jan'
    elif mm =='02':
        return 'Feb'
    elif mm =='03':
        return 'Mar'
    elif mm =='04':
        return 'Apr'
    elif mm =='05':
        return 'May'
    elif mm =='06':
        return 'Jun'
    elif mm =='07':
        return 'Jul'
    elif mm =='08':
        return 'Aug'
    elif mm =='09':
        return 'Sep'
    elif mm =='10':
        return 'Oct'
    elif mm =='11':
        return 'Nov'
    elif mm =='12':
        return 'Dec'
def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    '''
    Takes in parameters of current values and current best values
    Returns current values or best values depending on which are better, as long as current values are in between 6am and 7pm
    '''
    #returns best values if current hr is not between 6am and 7pm
    if not 6 < hr < 19:
        return best_mm , best_dd, best_hr, best_wvht, best_dpd
    #returns current values if current wvht is greater than best
    elif wvht > best_wvht:
        return mm , dd , hr, wvht, dpd
    #returns best values if best wvht is greater than current
    elif wvht < best_wvht:
        return best_mm , best_dd, best_hr, best_wvht, best_dpd
    #returns current values if current dpd is greater than best
    #returns best values if best dpd is greater than current
    elif wvht == best_wvht :
        if dpd > best_dpd:
            return mm , dd , hr, wvht, dpd
        elif best_dpd > dpd:
            return best_mm , best_dd, best_hr, best_wvht, best_dpd

def main(): 
    '''
    Uses the functions to read through the file and output the desired data
    '''
    print("Wave Data")#opening statement
    #initializes all values
    best_mm , best_dd = '1','1'
    best_hr, best_wvht, best_dpd = 1, 0.1, 0.1
    max_wvht, min_wvht, total_wvht, count = 0.1, 10**6, 0.0, 0
    wvht, dpd = 0.1,0.1
   
    file_name = open_file()#references function to get filename
    fp = open(file_name,'r')#opens file based on filename
   #skips two lines
    fp.readline()
    fp.readline()
    #for loop reads through each line of file and sets values from file
    for line in fp:
        mm = line[5:7]
        dd = line[8:10]
        try:
            hr = int(line[11:13])
        except ValueError:
            continue
        wvht =line[30:36] 
        dpd = line[37:42]
        #if wvht or dpd is equal to null values then continues through loop
        if line[30:36] == '99.00':
            continue    
        if line[37:42] == '99.00':
           continue
       #converts wvht and dpd to float
        wvht = float(wvht)
        dpd = float(dpd)
        #sets max and min wvht if greater than or less than current max/min
        if wvht > max_wvht:
            max_wvht = wvht
        if wvht < min_wvht:
            min_wvht = wvht
        total_wvht+= wvht#adds wvht to total 
        count+=1#adds 1 to count
        avg_wvht = total_wvht / count #calculates average by dividing total by count
        #sets best values by referencing the best_surf function
        best_mm, best_dd, best_hr, best_wvht, best_dpd = best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd)
    #prints all of data in correct format
    print("\nWave Height in meters.")
    print("{:7s}: {:4.2f} m".format('average',avg_wvht))
    print("{:7s}: {:4.2f} m".format('max',max_wvht))
    print("{:7s}: {:4.2f} m".format('min',min_wvht))
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(get_month_str(best_mm),best_dd,best_hr,best_wvht,best_dpd))#uses getmonth to convert number form of month to 3-letter month
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()