def missing_number(nums):
    """
    Находит единственное отсутствующее число из последовательности натуральных чисел 1,2,…,n.
    
    Использует арифметическую формулу суммы первых n натуральных чисел:
    S = n(n+1)/2, где n - длина полного массива
    
    Args:
        nums (list): Массив чисел от 1 до n с одним отсутствующим элементом
        
    Returns:
        int: Отсутствующее число
        
    Time Complexity: O(n), где n - длина массива
    Space Complexity: O(1) - дополнительная память не используется
    """
    n = len(nums) + 1  # Полная длина массива с отсутствующим элементом
    expected_sum = n * (n + 1) // 2  # Сумма чисел от 1 до n
    actual_sum = sum(nums)  # Сумма существующих чисел
    return expected_sum - actual_sum


# Альтернативное решение через XOR (тоже O(1) памяти)
def missing_number_xor(nums):
    """
    Находит отсутствующее число с использованием операции XOR.
    
    XOR всех чисел от 1 до n и всех чисел в массиве даст отсутствующее число,
    так как a ^ a = 0 и a ^ 0 = a.
    """
    n = len(nums) + 1
    xor_all = 0
    
    # XOR всех чисел от 1 до n
    for i in range(1, n + 1):
        xor_all ^= i
    
    # XOR всех чисел в массиве
    for num in nums:
        xor_all ^= num
    
    return xor_all


# Тесты
if __name__ == "__main__":
    # Пример из задания
    nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
    print(missing_number(nums))      # 7
    print(missing_number_xor(nums))   # 7
    
    # Дополнительные тесты
    print(missing_number([2, 3, 1, 5]))  # 4
    print(missing_number([1]))           # 2
    print(missing_number([]))            # 1
    print(missing_number([1, 2, 4, 5]))   # 3
