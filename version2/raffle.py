"""Randomly pick customer and print customer info"""

# Hint: remember to import any functions you need from
# other files or libraries

import random

from customers import get_customers_from_file


def random_winner(customers):
    """Select a random winner from list of customers."""

    random_customer = random.choice(customers)

    name = random_customer.name
    email = random_customer.email

    print(f"Tell {name} at {email} that they've won")


def raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    random_winner(customers)


if __name__ == "__main__":
    raffle()