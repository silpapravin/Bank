from customer import Customer
class FileParser():
    
    # reading data from file and storing in alist

    def read_customers(self, filename): 
        customers = []
        try:
            fo = open(filename, "r")
            lines = fo.readlines()
            fo.close()
        except IOError:
            print(f"Warning : couldnot open file {filename} for reading")
            input("Return to continue....")
            return customers
        for line in lines:
            customer = self.parse_customer_text(line)
            customers.append(customer)
        
        return customers

     # parsing each customer records and storing in list#

    def parse_customer_text(self, cust_text):

        fields = cust_text.split("|")

        forename = fields[0]
        surname = fields[1]
        ppsnumber = fields[2]
        accounttype = fields[3]
        overdraft = fields[4]
        accountnumber = int(fields[5])
        balance= float(fields[6])
        interest = float(fields[7])

        return Customer(forename, surname, ppsnumber, accounttype, overdraft, accountnumber,balance,interest)

    #writing list data into file#
    
    def write_customers(self, filename, customers): 
                    
        lines = []
        first_customer = True
        for customer in customers:

            if first_customer == True:
                lines.append(customer.file_text())
                first_customer = False
            else:
                lines.append(f"\n{customer.file_text()}")

        try:
            fo = open(filename, "w") 
            fo.writelines(lines)
            fo.close()
        except IOError:
            print(f"Warning : couldnot open file {filename} for writing")
            input("Return to continue....")