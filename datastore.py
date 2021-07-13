from customer import Customer
from file_parser import FileParser
class Datastore:

    def __init__(self):

        self._customers = []
        
        self.read_customers()

    def read_customers(self):

        file_parser = FileParser()
        self._customers = file_parser.read_customers("custs.txt")

    def add_customer(self, customer):

        self._customers.append(customer)


    @property
    def customers(self):
        return self._customers
