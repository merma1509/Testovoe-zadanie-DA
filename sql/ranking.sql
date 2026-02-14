-- Задача 1: Абитуриенты
-- Создание колонки с позицией абитуриента в общем рейтинге

-- Решение с использованием оконной функции (оптимальное)
SELECT 
    id,
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position
FROM examination
ORDER BY scores DESC;

-- Альтернативное решение без оконных функций (через self join)
SELECT 
    e1.id,
    e1.scores,
    COUNT(DISTINCT e2.scores) + 1 AS position
FROM examination e1
LEFT JOIN examination e2 ON e2.scores > e1.scores
GROUP BY e1.id, e1.scores
ORDER BY e1.scores DESC;

-- Еще один вариант без оконных функций (через подзапрос)
SELECT 
    id,
    scores,
    (SELECT COUNT(DISTINCT scores) + 1 
     FROM examination e2 
     WHERE e2.scores > e1.scores) AS position
FROM examination e1
ORDER BY scores DESC;

-- Примечание:
-- RANK() дает одинаковый ранг для одинаковых баллов и пропускает следующие номера
-- DENSE_RANK() дает одинаковый ранг, но не пропускает номера
-- ROW_NUMBER() дает уникальные номера даже при равных балках
