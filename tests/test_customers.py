import unittest

from dealership.customers import Customer, Employee


class CustomerTestCase(unittest.TestCase):
    def test_if_are_employee(self):
        c = Customer('John', 'Doe', 'john@example.com')
        self.assertEqual(c.first_name, 'John')
        self.assertEqual(c.last_name, 'Doe')
        self.assertEqual(c.email, 'john@example.com')
        self.assertFalse(c.is_employee())

        e = Employee('Jane', 'Doe', 'jane@example.com')
        self.assertEqual(e.first_name, 'Jane')
        self.assertEqual(e.last_name, 'Doe')
        self.assertEqual(e.email, 'jane@example.com')
        self.assertTrue(e.is_employee())
