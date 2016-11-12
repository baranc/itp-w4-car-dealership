import unittest

from dealership.contracts import BuyContract, LeaseContract
from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle


class BaseContractTestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(maker='Ford', model='Mustang', year=2005,
                       base_price=18000, miles=31000)

        self.truck = Truck(maker='Chevrolet', model='Silverado', year=2014,
                           base_price=29000, miles=3000)

        self.bike = Motorcycle(maker='Ducati', model='Monster',
                               year=2016, base_price=18000, miles=700)

        self.customer = Customer('John', 'Doe', 'john@example.com')
        self.employee = Employee('Jane', 'Doe', 'jane@example.com')


class BuyContractTestCase(BaseContractTestCase):
    def test_buy_contract_total_value_with_customer(self):
        car_contract = BuyContract(
            vehicle=self.car, customer=self.customer, monthly_payments=6)

        self.assertAlmostEqual(car_contract.total_value(), 22986.72, places=3)
        self.assertAlmostEqual(car_contract.monthly_value(), 3831.12, places=3)

        truck_contract = BuyContract(
            vehicle=self.truck, customer=self.customer, monthly_payments=12)

        self.assertAlmostEqual(
            truck_contract.total_value(), 52580.47, places=1)
        self.assertAlmostEqual(
            truck_contract.monthly_value(), 4381.70, places=1)

        bike_contract = BuyContract(
            vehicle=self.bike, customer=self.customer, monthly_payments=36)

        self.assertAlmostEqual(
            bike_contract.total_value(), 27141.84, places=2)
        self.assertAlmostEqual(
            bike_contract.monthly_value(), 753.94, places=2)

    def test_buy_contract_total_value_with_employee(self):
        car_contract = BuyContract(
            vehicle=self.car, customer=self.employee, monthly_payments=6)

        self.assertAlmostEqual(car_contract.total_value(), 20688.04, places=1)
        self.assertAlmostEqual(car_contract.monthly_value(), 3448, places=1)

        truck_contract = BuyContract(
            vehicle=self.truck, customer=self.employee, monthly_payments=12)

        self.assertAlmostEqual(
            truck_contract.total_value(), 47322.43, places=2)
        self.assertAlmostEqual(
            truck_contract.monthly_value(), 3943.53, places=1)

        bike_contract = BuyContract(
            vehicle=self.bike, customer=self.employee, monthly_payments=36)

        self.assertAlmostEqual(
            bike_contract.total_value(), 24427.65, places=1)
        self.assertAlmostEqual(
            bike_contract.monthly_value(), 678.54, places=1)


class LeaseContractTestCase(BaseContractTestCase):
    def test_buy_contract_total_value_with_customer(self):
        car_contract = LeaseContract(
            vehicle=self.car, customer=self.customer, length_in_months=12)

        self.assertAlmostEqual(car_contract.total_value(), 23760.0, places=3)
        self.assertAlmostEqual(car_contract.monthly_value(), 1980.0, places=3)

        truck_contract = LeaseContract(
            vehicle=self.truck, customer=self.customer, length_in_months=24)

        self.assertAlmostEqual(
            truck_contract.total_value(), 49686.66, places=1)
        self.assertAlmostEqual(
            truck_contract.monthly_value(), 2070.27, places=1)

        bike_contract = LeaseContract(
            vehicle=self.bike, customer=self.customer, length_in_months=36)

        self.assertAlmostEqual(
            bike_contract.total_value(), 20350, places=2)
        self.assertAlmostEqual(
            bike_contract.monthly_value(), 565.27, places=1)
