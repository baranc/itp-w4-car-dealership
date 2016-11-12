#from dealership.vehicles import Vehicle
#from dealership.customers import Person


class Contract(object):
    def __init__(self, customer, vehicle):
        self.vehicle =  vehicle
        self.customer = customer
    
    
    def employee_discount(self):
        if self.customer.is_employee():
            return .9
        else:
            return 1   
        
        

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.monthly_payments = monthly_payments
        
        #if customer is Employee
        
    def total_value(self):
        return (self.vehicle.sale_price() + (self.vehicle.interest_rate() 
        * self.monthly_payments
        * self.vehicle.sale_price() / 100)) * self.employee_discount()
    
    def monthly_value(self):
       return self.total_value()/self.monthly_payments
        
  
    

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        self.vehicle = vehicle
        self.customer = customer
        self.length_in_months = length_in_months
        
    def total_value(self):
        return (self.vehicle.sale_price() + self.lease_multiplier()) * self.employee_discount()
        
    def lease_multiplier(self):
        return self.vehicle.sale_price() * self.vehicle.lease_rate() / self.length_in_months
            
    def monthly_value(self):
       return self.total_value()/self.length_in_months