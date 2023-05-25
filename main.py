print("Welcome to the tip calculator!")
cost= float(input("What was the total bill? $"))
tipinput=int(input("How much tip would you like to give? 10, 12, or 15? "))
tip = (tipinput/100) * cost
split = int(input("How many people to split the bill?"))


#fomratting so that the calculation always returns two decimal points 
finalamount = "{:.2f}".format(round(((cost+tip)/split),2))
print("Each person should pay: $"+ finalamount)

