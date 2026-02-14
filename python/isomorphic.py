def is_isomorphic(s: str, t: str) -> bool:
    """
    Проверяет, являются ли две строки изоморфными.
    
    Строки s и t называются изоморфными, если все вхождения каждого символа 
    строки s можно последовательно заменить другим символом и получить строку t.
    Порядок символов при этом должен сохраняться, а замена — быть уникальной.
    
    Args:
        s (str): Первая строка
        t (str): Вторая строка
        
    Returns:
        bool: True если строки изоморфны, False в противном случае
        
    Time Complexity: O(n), где n - длина строк
    Space Complexity: O(k), где k - количество уникальных символов (<= n)
    """
    if len(s) != len(t):
        return False
    
    # Словарь для соответствия символов из s в символы из t
    s_to_t = {}
    # Словарь для соответствия символов из t в символы из s
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Проверяем соответствие из s в t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Проверяем соответствие из t в s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True


# Тесты
if __name__ == "__main__":
    # Пример из задания
    print(is_isomorphic('paper', 'title'))  # True
    
    # Дополнительные тесты
    print(is_isomorphic('egg', 'add'))      # True
    print(is_isomorphic('foo', 'bar'))      # False
    print(is_isomorphic('paper', 'title'))  # True
    print(is_isomorphic('ab', 'aa'))        # False
    print(is_isomorphic('aab', 'xxy'))      # True
    print(is_isomorphic('aab', 'xyz'))      # False
