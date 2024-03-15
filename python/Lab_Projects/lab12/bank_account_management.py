#Author: Josh Hodges
#Date:30NOV23
"""statement of problem: Create a bank account management program
that includes bank account class with acct#, acct holder, and balance
will include methods deposit, withdrawl, balance, and display info
will also include a user interaction loop that will allow user to edit or display appropriate info"""
#statement of authenticity:I worked on this alone. 
#layman problem/solution:

class BankAccount:
    def __init__(self, accountnum, accountholder, balance):
        self.bal=float(balance)
        self.actnum=accountnum
        self.acthold=accountholder

    def deposit(self, depamt):
        self.bal+=float(depamt)

    def withdrawl(self, drawlamt):
        self.bal-=drawlamt

    def getbal(self):
        return int(self.bal)
    
    def __str__(self):
        return "Account number: "+self.actnum+" Account holder: "+self.acthold+" Balance: "+str(self.bal)
    
    def getName(self):
        return self.acthold
    
    def getNum(self):
        return self.actnum



def main():
    accounts=[]
    #allows user to remain in menu
    open=True
    while True:

        print('1)Create Account\n')
        print("2)Deposit money into an account\n")
        print('3)Withdrawl money from an account\n')
        print('4)Check Balance of an account\n')
        print('5)Quit')

        choice=input('What would you like to do?\n Please enter the number of your choice: ')
        #create new account object
        if choice=="1":
            name=input('What is the name of the account holder?: ')
            acntnumber=input('What is the account number?: ')
            bal=input('What is the current balance of the account')
            newact=BankAccount(acntnumber,name,bal)
            accounts.append(newact)
            print("Your new account has been created.")

        #deposit
        elif choice=="2":
            id=input('What is the name on or the account number of the account you wish to deposit to?: ')
            amount=input('How much do you wish to deposit?: ')
            for i in accounts:
                if id==i.getName() or id==i.getNum():
                    i.deposit(amount)
                    print('Your new balance is,',i.getbal())
                    break
                   
        #Withdrawl
        elif choice=="3":
            id=input('What is the name on or the account number of the account you wish to withdrawl from?: ')
            amount=float(input('How much do you wish to withdrawl?: '))
            for i in accounts:
                if id==i.getName() or id==i.getNum():
                    if amount > i.getbal():
                        print("Insufficient Funds!")

                    else:
                        i.withdrawl(amount)
                        print("Your new balance is,",i.getbal())
                        break



        #Check balance
        elif choice=="4":
            id=input('What is the name on or the account number of the account you wish to see?:')
            for i in accounts:
                if id==i.getName() or id==i.getNum():
                    #statement=i.__str__()
                    print(i)
            

        #Quit
        elif choice=="5":
            break
        
        #invalid entry
        else:
            print('That is not a valid entry.\n please enter the menu number of what you wish to do.')


main()