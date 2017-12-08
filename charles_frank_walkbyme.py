#!/usr/bin/python
#Charles V. Frank Jr.
#Inspiration; https://www.johannesbader.ch/2016/06/the-dga-of-sisron/
#I am going to modify the Sisron DGA to satisfy the requirements:
#Accepted TLDs: .csc840.lan, .com, .press, .me, .cc	
#Length: 9-15	
#Alphabet: No vowels, numbers ok	
#Non-deterministic
#Laymans Description:
#(1) calculate a date minus certain number of days (day_index)
#(2) generate a string from that date based upon the:
#       %A - Weekday full name
#       %j - Day of the year as a decimal number
#       %d - Numeric representation of day of the month
#       %m - Numeric representation of the month
#       %Y - Year with century
#(3) b54encode the string, replacing the vowles and =
#       This string should be longer than 15 chars
#(4) calculate the length of the domain
#       The length will be between 9 and 15
#(5) return the doman[domain_length] + tld
#The Seed:
#   day_index 


from datetime import datetime, timedelta
import base64

import datetime as dt
import pandas as pd
import pandas_datareader.data as web


#dga algorithm
# d - date
# day_index - index to the day number
# tld-index - index to tlds

def dga(d, day_index, tld_index):

    #defined tlgs
    tlds = [".csc840.lan", ".com", ".press", ".me", ".cc"]

    #get the volume of trades for the TSLA stock for the date
    df = web.DataReader("TSLA", "yahoo", d)
    seed = df.iloc[0]['Volume']

    #go back in the date based upon day_index
    d -= timedelta(days=(day_index))

    #generate date string
    ds = d.strftime("%A%j%d%m%Y")

    #calculate the digit to replace with
    the_char = str(unichr((day_index % 25) + 97))
    
    #substitute for vowels and = 
    ds = base64.b64encode(ds).lower().replace("=",the_char)
    ds = ds.replace("a",the_char)
    ds = ds.replace("e",the_char)
    ds = ds.replace("i",the_char)
    ds = ds.replace("o",the_char)
    ds = ds.replace("u",the_char)
    ds = ds.replace("y",the_char)

    #calculate the length for the domain(ds)
    #based upon the day_index
    ds_len = (day_index % 7) + 9
    
    return ds[0:ds_len] + tlds[tld_index]

#main routine
if __name__=="__main__":
    
    #get the current date and time now
    d = datetime.now()

    #execute 10 DGA 
    for i in range(10):
        print(dga(d, i%32, i%5))



 
