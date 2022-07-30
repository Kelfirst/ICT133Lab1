print("\n\nQuestion 4: Write a program that reads in a positive integer representing time in seconds and converts it to hour, minute and seconds. For example, if the input is 3670 seconds, output 1 hour, 1 minute and 10 seconds. ")
def q4():
    inputTime=int(input("How many seconds ah?: "))
    theHour=inputTime//3600 #calculating the hours, since we dont need the float number we integer divide.
    inputTime=inputTime%3600 #calculating remainding seconds after hours.
    theMinute=inputTime//60 #calculating the minutes, as usual, we just integer divide.
    theSecond=inputTime%60 #since we dont need inputTime anymore, there is no need to update this variable

    print(theHour,"Hours",theMinute,"Minutes", theSecond,"Seconds") 
    #finalproduction.

q4()
