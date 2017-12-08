#!/usr/bin/python
#Charles V. Frank Jr.
#This script converst the C code for the Ranbyus DGA
#Source: https://www.johannesbader.ch/2015/05/the-dga-of-ranbyus/
#DGA Algorithm Description:
#(1) initialize a list of domains
#(2) set the tld_index to the day
#(3) define a loop for the number of domains to be generated
#(4)    initia;ize the domain (domain name)
#(6)    define a loop for 14 iterations (size of domain)
#(7)        perform the calculations:
#               day, year, month, seed
#(8)        calculate the character to add to the domain 
#(9)        add the character to the domain (14 characters added)
#(10)   print the domain along with the tld from [tld_index % 8]
#(11)   increment the tld index
#DGA Parameters:
#   day - numberic representation of the day (dd)
#   month - numeric representation of the month (m)
#   year - numeric representation of the year (YYYY)
#   seed - ul long of hex base 16
#   nr - number of domain names to generate

import sys


#dga algorithm

def dga(day, month, year, seed, nr):
    
    #list of tld
    tlds = ["in", "me", "cc", "su", "tw", "net", "com", "pw", "org"]
    
    #set tld_index
    tld_index = int(day)

    #for loop for number of runs
    for d in range (nr):

        #initialize domain string
        domain = ""

        #for loop to calculate a domain
        for i in range (14):
            #Calculations
            #day 
            day = (day >> 15) ^ 16 * (day & 0x1FFF ^ 4 * (seed ^ day))
            #year 
            year = ((year & 0xFFFFFFF0) << 17) ^ ((year ^ (7 * year)) >> 11)
            #month 
            month = 14 * (month & 0xFFFFFFFE) ^ ((month ^ (4 * month)) >> 8)
            #seed 
            seed = (seed >> 6) ^ ((day + 8 * seed) << 8) & 0x3FFFF00
            #domain char
            x = ((day ^ month ^ year) % 25) + 97
            #assign into the the domain string
            domain = domain + chr(x) 
            
        #print the domain with the tld   
        print str(domain) + "." + str(tlds[tld_index % 8])
        
        #increment tld_index
        tld_index = tld_index + 1
  
#main
if __name__ == "__main__":
    
    #get number of arguments
    argc = len(sys.argv)

    #check for 5 arguments
#    if(argc != 5): 
#        printf("Usage: dga <day> <month> <year> <seed>\n")
#        printf("Example: dga 14 5 2015 b6354bc3\n") 
#        exit(0);
    
    #call dga algorithm
#    dga(atoi(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
#        long(str(sys.argv[4]), 16), 10)


    dga(14, 5, 2015, long(str("b6354bc3"), 16), 10)

 
