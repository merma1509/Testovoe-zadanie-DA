-- Задача 3: Покупки
-- Вывести ID клиентов, которые за последний месяц по всем своим счетам совершили покупок меньше, чем на 5000 рублей.
-- Без использования подзапросов и оконных функций.

CREATE TABLE account(
    id integer,        -- ID счета
    client_id integer, -- ID клиента
    open_dt date,      -- дата открытия счета
    close_dt date      -- дата закрытия счета
);

CREATE TABLE transaction(
    id integer,            -- ID транзакции
    account_id integer,    -- ID счета
    transaction_date date, -- дата транзакции
    amount numeric(10,2),  -- сумма транзакции
    type varchar(3)        -- тип транзакции
);

-- Решение через JOIN + GROUP BY + HAVING
SELECT DISTINCT a.client_id
FROM account a
JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
  AND t.type = 'PUR'  -- предполагаем, что покупки имеют тип 'PUR'
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;

-- Альтернативный вариант с использованием LEFT JOIN для включения клиентов без покупок
SELECT a.client_id
FROM account a
LEFT JOIN transaction t ON a.id = t.account_id 
    AND t.transaction_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
    AND t.type = 'PUR'
GROUP BY a.client_id
HAVING COALESCE(SUM(t.amount), 0) < 5000;

-- Вариант для PostgreSQL (синтаксис дат)
SELECT DISTINCT a.client_id
FROM account a
JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
  AND t.type = 'PUR'
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;

-- Вариант для MySQL с учетом разных типов транзакций
SELECT a.client_id
FROM account a
JOIN transaction t ON a.id = t.account_id
WHERE t.transaction_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)
  AND t.type IN ('PUR', 'BUY', 'SALE')  -- различные возможные типы покупок
GROUP BY a.client_id
HAVING SUM(CASE WHEN t.amount > 0 THEN t.amount ELSE 0 END) < 5000;

-- Объяснение логики:
-- 1. JOIN соединяет счета с транзакциями
-- 2. WHERE фильтрует транзакции за последний месяц и только покупки
-- 3. GROUP BY группирует по клиентам
-- 4. HAVING фильтрует клиентов с суммой покупок < 5000
-- 5. DISTINCT убирает дубликаты (если у клиента несколько счетов)

-- Примечания:
-- Предполагается, что тип транзакции для покупок может быть 'PUR', 'BUY' или подобным
-- Если все транзакции являются покупками, условие t.type можно убрать
-- Для точного решения нужно знать конкретные значения в поле type
