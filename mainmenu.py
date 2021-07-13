from customer import Customer 
from file_parser import FileParser
from utils import Utils
from customermenu import Customermenu
class Mainmenu():

    Utils.clear_screen()

    def display_main_menu(self, ds):
        print("       BANK ACCOUNT MANAGEMENT SYSTEM    ")
        print("       ------------------------------")
        selection = "0"
        while(selection != "3"):
            #Utils.clear_screen()
            selection = self.show_user_menu(ds)
            if(selection not in ["1", "2", "3"]):
                #Utils.clear_screen()
                print(f"Invalid menu option [{selection}]. Press return to try again.")
                input()
    
    def show_user_menu(self, ds):
        print("")
        print("1. Existing Customers")
        print("2. New Customer Registration")
        print("3. Exit\n")
        selection = input("Please choose an option (1-3): ")
        if(selection == "1"):
            customer_menu=Customermenu()
            customer_menu.Display_customer_menu(ds)
        elif(selection == "2"):
            self.add_customer(ds)
            Utils.clear_screen()
            self.display_main_menu(ds)
        elif(selection=="3"):
            file_parser = FileParser()
            file_parser.write_customers("custs.txt", ds.customers)
            print("Thank you for using the system")
            print("Application exiting....")
            exit()
        return selection

############ new registration############

    def add_customer(self, ds):
        Utils.clear_screen()
        print("Add a new Customer")
        print("==================\n")
        # first name validation
        while True: 
            try:
                forename = str(input("First Name  : "))
                if (len(forename) > 0 and forename.isalpha()):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid entry.. Enter a valid first name.")
                continue 
            
        #surname validation
        while True: 
            try:
                surname = str(input("Second Name  : "))
                if (len(surname) > 0 and surname.isalpha()):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid entry..Enter a valid second name")
                continue 
        # pps number validation 
        while True: 
            try:
                ppsnumber = str(input("PPS Number: "))
                if (len(ppsnumber) == 7):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid entry..PPS number needs 7 characters.")
                continue 
        ## account type validation

        while True: 
            try:
                type = str(input("AccountType CURRENT/DEPOSIT[C/D] :"))
                type=type.upper()
                if (type=="C" or type=="D" ):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid entry...Enter C/D")
                continue 
    
        if (type.upper()=="C"):
            type="CURRENT"
            balance=25.0
        elif(type.upper()=="D"):
            type="DEPOSIT"
            balance=50.0
        ### overdraft validation###
        while True: 
            try:
                od = str(input("Overdraft Facility [Y/N]    : "))
                od=od.upper()
                if (od=="Y" or od=="N" ):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Invalid entry...Enter Y/N")
                continue 
        if (od.upper()=="Y"):
            od="YES"
        elif(od.upper()=="N"):
            od="NO"

        accountno=len(ds.customers)+100 #account number automatically created#
        interest=2.0
        customer = Customer(forename, surname, ppsnumber, type, od,accountno, balance,interest)
        ds.add_customer(customer)
        print("")
        print("Registration completed.")
        input("Return to continue...")
        


        

    