from turtle import hideturtle


def main():
    #this asks you how much the cake should cost to multiply it
    theprice = int(input("How much does the cake cost?\n"))
    # takes in the number of cakes and theprice    
    def cakemath(numberofcakes, price):
        # varaible that does the math $$$$$$$$$$ 🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑
        moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney = int(numberofcakes) * int(price)
        # total that uses the fstring python feature so i wouldn't have to format.. lazy 
        print(f"Your total cost for {numberofcakes} amount of cakes is {moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney}$")
    otherinput = input("how many cakes do you want?\n")
    # calls the function with the inputs
    cakemath(otherinput, theprice)
    
# this just makes sure it loops whenever they finish the thing
while True:      
    theinput = input("do you want to start\n").lower()
# if yes then call the function otherwise bye bye
    if theinput == "yes":
        main()
    else:
        print("bye")
