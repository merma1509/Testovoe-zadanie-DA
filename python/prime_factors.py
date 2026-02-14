def prime_factors(n):
    """
    Разбивает натуральное число n на простые множители.
    
    Алгоритм пробного деления с оптимизацией:
    1. Сначала делим на 2, пока делится
    2. Затем проверяем нечетные делители до √n
    3. Если остаток > 1, он тоже простой множитель
    
    Args:
        n (int): Натуральное число для факторизации
        
    Returns:
        list: Список простых множителей в порядке возрастания
        
    Time Complexity: O(√n), где n - входное число
    Space Complexity: O(log n) - максимальное количество множителей
    """
    if n <= 1:
        return []
    
    factors = []
    
    # Делим на 2, пока возможно
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Проверяем нечетные делители от 3 до √n
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # Переходим к следующему нечетному числу
    
    # Если остаток > 1, он простой
    if n > 1:
        factors.append(n)
    
    return factors


# Оптимизированная версия с предварительной проверкой простых чисел
def prime_factors_optimized(n):
    """
    Оптимизированная версия с использованием решета Эратосфена для малых чисел.
    """
    if n <= 1:
        return []
    
    # Для малых чисел используем решето Эратосфена
    if n < 1000:
        return prime_factors_with_sieve(n)
    else:
        return prime_factors(n)


def prime_factors_with_sieve(n):
    """
    Факторизация с использованием решета Эратосфена для чисел < 1000.
    """
    # Создаем решето до √n
    limit = int(n ** 0.5) + 1
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    
    factors = []
    remaining = n
    
    for prime in primes:
        while remaining % prime == 0:
            factors.append(prime)
            remaining //= prime
        if prime * prime > remaining:
            break
    
    if remaining > 1:
        factors.append(remaining)
    
    return factors


# Тесты
if __name__ == "__main__":
    # Пример из задания
    n = 56
    print(prime_factors(n))  # [2, 2, 2, 7]
    
    # Дополнительные тесты
    print(prime_factors(1))        # []
    print(prime_factors(2))        # [2]
    print(prime_factors(13))       # [13]
    print(prime_factors(100))      # [2, 2, 5, 5]
    print(prime_factors(84))       # [2, 2, 3, 7]
    print(prime_factors(9973))     # [9973] (простое число)
    
    # Сравнение с оптимизированной версией
    import time
    test_numbers = [56, 100, 9973, 123456]
    
    for num in test_numbers:
        start = time.time()
        result1 = prime_factors(num)
        time1 = time.time() - start
        
        start = time.time()
        result2 = prime_factors_optimized(num)
        time2 = time.time() - start
        
        print(f"{num}: {result1} (basic: {time1:.6f}s, optimized: {time2:.6f}s)")
