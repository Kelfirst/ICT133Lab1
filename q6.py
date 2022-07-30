print("\n\nQuestion 6 : A  restaurant  is  offering  meals  at  50%  discount.  A  service  charge  (10%)  and GST  (7%)  apply  to  the  discounted  cost.  While  the  service  charge  applies  to the discounted price, note that the GST calculation is based on the total of the discounted amount and the service charge.  ")

def q6():
    mealAmount=int(input("Enter Meal Amount"))
    discount50=mealAmount*0.5
    serviceCharge=discount50*0.1
    gst=(discount50+serviceCharge)*0.07
    totalAmount=discount50+serviceCharge+gst

    print("~~~~~~Receipt~~~~~")
    print("Cost of Meal:  ",mealAmount,"\n50% Discount:  ",discount50,"\nService Charge:",serviceCharge,"\nGST:           ",gst,"\nTotal Amount   ",totalAmount)
    print("Thank you for your patronage! No more 50% next time!")

q6()