from .vehicles import Car, Truck, Motorcycle


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def _discounted_price(self, price):
        if self.customer.is_employee():
            return price * .9
        return price

    def monthly_value(self):
        return self.total_value() / self._monthly_attribute()


class BuyContract(Contract):
    VEHICLE_MULTIPLIERS = {
        Car: 1.07,
        Motorcycle: 1.03,
        Truck: 1.11
    }

    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        sale_price = self.vehicle.sale_price()
        multiplier = self.VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        price = sale_price + (multiplier * self.monthly_payments *
                              sale_price / 100)

        return self._discounted_price(price)

    def _monthly_attribute(self):
        return self.monthly_payments


class LeaseContract(Contract):
    VEHICLE_MULTIPLIERS = {
        Car: 1.2,
        Motorcycle: 1,
        Truck: 1.7
    }

    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        sale_price = self.vehicle.sale_price()
        multiplier = self.VEHICLE_MULTIPLIERS[self.vehicle.__class__]
        price = sale_price + (sale_price * multiplier / self.length_in_months)

        return self._discounted_price(price)

    def _monthly_attribute(self):
        return self.length_in_months
