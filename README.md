
# NWOS: Python Library for Prime and Composite Number Checking

**NWOS** is a Python library designed to work with **prime** and **composite** numbers. It provides simple and efficient functions for checking whether a number is prime or composite, and can also process lists of numbers.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
  - [Prime Number Check](#prime-number-check)
  - [Composite Number Check](#composite-number-check)
  - [Batch Checking for Lists](#batch-checking-for-lists)
- [Usage](#usage)
  - [Checking a Single Number](#checking-a-single-number)
  - [Checking Composite Numbers](#checking-composite-numbers)
  - [Checking a List of Numbers](#checking-a-list-of-numbers)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the **nwos** library, use the following command:

```bash
pip install nwos
```

Ensure that you are using Python version 3.6 or higher.

## Features

The **nwos** library includes the following key functionalities:

### Prime Number Check

- **Prime number**: A natural number greater than 1 that is divisible only by 1 and itself.
- Function `is_prime(num)` returns `True` if the number is prime and `False` otherwise.

### Composite Number Check

- **Composite number**: A natural number greater than 1 that is not prime, meaning it has divisors other than 1 and itself.
- Function `is_composite(num)` returns `True` if the number is composite and `False` otherwise.

### Batch Checking for Lists

- Pass a list of numbers to the function `check_list_prime(lst)`, and it will return two lists: one for prime numbers and another for composite numbers.

## Usage

Below are some examples showing how to use the **nwos** library.

### Checking a Single Number

To check if a number is prime, use the function `is_prime(num)`:

```python
import nwos

# Check if a number is prime
number = 29
if nwos.is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```

### Checking Composite Numbers

To check if a number is composite, use the function `is_composite(num)`:

```python
import nwos

# Check if a number is composite
number = 30
if nwos.is_composite(number):
    print(f"{number} is a composite number.")
else:
    print(f"{number} is not a composite number.")
```

### Checking a List of Numbers

To check a list of numbers and separate them into primes and composites, use `check_list_prime(lst)`:

```python
import nwos

numbers = [10, 17, 23, 25, 30, 37]
primes, composites = nwos.check_list_prime(numbers)

print("Prime numbers:", primes)
print("Composite numbers:", composites)
```

For the input list `[10, 17, 23, 25, 30, 37]`, the output will be:
```
Prime numbers: [17, 23, 37]
Composite numbers: [10, 25, 30]
```

## Error Handling

The library raises appropriate exceptions when incorrect input types are passed. For example, if the input is not an integer, a `ValueError` is raised:

```python
import nwos

try:
    nwos.is_prime("string instead of a number")
except ValueError as e:
    print(f"Error: {e}")
```

This will output:
```
Error: Invalid input: 'string instead of a number'. Only integers are allowed.
```

## Contributing

If you'd like to contribute to the **nwos** library, you are welcome to submit issues or pull requests to the [GitHub repository](https://github.com/your-username/nwos). 

Before submitting a pull request, please ensure that your code follows Python best practices and includes tests for any new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
