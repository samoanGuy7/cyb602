#William Laolagi
#Assignment: Python Week 3, try/catch and loops
#This program will get hours and rate as input from the user and calculate gross pay using python functions.
import sys

#Singleton for ease of use
class HighLow:
    def __init__(self):
        self.high = 0
        self.low = 0
        
#Helper functions        
def getInt(temp,values):
    while temp != "Done":
        try:
            temp = str(input("Enter an integer: "))
            if(temp == "Done"):
                break
            if(temp != "Done"):
                values.low = getLow(int(temp),values.low)
                values.high = getHigh(int(temp),values.high)
        except:
            print("Error: Please enter a number")
            
def getLow(integer,low):
    if((integer > 0 and integer < low) or low == 0):
        low = integer
    return low

def getHigh(integer,high):
    if(integer > high):
        high = integer
    return high
    
def get_highLow():
    return HighLow()

#Main execution    
print( "Enter in a number: " )
integer = input()
if(integer == "Done"):
    print("No numbers were entered")
    exit(0)

integer = int(integer)
values = get_highLow()
values.high = integer
values.low = integer
getInt(integer,values)

print("Low: " + str(values.low) + " High: " + str(values.high))