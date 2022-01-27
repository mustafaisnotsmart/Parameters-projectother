def main():
    def cakemath(numberofcakes, price                                            ):
        print("youre here")
        moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney = int(numberofcakes) * int(price)
        print(f"Your total cost for {numberofcakes} amount of cakes is {moneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoneymoney}")
    otherinput = input("how many cakes do you want?\n")
    cakemath(otherinput)
    

while True:      
    theinput = input("do you want to start the game?\n").lower()

    if theinput == "yes":
        main()
    else:
        print("bye")
