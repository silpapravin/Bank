from customer import Customer
class FileParser():

    def read_customers(self, filename): # reading from file
       
        fo = open(filename, "r")
        lines = fo.readlines()
        fo.close()
        customers = []
        for line in lines:
            customer = self.parse_customer_text(line)
            customers.append(customer)
        
        return customers

    def parse_customer_text(self, cust_text): # parsing each customer records and storing in list#

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

    def write_customers(self, filename, customers): #writing list data into file#
        
        fo = open(filename, "w")       
        lines = []
        first_customer = True
        for customer in customers:

            if first_customer == True:
                lines.append(customer.file_text())
                first_customer = False
            else:
                lines.append(f"\n{customer.file_text()}")
        
        fo.writelines(lines)
        fo.close()