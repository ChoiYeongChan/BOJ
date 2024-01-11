-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
from ANIMAL_OUTS
group by HOUR(DATETIME)
having hour<=19 and hour>=9
order by HOUR