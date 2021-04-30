rupee5Coins, rupee1Coins, amountToBeMade = int(input("Enter the 5 rupee coins we have: ")), int(input("Enter the 1 rupee coins we have: ")), int(input("Enter the amount of change we have to give: "))

def changeCalculator(rupee5Coins, rupee1Coins, amountToBeMade):

    coinsOf5 = amountToBeMade // 5

    coinsOf1 = amountToBeMade % 5

    if(coinsOf1 <= rupee1Coins):

        print(f"Rs 1 coins needed {coinsOf1}     Rs 5 coins needed {coinsOf5}")

    else:

        print("-1")


changeCalculator(rupee5Coins, rupee1Coins, amountToBeMade)

    
