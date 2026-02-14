"""
Задача 3: Одинокая дорога

На пустынном шоссе вероятность появления автомобиля за 30-минутный период составляет 0.95.

Какова вероятность его появления за 10 минут? А за 27 минут?

Ответ дать в процентах, округлив до десятых через точку с запятой, например: 42,7; 95,0
"""

import random
import numpy as np
import math
from collections import Counter

def lonely_road_analytical():
    """
    Аналитическое решение через пуассоновский процесс и экспоненциальное распределение.
    
    Returns:
        tuple: (вероятность за 10 минут, вероятность за 27 минут)
    """
    # Из условия: P(30) = 0.95
    # Для пуассоновского процесса: P(t) = 1 - e^(-λt)
    
    # Находим интенсивность λ
    # 0.95 = 1 - e^(-30λ)
    # e^(-30λ) = 0.05
    # -30λ = ln(0.05)
    # λ = -ln(0.05) / 30
    
    lambda_rate = -math.log(0.05) / 30
    
    # Вероятность за 10 минут
    prob_10 = 1 - math.exp(-lambda_rate * 10)
    
    # Вероятность за 27 минут
    prob_27 = 1 - math.exp(-lambda_rate * 27)
    
    return prob_10, prob_27

def lonely_road_proportional_method():
    """
    Альтернативный метод через пропорции.
    
    Returns:
        tuple: (вероятность за 10 минут, вероятность за 27 минут)
    """
    # Используем свойство: P(t) = 1 - (1 - P(T))^(t/T)
    # где T = 30 минут, P(T) = 0.95
    
    base_prob = 1 - 0.95  # = 0.05
    
    # Для 10 минут
    prob_10 = 1 - base_prob ** (10/30)
    
    # Для 27 минут
    prob_27 = 1 - base_prob ** (27/30)
    
    return prob_10, prob_27

def lonely_road_simulation(n_simulations=100000):
    """
    Метод Монте-Карло для проверки аналитического решения.
    
    Args:
        n_simulations (int): количество симуляций
        
    Returns:
        tuple: (вероятность за 10 минут, вероятность за 27 минут)
    """
    # Находим λ из условия
    lambda_rate = -math.log(0.05) / 30
    
    # Симуляция для 10 минут
    cars_10 = 0
    for _ in range(n_simulations):
        # Генерируем время до первого автомобиля
        time_to_car = random.expovariate(lambda_rate)
        if time_to_car <= 10:
            cars_10 += 1
    
    # Симуляция для 27 минут
    cars_27 = 0
    for _ in range(n_simulations):
        time_to_car = random.expovariate(lambda_rate)
        if time_to_car <= 27:
            cars_27 += 1
    
    prob_10_sim = cars_10 / n_simulations
    prob_27_sim = cars_27 / n_simulations
    
    return prob_10_sim, prob_27_sim

def lonely_road_exact_calculation():
    """
    Точный расчет через численное интегрирование.
    
    Returns:
        tuple: (вероятность за 10 минут, вероятность за 27 минут)
    """
    lambda_rate = -math.log(0.05) / 30
    
    # Точные вычисления с высокой точностью
    prob_10 = 1 - math.exp(-lambda_rate * 10)
    prob_27 = 1 - math.exp(-lambda_rate * 27)
    
    return prob_10, prob_27

def lonely_road_detailed_analysis():
    """
    Детальный анализ пуассоновского процесса.
    
    Returns:
        dict: детальная информация
    """
    lambda_rate = -math.log(0.05) / 30
    
    analysis = {
        'lambda_rate': lambda_rate,
        'mean_time_between_cars': 1 / lambda_rate,
        'prob_no_car_10': math.exp(-lambda_rate * 10),
        'prob_no_car_27': math.exp(-lambda_rate * 27),
        'prob_no_car_30': math.exp(-lambda_rate * 30),
    }
    
    # Распределение числа автомобилей для разных интервалов
    intervals = [5, 10, 15, 20, 25, 30]
    for interval in intervals:
        # Вероятность k автомобилей за интервал
        probs = []
        for k in range(6):  # до 5 автомобилей
            prob = (lambda_rate * interval) ** k * math.exp(-lambda_rate * interval) / math.factorial(k)
            probs.append(prob)
        analysis[f'prob_dist_{interval}'] = probs
    
    return analysis

def lonely_road_probability_distribution():
    """
    Распределение вероятностей времени до первого автомобиля.
    
    Returns:
        dict: распределение по временным интервалам
    """
    lambda_rate = -math.log(0.05) / 30
    n_simulations = 50000
    
    distribution = Counter()
    
    for _ in range(n_simulations):
        time_to_car = random.expovariate(lambda_rate)
        
        # Категоризируем по интервалам
        if time_to_car <= 5:
            distribution['0-5 мин'] += 1
        elif time_to_car <= 10:
            distribution['5-10 мин'] += 1
        elif time_to_car <= 15:
            distribution['10-15 мин'] += 1
        elif time_to_car <= 20:
            distribution['15-20 мин'] += 1
        elif time_to_car <= 25:
            distribution['20-25 мин'] += 1
        elif time_to_car <= 30:
            distribution['25-30 мин'] += 1
        else:
            distribution['>30 мин'] += 1
    
    # Преобразование в вероятности
    probabilities = {k: v/n_simulations for k, v in distribution.items()}
    
    return probabilities

def format_probability(prob):
    """
    Форматирует вероятность в требуемый формат.
    
    Args:
        prob (float): вероятность как десятичная дробь
        
    Returns:
        str: отформатированная вероятность
    """
    percentage = prob * 100
    return f"{percentage:.1f}".replace('.', ',')

def main():
    """
    Основная функция для демонстрации всех методов решения.
    """
    print("ЗАДАЧА 3: ОДИНОКАЯ ДОРОГА")
    print("=" *30)
    print("Вероятность появления автомобиля за 30 минут = 0.95")
    print("Найти вероятность за 10 и 27 минут.")
    print()
    
    # Аналитическое решение
    prob_10, prob_27 = lonely_road_analytical()
    print(f"Аналитическое решение:")
    print(f"   Интенсивность λ = {-math.log(0.05)/30:.4f} автомобилей/минуту")
    print(f"   P(10 мин) = 1 - e^(-λ×10) = {prob_10:.3f} = {format_probability(prob_10)}%")
    print(f"   P(27 мин) = 1 - e^(-λ×27) = {prob_27:.3f} = {format_probability(prob_27)}%")
    print()
    
    # Метод пропорций
    prob_10_prop, prob_27_prop = lonely_road_proportional_method()
    print(f"Метод пропорций:")
    print(f"   P(10 мин) = 1 - 0.05^(1/3) = {prob_10_prop:.3f} = {format_probability(prob_10_prop)}%")
    print(f"   P(27 мин) = 1 - 0.05^0.9 = {prob_27_prop:.3f} = {format_probability(prob_27_prop)}%")
    print()
    
    # Метод Монте-Карло
    prob_10_sim, prob_27_sim = lonely_road_simulation(50000)
    print(f"Метод Монте-Карло (50,000 симуляций):")
    print(f"   P(10 мин) = {prob_10_sim:.3f} = {format_probability(prob_10_sim)}%")
    print(f"   P(27 мин) = {prob_27_sim:.3f} = {format_probability(prob_27_sim)}%")
    print(f"   Погрешность 10 мин: {abs(prob_10 - prob_10_sim):.4f}")
    print(f"   Погрешность 27 мин: {abs(prob_27 - prob_27_sim):.4f}")
    print()
    
    # Распределение времени до первого автомобиля
    time_distribution = lonely_road_probability_distribution()
    print(f"Распределение времени до первого автомобиля:")
    for interval in sorted(time_distribution.keys()):
        prob = time_distribution[interval]
        print(f"   {interval}: {prob:.3f} ({prob*100:.1f}%)")
    print()
    
    # Детальный анализ
    analysis = lonely_road_detailed_analysis()
    print("Детальный анализ пуассоновского процесса:")
    print(f"   Интенсивность λ: {analysis['lambda_rate']:.4f} автомобилей/минуту")
    print(f"   Среднее время между автомобилями: {analysis['mean_time_between_cars']:.2f} минут")
    print(f"   P(нет авто за 10 мин): {analysis['prob_no_car_10']:.3f}")
    print(f"   P(нет авто за 27 мин): {analysis['prob_no_car_27']:.3f}")
    print(f"   P(нет авто за 30 мин): {analysis['prob_no_car_30']:.3f}")
    print()
    
    # Распределение числа автомобилей
    print("Вероятность k автомобилей за 10 минут:")
    for k in range(5):
        prob = analysis['prob_dist_10'][k]
        print(f"   {k} авто: {prob:.3f} ({prob*100:.1f}%)")
    print()
    
    # Математические выкладки
    print("Математические выкладки:")
    print("   Из условия: P(30) = 0.95 = 1 - e^(-30λ)")
    print("   Отсюда: e^(-30λ) = 0.05")
    print(f"   λ = -ln(0.05)/30 = {-math.log(0.05)/30:.4f}")
    print()
    print("   P(10) = 1 - e^(-λx10)")
    print(f"   P(10) = 1 - e^({-math.log(0.05)/30 * 10:.3f}) = {prob_10:.3f}")
    print()
    print("   P(27) = 1 - e^(-λx27)")
    print(f"   P(27) = 1 - e^({-math.log(0.05)/30 * 27:.3f}) = {prob_27:.3f}")
    print()
    
    print(f"ОТВЕТ: {format_probability(prob_10)}; {format_probability(prob_27)}")
    print("=" * 20)

if __name__ == "__main__":
    main()
