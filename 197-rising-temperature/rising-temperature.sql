# Write your MySQL query statement below
SELECT w.id
FROM Weather w JOIN Weather t
On w.recordDate=DATE_ADD(t.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > t.temperature;