SELECT a.PRODUCT_ID, a.PRODUCT_NAME, sum(a.PRICE*b.AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT a
join FOOD_ORDER b
on a.PRODUCT_ID=b.PRODUCT_ID
where month(b.PRODUCE_DATE)=5
group by PRODUCT_ID
order by TOTAL_SALES desc, a.PRODUCT_ID