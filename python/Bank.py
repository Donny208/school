class Customer(object):
    def __init__(self,name, balance=0.0, cbalance=0.0):
        self.name = name
        self.balance = 0
        self.cbalance = 0
        
    def deposit(self,amount):
        self.balance += amount
        print(self.name,'Balance Is:',self.balance,'After You Deposited',amount)
        
    def withdrawl(self,amount):
        if amount > self.balance:
            print('You Do Not Have Enough Money In The Bank... Try Again')
        else:
            self.balance -= withh
            print('Your Balance Is:',self.balance)
    
    def getBalance(self):
        print('Your Balance Is:',self.balance)
        
    def setBalance(self,amount):
        self.balance = amount
        print(self.name,'Balance Is:',self.balance)
        
    def cdeposit(self,amount):
        self.cbalance += amount
        print(self.name,'Balance Is:',self.cbalance,'After You Deposited',amount)
            
    def cwithdrawl(self,amount):
        if amount > self.cbalance:
            print('You Do Not Have Enough Money In The Bank... Try Again')
        else:
            self.cbalance -= withh
            print('Your Balance Is:',self.cbalance)
    
    def cgetBalance(self):
        print('Your Balance Is:',self.cbalance)
        
    def csetBalance(self,amount):
        self.cbalance = amount
        print(self.name,'Balance Is:',self.cbalance)    

def startHere():
    print('Welcome To Don-Bank')
    Maggie = Customer('Maggie Lala')
    Maggie.setBalance(500.0)
    John = Customer('John Cena')
    John.setBalance(500.0)
    
    #While Loop
    loop = True
    while loop == True:
        loopTest = input('Make A Transation? (y or n)')
        if loopTest.lower() == 'y':
            custName = input('Select Maggie Or John> ')
            if custName.lower() == 'maggie':
                t = input('Would you like to (d)Deposit, (w)Withdraw, or (p)Print balance> ')
                if t.lower() == 'd':
                    amount = int(input('How much do you want to deposit?> '))
                    Maggie.deposit(amount)
                elif t.lower() == 'w':
                    amount = int(input('How much do you want to withdraw?> '))
                    Maggie.withdraw(amount)
                elif t.lower() == 'p':
                    Maggie.getBalance()
                else:
                    print('Try Again!')
            elif custName.lower() == 'john':
                t = input('Would you like to (d)Deposit, (w)Withdraw, or (p)Print balance> ')
                if t.lower() == 'd':
                    amount = int(input('How much do you want to deposit?> '))
                    John.deposit(amount)
                elif t.lower() == 'w':
                    amount = int(input('How much do you want to withdraw?> '))
                    John.withdraw(amount)
                elif t.lower() == 'p':
                    John.getBalance()
                else :
                    print('Try Agani!')
        elif loopTest.lower() == 'n':
            loop = False
        

if __name__ == '__main__':
    startHere()
    
