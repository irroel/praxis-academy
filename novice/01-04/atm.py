class BalanceInquiry():
    balance = 0.0
    def setBalance(self, b):
        self.balance = b
    def getBalance(self):
        return self.balance

class Deposit():
    deposit = 0.0
    def setDeposit(self, d):
        self.deposit = d
    def getDeposit(self):
        return self.deposit

class Withdraw():
    withdraw = 0.0
    def setWithdraw(self, w):
        self.withdraw = w
    def getWithdraw(self, w):
        return self.withdraw

class ATMmachine(): 
    def main():
        def withDrawMoney():
            if bal.balance == 0.0:
                print('Your current balance is zero.')
                print('You cannot withdraw!.')
                print('You need to deposit money first.')
            elif bal.balance < 500:
                print('You do not have sufficient money to withdraw')
                print('Checked your balance to see your money in the bank.')
            elif wit.withdraw > bal.balance:

                print('The amount you withdraw is greater than to your balance')
                print('Please check the amount you entered')
            else:
                bal.balance = bal.balance - wit.withdraw
                print(f'You withdraw the amount of Php {wit.getWithdraw(3)}')
        def depositMoney():
            print(f'You deposited the amount of {depo.getDeposit()}')

        depo = Deposit()
        bal = BalanceInquiry()
        wit = Withdraw()
        flag = True
        
        while flag:
            print('Please select ATM Transactions')
            print("Press [1] Deposit")
            print('Press [2] Withdraw')
            print('Press [3] Balance Inquiry')
            print('Press [4] Exit')
            print('What would you like to do?')
            inp = int(input())
            if inp == 4:
                flag = False
                break
            elif inp == 1:
                print('Enter the ammount of money to deposit:')
                d = float(input())
                depo.setDeposit(d)
                bal.balance = bal.balance + depo.deposit
                depositMoney()
                print()
                print()
            elif inp == 2:
                print('To withdraw, make sure that you have sufficient balance account')
                print('Enter ammount of money to withdraw: ')
                w = float(input())
                wit.setWithdraw(w)
                withDrawMoney()                
                print()
                print()
            elif inp == 3:
                print(f'Your money in ATM is : {bal.getBalance()}')
                print()
                print()
            else:
                flag = False
                break
    if __name__ == "__main__":
        print('===================================================================')
        print(f'                  Welcome to this simple ATM Machine              ')
        print('===================================================================')
        main()
