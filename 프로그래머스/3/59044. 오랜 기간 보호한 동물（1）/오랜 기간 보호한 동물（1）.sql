SELECT a.NAME, a.DATETIME
from ANIMAL_INS a
left join ANIMAL_OUTS b
on a.ANIMAL_ID=b.ANIMAL_ID
where b.ANIMAL_ID is NULL
order by a.DATETIME asc
limit 3