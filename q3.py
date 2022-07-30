print("\n\nQuestion 3: Write  a  program  that  takes  in  a  3  digit  integer  and  displays  the  sum  and product of the digits. E.g. if the number is 123, the sum displayed is 6 and the product is also 6. ")
def q3():
    digit3=str(input("Input only 3 digits dont play punk: "))

    #strDigit3=str(digit3) # I made this string to integer line redundant. Saves one line.

    #finds the digit via string position, then convert back to int
    #EDIT, I made this line redundant. Yet again.
    #number1=int(digit3[0])
    #number2=int(digit3[1])
    #number3=int(digit3[2])

    #Refactored and eliminated so many variables
    #extracts individual digits position, converting back
    #to integer, does the calculations based on the variable
    totalSum=(int(digit3[0]))+(int(digit3[1]))+(int(digit3[2])) 
    totalProduct=(int(digit3[0]))*(int(digit3[1]))*(int(digit3[2]))

    print("Total Sum is:",totalSum,"Total Product is:",totalProduct)

    #print("TEST ONLY, REMEMBER TO ENABLE INPUT.",digit3,number1,number2,number3)

q3()