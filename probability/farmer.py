"""
Задача 1: Фермер

На ферме содержатся шесть разных видов животных, и каждый раз, когда фермер заходит в сарай, 
он видит одно случайное животное. За день фермер заходит в сарай 6 раз.

Каково математическое ожидание количества разных видов животных, которые фермер увидит за день?
"""

import random
import numpy as np
from collections import Counter
from itertools import product

def farmer_expected_value_analytical():
    """
    Аналитическое решение через линейность математического ожидания.
    
    Returns:
        float: математическое ожидание количества разных видов животных
    """
    n_animals = 6
    n_visits = 6
    
    # Вероятность увидеть конкретный вид животного хотя бы раз
    prob_see_animal = 1 - (1 - 1/n_animals) ** n_visits
    
    # По линейности математического ожидания
    expected_value = n_animals * prob_see_animal
    
    return expected_value

def farmer_simulation(n_simulations=100000):
    """
    Метод Монте-Карло для проверки аналитического решения.
    
    Args:
        n_simulations (int): количество симуляций
        
    Returns:
        float: среднее количество разных видов животных по симуляциям
    """
    n_animals = 6
    n_visits = 6
    
    total_unique_animals = 0
    
    for _ in range(n_simulations):
        # Симуляция одного дня
        daily_visits = [random.randint(1, n_animals) for _ in range(n_visits)]
        unique_animals = len(set(daily_visits))
        total_unique_animals += unique_animals
    
    return total_unique_animals / n_simulations

def farmer_exact_calculation():
    """
    Точный расчет через перебор всех возможных комбинаций.
    
    Returns:
        float: точное математическое ожидание
    """
    n_animals = 6
    n_visits = 6
    
    # Все возможные комбинации посещений
    all_combinations = product(range(1, n_animals + 1), repeat=n_visits)
    
    total_unique = 0
    total_combinations = n_animals ** n_visits
    
    for combination in all_combinations:
        unique_count = len(set(combination))
        total_unique += unique_count
    
    return total_unique / total_combinations

def farmer_probability_distribution():
    """
    Распределение вероятностей для количества разных видов животных.
    
    Returns:
        dict: распределение вероятностей
    """
    n_animals = 6
    n_visits = 6
    
    # Подсчет всех комбинаций
    all_combinations = product(range(1, n_animals + 1), repeat=n_visits)
    distribution = Counter()
    
    for combination in all_combinations:
        unique_count = len(set(combination))
        distribution[unique_count] += 1
    
    total_combinations = n_animals ** n_visits
    
    # Преобразование в вероятности
    probabilities = {k: v/total_combinations for k, v in distribution.items()}
    
    return probabilities

def main():
    """
    Основная функция для демонстрации всех методов решения.
    """
    print("=" * 60)
    print("ЗАДАЧА 1: ФЕРМЕР")
    print("=" * 60)
    print("На ферме содержатся 6 разных видов животных.")
    print("Фермер заходит в сарай 6 раз в день.")
    print("Каково математическое ожидание количества разных видов животных?")
    print()
    
    # Аналитическое решение
    analytical_result = farmer_expected_value_analytical()
    print(f"📊 Аналитическое решение:")
    print(f"   E[X] = 6 × (1 - (5/6)^6) = {analytical_result:.4f}")
    print(f"   Округленный ответ: {analytical_result:.2f}")
    print()
    
    # Метод Монте-Карло
    simulation_result = farmer_simulation(50000)
    print(f"🎲 Метод Монте-Карло (50,000 симуляций):")
    print(f"   Среднее значение: {simulation_result:.4f}")
    print(f"   Погрешность: {abs(analytical_result - simulation_result):.4f}")
    print()
    
    # Распределение вероятностей
    probabilities = farmer_probability_distribution()
    print(f"📈 Распределение вероятностей:")
    for unique_count in sorted(probabilities.keys()):
        prob = probabilities[unique_count]
        print(f"   {unique_count} разных видов: {prob:.4f} ({prob*100:.2f}%)")
    print()
    
    # Проверка через распределение
    expected_from_distribution = sum(k * v for k, v in probabilities.items())
    print(f"✅ Проверка через распределение:")
    print(f"   E[X] = Σ(k × P(k)) = {expected_from_distribution:.4f}")
    print()
    
    # Математические детали
    print("🧮 Математические выкладки:")
    print("   Вероятность увидеть конкретный животное:")
    print("   P(увидеть) = 1 - P(не увидеть) = 1 - (5/6)^6")
    print(f"   P(увидеть) = 1 - {15625/46656:.6f} = {1 - 15625/46656:.6f}")
    print()
    print("   По линейности математического ожидания:")
    print("   E[X] = Σ E[X_i] = 6 × P(увидеть)")
    print(f"   E[X] = 6 × {1 - 15625/46656:.6f} = {analytical_result:.4f}")
    print()
    
    print("=" * 60)
    print(f"ОТВЕТ: {analytical_result:.2f}")
    print("=" * 60)

if __name__ == "__main__":
    main()
