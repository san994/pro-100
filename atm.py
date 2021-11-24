class ATM():
    def __init__(self,cardNumber,pinNumber,balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance

    def CashWithdrawl(self):
        inp = int(input("enter the amout to be withdraw: "))
        if(self.balance>inp):
            self.balance  = self.balance-int(inp)
            print("you withdraw {} and remain {}".format(inp,self.balance))
        elif(self.balance<inp):
            print("you dont have required money")

        return True

    def CashAdd(self):
        inp = int(input('entter the amount to add: '))
        if(inp<1000):
            self.balance = self.balance+int(inp)
            print("you add {} and have in account {}".format(inp,self.balance))
        else:
            print("the added amount is much greater")

        return True
       

cardNumber = int(input('enter the cardNumber'))
pinNumber = int(input('enter the pinNumber'))
balance = int(input('enter the balance'))
ramAtm = ATM(cardNumber,pinNumber,balance)
completeTransection = False
while not completeTransection:
  inp = input("enter what you want(a/w)a=add w=withdraw: ")
  if(inp == "a"):
      transectiondetail = ramAtm.CashAdd()
  elif(inp == 'w'):
      transectiondetail = ramAtm.CashWithdrawl()
  
  if(transectiondetail == True):
      inp = input("do you want to leave(y/n): ")
      if(inp == "y"):
          completeTransection=True
      if(inp == "n"):
          completeTransection=False

if(completeTransection):
    print("bye thanks for using our services")
