print("\n\nQuestion 5: Write  a  program  that  reads  an  input  representing  a  change  which  is  an amount less than 1 dollar.  The program calculates the change into 50, 10, 5 and  1  cent  coins.  The  program  then  displays  the  number  of  each  coin required for that change.")

def q5():
    change=int(input("\nInput a change below 100: "))
    #unnecessary print. Lab has no grading marks so yeah
    print("\nTrivia: You can go to toilet",(change//20),"times at Fortune Center (20 Cents) or",(change//10),"times at Tanjong Pagar Hawker Center (10 Cents). Yes.. Its 2022...\n")
    fiftyCent=change//50
    change=change-(fiftyCent*50)
    tenCent=change//10
    change=change-(tenCent*10)
    fiveCent=change//5
    oneCent=change-(fiveCent*5)

    


    #TEST PRINT DURING DEV, SHOULD BE COMMENTED OUT AFTER PRODUCTION
    print("\n Your Change List:\n50 Cent:",fiftyCent,"\n10 Cent:",tenCent,"\n5 Cent:",fiveCent,"\n1 Cent:",oneCent)

q5()
