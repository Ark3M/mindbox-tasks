from collections import Counter
import pandas as pd
import random


def create_customers_ids(n_customers: int, id_length: int, spec_number: int) -> list[str]:
    assert id_length >= 2, "An ID length should be >= 2"
    assert len(str(spec_number)) < id_length, "The first number of ID should be < ID length"

    customers_ids = []
    #chars = list(set(string.digits))  # Variable for case in which we want to generate random IDs.

    for i in range(1, n_customers + 1):  # Customer number starts from 1.
        zeros = id_length - len(str(i)) - len(str(spec_number))
        customer_id = str(spec_number) + "".join([str(0) for i in range(zeros)]) + str(i)
        #customer_id = str(spec_digit) + "".join(random.choices(chars, k=id_length))  # Create random IDs
                                                                                      # with length = id_length.
        customers_ids.append(customer_id)
    return customers_ids


def create_groups_numbers(customers_ids: list[str]) -> list[int]:
    groups_numbers = []

    for id in customers_ids:
        groups_numbers.append(sum(map(int, id)))
    return groups_numbers


def add_customers_in_group(customers_ids: list[str], groups_numbers: list[int]) -> pd.DataFrame:
    data = {"customer_ID": customers_ids,
            "group_number": groups_numbers}

    customers = pd.DataFrame(data=data)
    group_customers_counts = customers["group_number"].value_counts()
    group_customers = customers["group_number"].apply(lambda x: group_customers_counts[x])
    customers.insert(2, "customers_in_group", group_customers)
    return customers


# Task 1. ID starts from zero.
def count_customers_zeros(n_customers: int) -> dict and pd.DataFrame:
    customers_ids = create_customers_ids(n_customers, id_length, spec_number=0)
    assert spec_digit == 0, "The first number of ID should be 0"

    groups_numbers = create_groups_numbers(customers_ids)
    customers = add_customers_in_group(customers_ids, groups_numbers)
    return dict(Counter(groups_numbers)), customers  # You can choose what you want.


# Task 2. ID starts from specified number.
def count_customers_spec(n_customers: int, n_first_id: int) -> dict and pd.DataFrame:
    customers_ids = create_customers_ids(n_customers, id_length, spec_number=n_first_id)
    groups_numbers = create_groups_numbers(customers_ids)
    customers = add_customers_in_group(customers_ids, groups_numbers)
    return dict(Counter(groups_numbers)), customers  # You can choose what you want.

#n_customers = random.randint(1, 100)  # For instance. You can set any integer value from 1 to N.
#id_length = random.randint(5, 7)  # Generate a random ID length in range from 5 to 7.

print("Enter number of customers:")
n_customers = int(input())

print("Enter minimum desired length of ID, but remember that:\n"
      "1. In the first task ID starts from 0.\n"
      "2. In the second task ID starts from entered digit.")
id_length = int(input())

print("Enter the first number of ID:")
spec_number = int(input())

print("\n---Output---")
print("Customers in each group (dict):\n", count_customers_spec(n_customers, n_first_id=spec_number)[0])
print()
print("Customers in each group (DataFrame):\n", count_customers_spec(n_customers, n_first_id=spec_number)[1])
