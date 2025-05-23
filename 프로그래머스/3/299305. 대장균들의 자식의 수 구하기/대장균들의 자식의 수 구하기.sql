-- 코드를 작성해주세요
SELECT A.ID as ID, IFNULL(B.CNT,0) as CHILD_COUNT
FROM ECOLI_DATA A left outer join (
    SELECT PARENT_ID, COUNT(*) as CNT
    FROM ECOLI_DATA
    GROUP BY PARENT_ID
    ) B ON A.ID=B.PARENT_ID
GROUP BY A.ID, B.CNT
ORDER BY ID ASC