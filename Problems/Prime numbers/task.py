prime_numbers = [number for number in range(2, 1000)
                 if all(number % divisor for divisor in range(2, number))]
