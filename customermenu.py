from utils import Utils
from file_parser import FileParser
class Customermenu:

   def Display_customer_menu(self,datastore):
        Utils.clear_screen()
        print("     CUSTOMER MENU ")
        print("     --------------")
        print(" 1. List all accounts")
        print(" 2. View account information")
        print(" 3. Cash Withdrawal")
        print(" 4. Cash Deposit")
        print(" 5. Transfer funds")
        print(" 6. Main menu")
        choice=input("Enter your choice :  ")
        if(choice=="1"):
            self.view_customers(datastore)
            self.Display_customer_menu(datastore)
        elif(choice=="2"):
            self.view_accountinfo(datastore)
            Utils.clear_screen()
            self.Display_customer_menu(datastore)
        elif(choice=="3"):
            self.cash_withdrawal(datastore)
            Utils.clear_screen()
            self.Display_customer_menu(datastore)
        elif(choice=="4"):
           self.cash_deposit(datastore)
           Utils.clear_screen()
           self.Display_customer_menu(datastore)
        elif(choice=="5"):
            self.fund_transfer(datastore)
            Utils.clear_screen
            self.Display_customer_menu(datastore)
        elif(choice=="6"):
            #mainmenu=Mainmenu()
            #mainmenu.show_user_menu(datastore)
            file_parser = FileParser()
            file_parser.write_customers("custs.txt", datastore.customers)
            print("Thankyou for using the system")
            print("Application exiting.......")
            exit()
        else:
            input("Invalid Entry ...Return to continue..")
            Utils.clear_screen()
            self.Display_customer_menu(datastore)

############ view all customer information####################

   def view_customers(self, ds):
        Utils.clear_screen()
        print("")
        print("           CUSTOMER ACCOUNT INFORMATION")
        print("")
        print("   Customer Name      PPSNo     Accouttype    Overdraft  Accountno    Balance    Interest(%)")
        print("===========================================================================================")

        for customer in ds.customers:
            print(customer)
        print("=======================================================================================")

        input("Please enter to continue....")

################## view cutomer information using pps number   ################

   def view_accountinfo(self,ds):
      Utils.clear_screen()
      found=False
      print("")
      print("    CUSTOMER ACCOUNT INFO  ")
      print("    ----------------------")
      ppsn=input("Enter custoner PPS number  :  ")
      print("")
      print("   Customer Name      PPSNo     Accouttype    Overdraft  Accountno    Balance    Interest(%)")
      print("===========================================================================================")
      for customer in ds.customers:
          if (ppsn==customer.ppsnumber):
              found=True
              print(customer)
      print("============================================================================================")
      if(found==False):
          print("")
          print("Incorrect PPS Number....")
      input("Return to continue.......")

########################## cash withdrawal###############


   def cash_withdrawal(self,ds):
        Utils.clear_screen()
        print("")
        print("    CASH WITHDRAWAL ")
        print("    ---------------")
        found=False
        accno = False
        while accno == False:
          try:
              accno = int(input("Enter customer account number :  "))
          except:
               print("Invalid entry...Account number should be a numeric value")
        for customer in ds.customers:
            if(accno==customer.accountnumber):
                print(" Account Name       : ", customer.forename)
                print(" Account Type       : ",customer.accounttype)
                print(" Current Balance    : ",customer.balance)
                print(" Overdraft facility :",customer.overdraft)
                print("")
                found=True
                withdraw_amount= False
                while withdraw_amount == False:
                   try:
                       withdraw_amount = float(input("Enter the amount to be withdrawan : "))
                   except:
                        print("Invalid entry. Please enter a numeric value...")
                if ((withdraw_amount>customer.balance) and (customer.overdraft=="NO")):
                    print("Insufficient funds..Transaction unsuccessful..")
                    input("Return to continue...")
                    break
                elif ((withdraw_amount>customer.balance) and (customer.overdraft=="YES")):
                    customer.balance=customer.balance-withdraw_amount
                    print("Transaction Successful")
                    input("Return to continue....")
                    break
                elif (withdraw_amount<customer.balance):
                    customer.balance=customer.balance-withdraw_amount
                    if (customer.balance>10000):
                        customer.interest=5.0
                    else:
                        customer.interest=2.0
                    print("Transaction Successful")
                    print("Current balance is : ",customer.balance)
                    input("Return to continue....")
                    break
        if(found==False):
            print(" Account number doesnot exist...")
            input(" Return to continue")
            


 
 ################cash deposit####################################

   def cash_deposit(self,ds):
        Utils.clear_screen()
        print("")
        print("    CASH DEPOSIT ")
        print("    ---------------")
        found=False
        accno = False
        while accno == False:
          try:
              accno = int(input("Enter customer account number :  "))
          except:
               print("Invalid entry...Account number should be a numeric value")
        for customer in ds.customers:
            if(accno==customer.accountnumber):
                print(" Account Name       : ", customer.forename)
                print(" Account Type       : ",customer.accounttype)
                print(" Balance    : ",customer.balance)
                print(" Overdraft facility :",customer.overdraft)
                print("")
                found=True
                deposit_amount= False
                while deposit_amount == False:
                   try:
                       deposit_amount = float(input("Enter the amount to be deposited : "))
                   except:
                        print("Invalid entry. Please enter a numeric value...")
                customer.balance=customer.balance+deposit_amount
                if (customer.balance>10000):
                    customer.interest=5.0
                else:
                    customer.interest=2.0
                print("")
                print("Current Balance is  :  ",customer.balance)
                input("Transaction successful...Return to continue")
                break
        if(found==False):
            print("Account number doesnot exists....") 
            input("Return to continue.....")   




####################### transfer funds####################################

   def fund_transfer(self,ds):
        Utils.clear_screen()
        print("")
        print("    FUND TRANSFER ")
        print("    ---------------")
        found=False
        accno1 = False
        while accno1 == False:
          try:
              accno1 = int(input("Enter FROM account number :  "))
          except:
               print("Invalid entry...FROM Account number should be a numeric value")
        accno2 = False
        while accno2 == False:
          try:
              accno2 = int(input("Enter TO account number :  "))
          except:
               print("Invalid entry...TO Account number should be a numeric value")
            
        for customer in ds.customers:
            if(accno1==customer.accountnumber):
                for customer1 in ds.customers:
                    if(accno2==customer1.accountnumber):
                         found=True
                         print("")
                         print("FROM account details:")
                         print("---------------------")
                         print(" Account Name  : ", customer.forename,"  Current Balance  :",customer.balance,"  Overdraft  :",customer.overdraft)
                         print("")
                         print(" TO account details:")
                         print("-------------------")
                         print(" Account Name  : ", customer1.forename,"  Current Balance : ",customer1.balance,"  Overdraft  :",customer1.overdraft)
                         print("")
                         transfer_amount = False
                         while transfer_amount == False:
                            try:
                                transfer_amount = float(input("Enter amount to be transfered :  "))
                            except:
                                print("Invalid entry...Amount should be a numeric value")
                         if ((transfer_amount>customer.balance) and (customer.overdraft=="NO")):
                              print("Insufficient funds..Fund transfer unsuccessful..")
                              input("Return to continue...")
                              break
                         elif ((transfer_amount>customer.balance) and (customer.overdraft=="YES")):
                              customer.balance=customer.balance-transfer_amount
                              customer1.balance=customer1.balance+transfer_amount
                              if (customer1.balance>10000):
                                   customer1.interest=5.0
                              else:
                                   customer1.interest=2.0
                              print("Transaction successful...")
                              print("")
                              print("FROM account current balance  :", customer.balance) 
                              print("TO account current balance  :", customer1.balance)
                              input("Return to continue.....")
                              break
                         elif (transfer_amount<customer.balance):
                              customer.balance=customer.balance-transfer_amount
                              if (customer.balance>10000):
                                   customer.interest=5.0
                              else:
                                   customer.interest=2.0                    
                              customer1.balance=customer1.balance+transfer_amount
                              if (customer1.balance>10000):
                                   customer1.interest=5.0
                              else:
                                   customer1.interest=2.0
                              print("")
                              print("Transaction successful...")
                              print("FROM account current balance  :", customer.balance)
                              print("TO account current balance  :", customer1.balance)
                              input("Return to continue.....")
                              break
        if(found==False) :
               print(" Account number doesnot exist...")
               input("Return to continue.....")