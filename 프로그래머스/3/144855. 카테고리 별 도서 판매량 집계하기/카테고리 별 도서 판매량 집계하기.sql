SELECT B.CATEGORY as CATEGORY, SUM(S.SALES) as TOTAL_SALES
FROM BOOK B JOIN (
SELECT BOOK_ID, SALES_DATE, SALES
    FROM BOOK_SALES
    WHERE year(SALES_DATE)=2022 and month(SALES_DATE)=1
) S ON B.BOOK_ID=S.BOOK_ID
GROUP BY B.CATEGORY
-- WHERE year(S.SALES_DATE)=2022 and month(S.SALES_DATE)=1
ORDER BY CATEGORY