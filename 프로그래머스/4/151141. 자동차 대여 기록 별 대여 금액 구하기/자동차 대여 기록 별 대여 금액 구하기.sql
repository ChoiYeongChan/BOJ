WITH VALUE AS (SELECT C.DAILY_FEE, C.CAR_TYPE, H.HISTORY_ID, DATEDIFF(H.END_DATE,H.START_DATE)+1 as DAY,
CASE
WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1>=90 THEN '90일 이상'
WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1>=30 THEN '30일 이상'
WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1>=7 THEN '7일 이상'
ELSE 'NONE' END AS DURATION_TYPE
FROM CAR_RENTAL_COMPANY_CAR C INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID=H.CAR_ID
WHERE C.CAR_TYPE='트럭')

SELECT V.HISTORY_ID as HISTORY_ID, ROUND(V.DAILY_FEE*V.DAY*((100-IFNULL(P.DISCOUNT_RATE,0))/100)) as FEE
FROM VALUE V left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON V.CAR_TYPE=P.CAR_TYPE and V.DURATION_TYPE=P.DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC