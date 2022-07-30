print("\n\nQuestion 8: Write a program that has 3 inputs – loan amount, duration in years and interest rate. The program displays the compound interest based on the formula above. ")
def q8():
    loanAmount=float(input("How much the money?"))
    years=int(input("How many years?"))
    interestRate=int(input("Lastly, interest rate?"))


    compundInterest=loanAmount*((1+(interestRate/100))**years)

    print(compundInterest)
q8()