print("\n\nQuestion 9: Write a program that reads in a time in 24 hr format. The program displays the time after adding 1 second to the time. ")
def main():
    #gather input
    computeHour=int(input("How many hours ah?: "))
    computeMinute=int(input("How many minutes ah?: "))
    computeSecond=int(input("Lastly how many seconds?: "))
    #combining inputs to seconds and add a second.
    inputTime=(computeHour*3600)+(computeMinute*60)+(computeSecond)+1
    #calculating hours, don't require float number we integer divide.
    theHour=inputTime//3600 
    #if the hours are below 24 it should return original value.
    theHour=(theHour+24)%24
    #calculating remainding seconds after hours.
    inputTime=inputTime%3600 
    #calculating the minutes, as usual, we just integer divide.
    theMinute=inputTime//60 
    theSecond=inputTime%60 
    #dont need inputTime, there is no need to update this variable

    #printing output, using zfill to fill up (zfill knowledge credited to stackoverflow.)
    print(str(theHour).zfill(2),":",str(theMinute).zfill(2),":", str(theSecond).zfill(2)) #finalproduction.
main()