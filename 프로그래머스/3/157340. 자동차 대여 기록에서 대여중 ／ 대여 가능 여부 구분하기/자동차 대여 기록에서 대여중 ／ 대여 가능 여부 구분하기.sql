SELECT CAR_ID, max( CASE
WHEN '2022-10-16' between START_DATE and END_DATE THEN '대여중'
ELSE '대여 가능'
END) as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC