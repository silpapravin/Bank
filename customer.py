class Customer:
    def __init__(self, forename, surname,ppsnumber, accounttype, overdraft, accountnumber,balance,interest):

        self._forename = forename
        self._surname = surname 
        self._ppsnumber=ppsnumber
        self._accounttype = accounttype
        self._overdraft = overdraft
        self._accountnumber=accountnumber
        self._balance = balance
        self._interest=interest

    def __repr__(self):
        repr = f"{(self.forename).ljust(10)} {self.surname.ljust(10)}{self._ppsnumber.ljust(10)} {self._accounttype.ljust(15)} "
        repr = repr + f"{self._overdraft.ljust(10)} {str(self._accountnumber).ljust(10)} "
        repr = repr + f"{str(self.balance).ljust(10)} {self.interest}"

        return repr

    def file_text(self):
        return f"{self.forename}|{self.surname}|{self._ppsnumber}|{self._accounttype}|{self.overdraft}|{self._accountnumber}|{self.balance}|{self._interest}" 
        
    
    @property
    def forename(self):
        return self._forename

    @forename.setter
    def forename(self, new_forename):
        self._forename = new_forename

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def ppsnumber(self):
        return self._ppsnumber

    @ppsnumber.setter
    def phone_number(self, new_ppsnumber):
        self._ppsnumber = new_ppsnumber

    @property
    def accounttype(self):
        return self._accounttype

    @accounttype.setter
    def email_address(self, new_accounttype):
        self._accounttype = new_accounttype

    @property
    def overdraft(self):
        return self._overdraft

    @overdraft.setter
    def overdraft(self, new_overdraft):
        self._overdraft = new_overdraft

    @property
    def accountnumber(self):
        return self._accountnumber

    @accountnumber.setter
    def accountnumber(self, new_accountnumber):
        self._accountnumber = new_accountnumber

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, new_interest):
        self._interest = new_interest