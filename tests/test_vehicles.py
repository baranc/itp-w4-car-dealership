import unittest

from dealership.vehicles import Car, Truck, Motorcycle


class CarTestCase(unittest.TestCase):
    def test_car_creation(self):
        c = Car(maker='Ford', model='Mustang', year=2005,
                base_price=18000, miles=31000)

        self.assertEqual(c.maker, 'Ford')
        self.assertEqual(c.model, 'Mustang')
        self.assertEqual(c.year, 2005)
        self.assertEqual(c.base_price, 18000)
        self.assertEqual(c.miles, 31000)

    def test_cars_sale_price(self):
        v1 = Car(maker='Ford', model='Mustang', year=2005,
                 base_price=18000, miles=31000)
        v2 = Car(maker='Ford', model='Mustang', year=2014,
                 base_price=31000, miles=11000)

        self.assertEqual(v1.sale_price(), 21600)
        self.assertEqual(v2.sale_price(), 37200)

    def test_cars_purchase_price(self):
        v1 = Car(maker='Ford', model='Mustang', year=2005,
                 base_price=18000, miles=31000)
        v2 = Car(maker='Ford', model='Mustang', year=2014,
                 base_price=31000, miles=11000)

        self.assertEqual(v1.purchase_price(), 21476)
        self.assertEqual(v2.purchase_price(), 37156)


class TruckTestCase(unittest.TestCase):
    def test_truck_creation(self):
        t = Truck(maker='Chevrolet', model='Silverado', year=2014,
                  base_price=29000, miles=3000)

        self.assertEqual(t.maker, 'Chevrolet')
        self.assertEqual(t.model, 'Silverado')
        self.assertEqual(t.year, 2014)
        self.assertEqual(t.base_price, 29000)
        self.assertEqual(t.miles, 3000)

    def test_trucks_sale_price(self):
        v1 = Truck(maker='Chevrolet', model='Silverado', year=2014,
                   base_price=29000, miles=3000)
        v2 = Truck(maker='Chevrolet', model='Silverado', year=2004,
                   base_price=16000, miles=52000)

        self.assertEqual(v1.sale_price(), 46400)
        self.assertEqual(v2.sale_price(), 25600)

    def test_trucks_purchase_price(self):
        v1 = Truck(maker='Chevrolet', model='Silverado', year=2014,
                   base_price=29000, miles=3000)
        v2 = Truck(maker='Chevrolet', model='Silverado', year=2004,
                   base_price=16000, miles=52000)

        self.assertEqual(v1.purchase_price(), 46340)
        self.assertEqual(v2.purchase_price(), 24560)


class MotorcycleTestCase(unittest.TestCase):
    def test_motorcycle_creation(self):
        m = Motorcycle(maker='Ducati', model='Monster', year=2016,
                       base_price=18000, miles=700)

        self.assertEqual(m.maker, 'Ducati')
        self.assertEqual(m.model, 'Monster')
        self.assertEqual(m.year, 2016)
        self.assertEqual(m.base_price, 18000)
        self.assertEqual(m.miles, 700)

    def test_motorcycle_sale_price(self):
        v1 = Motorcycle(maker='Ducati', model='Monster', year=2016,
                        base_price=18000, miles=700)
        v2 = Motorcycle(maker='Ducati', model='Monster', year=2009,
                        base_price=9000, miles=11400)

        self.assertEqual(v1.sale_price(), 19800)
        self.assertEqual(v2.sale_price(), 9900)

    def test_motorcycle_purchase_price(self):
        v1 = Motorcycle(maker='Ducati', model='Monster', year=2016,
                        base_price=18000, miles=700)
        v2 = Motorcycle(maker='Ducati', model='Monster', year=2009,
                        base_price=9000, miles=11400)

        self.assertEqual(v1.purchase_price(), 19793.7)
        self.assertEqual(v2.purchase_price(), 9797.4)
