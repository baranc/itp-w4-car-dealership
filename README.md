# Dealership calculator

Today we'll be building a system that will assist a vehicle dealership to calculate prices when a user wants to buy/lease a car. A dealership can also buy vehicles from customers.

There are three types of vehicles in the dealership: `Car`, `Truck` and `Motorcycle`. All these vehicles have the same attributes: `maker`, `model`, `year`, `base_price` (**important**, it'll be used to compute sale and purchase final prices), `miles` (see tests for more details).

### Customers

There are two types of customers (both extending the class `Person`): `Customer` and `Employee`. An Employee can decide to buy a car from the dealership, and she/he will have a discount. We'll talk about this in the _Contracts_ section below.

### Sale and purchase prices

A dealership can either buy or sell vehicles. The dealership will set special prices for both, selling and buying vehicles, which will be computed using the `base_price` specified. The prices are computed in this way:

* Sale price (`vehicle.sale_price()`, the price a customer has to pay TO the dealership to buy a vehicle): `base_price * S`. In this case `S` is a multiplier that will vary depending on the type of vehicle. (see section below).

* Purchase price (`vehicle.purchase_price()`, the price the dealership will pay a customer to buy her/his vehicle): `sale_price() - (P * miles)`. Similar to `S`, `P` will be a multiplier depending on the type of vehicle.

### Price multipliers for vehicles

**Sale multipliers**
* `Car`: 1.2
* `Motorcycle`: 1.1
* `Truck`: 1.6

**Purchase multipliers**
* `Car`: 0.004
* `Motorcycle`: 0.009
* `Truck`: 0.02

### Contracts

A customer can either buy or lease a car. There are two types of contracts to support such operations: `BuyContract` and `LeaseContract`. A contract will have two important methods:
* `total_value()` is the total value of the contract to pay by a customer.
* `monthly_value()` is the amount of money that a customer is supposed to pay monthly.

Each contract will have a different way to compute its value. But for both of them the value will depend of the price of the vehicle (discussed above) and the type of Customer. If the customer is an Employee, the contract will have a final discount of **10%**. If the customer is a regular `Customer`, there's no discount applied.

##### Buy Contracts

A `BuyContract` is created by passing the following attributes:

* `customer`: Either a regular `Customer` or an `Employee`
* `vehicle`: The vehicle involved in the transaction.
* `monthly_payments`: How many months the customer is going to take to pay for the whole contract. Example, if `monthly_payments` is 2, the customer will take two months to pay for it.

The `total_value()` of a `BuyContract` will be computed in this way: `vehicle.sale_price() + (I * monthly_payments * sale_price() / 100) - (discount if employee)`. In this case `I` is the interest rate applied and it will vary depending of the type of vehicle:

* `Car`: 7% monthly (1.07)
* `Motorcycle`: 3% monthly (1.03)
* `Truck`: 11% monthly (1.11)

The `monthly_value` of the contract will be just the total value divided by the amount of months: `total_value() / monthly_payments`.

##### Lease Contracts

A `LeaseContract` is created by passing the following attributes:

* `customer`: Either a regular `Customer` or an `Employee`
* `vehicle`: The vehicle involved in the transaction.
* `length_in_months`: How many months the customer is going to lease the vehicle.

The `total_value()` of a `LeaseContract` will be computed in this way: `vehicle.sale_price() + (lease_multiplier) - (discount if employee) * `. In this case `lease_multiplier` depends on the vehicle and is computed in the following way:

* `Car`: `sale_price() + (sale_price() * 1.2 / length_in_months)`.
* `Motorcycle`: `sale_price() + (sale_price() * 1 / length_in_months)`
* `Truck`: `sale_price() + (sale_price() * 1.7 / length_in_months)`

The `monthly_value` of the contract will be just the total value divided by the amount of months: `total_value() / length_in_months`.

## Examples

### Sale and Purchase prices

##### Car

Given a car with base_price $8,000 and 21,000 miles:
* `sale_price()` is: `$8,000 x 1.2` = `$9,600`
* `purchase_price()` is: `sale_price() - [0.004 * 21,000 (miles)]` = `9600 - (0.004 * 21000)` = `$9,516`

##### Motorcycle

Given a motorcycle with base_price $11,500 and 5000 miles:
* `sale_price()` is: `$11,500 x 1.1` = `$12,650`
* `purchase_price()` is: `sale_price() - [0.009 * 5,000 (miles)]` = `12650 - (0.009 * 5000)` = `$12,605`

##### Truck

Given a truck with base_price $21,900 and 50,000 miles
* `sale_price()` is: `$21,900 x 1.6` = `$35,040`
* `purchase_price()` is: `sale_price() - [0.02 * 50,000 (miles)]` = `35040 - (0.02 * 50000)` = `$34,040`

### Contracts

##### BuyContract

Given a Car with `sale_price()` $15,000, a regular customer (not employee) and 12 monthly_payments:

* `total_value()`: `sale_price() + (1.07 * monthly_payments * sale_price() / 100) - (discount if employee)` = `$15,000 + (1.07 * 12 * $15,000 / 100) - $0 (no employee)` = `15000 + (1.07 * 12 * 15000 / 100)` = `$16,926`
* `monthly_value()`: `total_value() / monthly_payments` = `$16,926 / 12` = `$1,410.50`

##### LeaseContract

Given a Truck with `sale_price()` $35,000, a regular customer (not employee) and 36 `length_in_months`:

* `total_value()`: `sale_price() + (sale_price() * 1.7 / length_in_months)` = `$35,000 + (35,000 * 1.7 / 36)` = `$36,652.77`
* `monthly_value()`: `total_value() / monthly_payments` = `$36,652.78 / 36` = `$1,018.13`
