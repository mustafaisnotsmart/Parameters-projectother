def main():
    theprice = int(input("How much does the cake cost?\n"))
    def cakemath(numberofcakes, price):
        moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney = int(numberofcakes) * int(price)
        print(f"Your total cost for {numberofcakes} amount of cakes is {moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney}$")
    otherinput = input("how many cakes do you want?\n")
    cakemath(otherinput, theprice)
    

while True:      
    theinput = input("do you want to start the game?\n").lower()

    if theinput == "yes":
        main()
    else:
        print("bye")
