class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.employee = False
        
    def is_employee(self):
        return self.employee


class Customer(Person):
    def __init__ (self, first_name, last_name, email):
        Person.__init__(self, first_name, last_name, email)
        self.employee = False
        


class Employee(Person):
    def __init__ (self, first_name, last_name, email):
        Person.__init__(self, first_name, last_name, email)
        self.employee = True
