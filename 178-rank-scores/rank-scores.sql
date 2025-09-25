# Write your MySQL query statement below
select s.score , count(d.score) as "rank"
from Scores s , (select distinct score from Scores) d
where s.score<=d.score
group by s.id
order by s.score desc;