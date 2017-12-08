#!/usr/bin/python
#Charles V. Frank Jr.
#I am going to modify the Sisron DGA to satisfy the requirements:
#Accepted TLDs: .csc840.lan, .com, .press, .me, .cc	
#Length: 9-15	
#Alphabet: No vowels, numbers ok	
#Non-deterministic
#Laymans Description:
#(1) calculate the volume to trades for tesla from yahoo as a global variable
#    initialize the tld_index as a global variable
#(2) initiate a loop to generate 20 characters
#       seed used for random1 calculation
#       Calculate random2, random3
#       Now, shift bits to change the seed value
#       calculate the character based upon random values
#       assign the character to the domain
#(3) encode the domain (this will put digits into the domain)
#(4) substitue vowels in the domain
#(5) Calculate the length of the domain name
#(6) print domain + tld
#The Seed:
#   Volume of stocks traded for TESLA
#In Main:
#execute a for loop for 10 times
#   call dga algorithm 
#Other:
#   Pandas module is used for its dataframe
#   and its specialized datareader

#modules
import base64
import pandas as pd
import pandas_datareader.data as web


#global variables
tld_index = -1

#get the seed from the volume of TSLA
#get the current volume for TESLA
df = web.DataReader("TSLA", "yahoo")
seed = long(df.iloc[-1]['Volume'])

#dga algorithm
def dga():

    #defined tlgs
    tlds = [".csc840.lan", ".com", ".press", ".me", ".cc"]

    #initialize
    global seed
    ds = ""
    global tld_index
    tld_index = (tld_index + 1) % 5

    #for loop to calculate a domain
    for i in range (20):
        #Calculations
        #random1 
        random1 = (seed >> 5) ^ 16 * ( seed & 0x1FFF0000 ^ 4 * (seed ^ seed))
        #random2
        random2 = ((tld_index & 0xFFF00FF0) << 3) ^ ((random1 ^ (7 * random1)) >> 7)
        #random3 
        random3 = 14 * (random1 & random2 & 0x0FFFFFFE) ^ ((random2 ^ (4 * random1)) >> 8)
        #seed 
        seed = (seed >> 3) ^ ((random2 * seed) << 5) & 0x0FFFFab
        #domain char
        x = ((random1 ^ random2 ^ random3) % 25) + 97
        #assign into the the domain string
        ds = ds + chr(x)
    
    #hash and substitute for vowels and = 
    ds = base64.b64encode(str(ds)).lower().replace("=","w")
    ds = ds.replace("a","b")
    ds = ds.replace("e","f")
    ds = ds.replace("i","j")
    ds = ds.replace("o","p")
    ds = ds.replace("u","v")
    ds = ds.replace("y","z")

    #calculate the length for the domain(ds)
    ds_len = (seed % 7) + 9

    #output the domain + tld
    print(ds[0:ds_len] + tlds[tld_index])
    
    return 

#main routine
if __name__== "__main__":
    
    #execute 10 Domains
    for i in range(10):
        dga()



 
