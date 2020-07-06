#!/usr/bin/env python3

#only left and right movement is allowed


def maneuring(cr,cc,tr,tc):  #cr=currentrow cc=currentcolumn tr=totalrows tc=totalcolumns
    if((cr >= tr) or (cc >= tc)):
        return 0
    if(cr == tr-1 and cc == tc-1):
        return 1
    total_ways = maneuring(cr,cc+1,tr,tc)+maneuring(cr+1,cc,tr,tc)   
    return total_ways 


if __name__ =="__main__":
    
    tr,tc = input("Enter the no.of rows and columns").split()
    tr =int(tr)
    tc =int(tc)
    print(maneuring(0,0,tr,tc))