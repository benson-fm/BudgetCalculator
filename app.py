import datetime

current_time = datetime.datetime.now()
format_time = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
global userInput

class budget:
    
    budgets = []
    def __init__(self, curTotal = 0, name = ""):
        self.curTotal = curTotal
        self.history = []
        self.name = name
        budget.budgets.append(self)

    def getAmt(self):
        return self.curTotal
    
    def getName(self):
        return self.name

    def withDraw(self, amount):
        self.curTotal -= amount
        self.history.append((format_time + ": -" + str(amount)))

    def deposit(self, amount):
        self.curTotal += amount
        self.history.append((format_time + ": +" + str(amount)))

    def showHistory(self):
        print("--- History ---\n")
        for i in range(len(self.history)):
            print(self.history[i])

    def totalMoneyInvested():
        total = 0
        for i in range(len(budget.budgets)):
            total += budget.budgets[i].getAmt()
        return total

    def percent(self):
        curTotals = 0.0 
        for i in range(len(budget.budgets)):
            curTotals += budget.budgets[i].getAmt()
        return str(int((self.curTotal/curTotals) * 100))

    def transfer(self, budgetNum, amount):
        budget.budgets[budgetNum].withDraw(amount)
        self.deposit(amount)

    def printBudgets():
        print("\n--- Budgets ---\n")
        for i in range(len(budget.budgets)):
            print(str(i + 1) + ". " + budget.budgets[i].getName() + " - $" + str(budget.budgets[i].getAmt())+ "\n")

def validValue():
    while True:
        try:
            amt = int(input("Amount: "))
            break
        except ValueError:
            print("Invalid Input")
            pass 
    return amt          

while True:

    print("--- Menu ---\n")
    while True:
        try:
            userInput = int(input("1.Make a New Budget\n2.Deposit Into a Existing Budget\n3.Withdraw from an Existing Budget\n4.Total Investments\n5.Current Percent Distribution in Budgets\n6.Budget History\n7.Transfer Funds\n8.Quit\n\nInput number: "))
            break
        except ValueError:
            print("Invalid Input\n")
            pass
    
    if(userInput == 1):
        print("\n--- New Budget ---")
        name = input("What would you like to name it?: ")
        amt = validValue()
        budget(amt,name)
        print("You made a new budget called " + budget.budgets[len(budget.budgets) - 1].getName() + " with a deposit of " + str(amt) + "\n")

    elif(userInput == 2):
        print("\n--- Deposit ---")
        if(len(budget.budgets) > 0):
            budget.printBudgets()
            choice = int(input("Budget Num: "))
            amt = validValue()
            budget.budgets[choice - 1].deposit(amt)
            print("Transaction Complete\n")
        else:
            print("Invalid Amount of Budgets\n")

    elif(userInput == 3):
        print("\n--- Withdraw ---")
        if(len(budget.budgets) > 0):
            budget.printBudgets()
            choice = int(input("Budget Num: "))
            amt = validValue()
            if budget.budgets[choice - 1].getAmt() >= amt:
                budget.budgets[choice - 1].withDraw(amt)
                print("Transcation Complete\n")
            else:
                print("Cannot take more than current value\n")
        else:
            print("Invalid Amount of Budgets\n")

    elif(userInput == 4):
        print("\n--- Total Investments ---")
        if(len(budget.budgets) > 0):
            print("Total Money Invested: " + str(budget.totalMoneyInvested()))
        else:
            print("Invalid Amount of Budgets")

    elif(userInput == 5):
        print("\n-- Current Distributions ---")
        if(len(budget.budgets) > 0):
            print("Total Money Invested: " + str(budget.totalMoneyInvested()))
            for i in range(len(budget.budgets)):
                print(str(i + 1) + ". " + budget.budgets[i].getName() + " - " + str(budget.budgets[i].getAmt()) + "\n" + "Percentage: " + str(budget.budgets[i].percent()) + "%\n")
        else:
            print("Invalid Amount of Budgets")

    elif(userInput == 6):
        print("\n--- Budget History ---")
        if(len(budget.budgets) > 0):
            budget.printBudgets()
            choice = int(input("Which budget would you like to view the history of?: "))
            budget.budgets[choice - 1].showHistory()
        else:
            print("Invalid Amount of Budgets")

    elif(userInput == 7):
        print("\n--- Transfer Funds ---")
        if(len(budget.budgets) > 1):
            budget.printBudgets()
            budget1 = int(input("Withdrawn Budget Num: "))
            amt = int(input("Amount: "))
            addBudget = int(input("Deposit Budget Num: "))
            if budget.budgets[budget1 - 1].getAmt() >= amt:
                budget.budgets[addBudget - 1].transfer(budget1 - 1, amt)
            else:
                print("Cannot take more than current value\n")
        else:
            print("Invalid Amount of Budgets")

    elif(userInput == 8):
        break

    else:
        print("Invalid Input")
     

print("Thank you for working with Budget Calculator!")