class IsPrime:
    def __init__(self, num):
        if not isinstance(num, int):
            raise ValueError(f"Invalid input: {num}. Only integers are allowed.")
        self.num = num

    def check_prime(self):
        # Если число меньше или равно 1, оно не является простым или составным
        if self.num <= 1:
            return False
        # Число 2 - это особый случай, оно простое
        if self.num == 2:
            return True
        # Все четные числа больше 2 - составные
        if self.num % 2 == 0:
            return False
        # Проверяем делимость до квадратного корня числа
        for i in range(3, int(self.num ** 0.5) + 1, 2):
            if self.num % i == 0:
                return False
        return True


def isPrime(num):
    prime_checker = IsPrime(num)
    return prime_checker.check_prime()


def isComposite(num):
    # Составное число - это любое число больше 1, которое не является простым
    prime_checker = IsPrime(num)
    return num > 1 and not prime_checker.check_prime()


def check_list_prime(lst):
    if not isinstance(lst, list):
        raise ValueError(f"Expected a list, but got {type(lst).__name__}")

    primes = []
    composites = []

    for num in lst:
        if not isinstance(num, int):
            raise ValueError(f"Invalid element in list: {num}. Only integers are allowed.")

        if isPrime(num):
            primes.append(num)
        elif isComposite(num):
            composites.append(num)

    return primes, composites
