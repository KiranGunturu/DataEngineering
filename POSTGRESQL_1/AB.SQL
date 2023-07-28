===User Shopping Sprees===
SELECT user_id
FROM transactions
group by user_id
having count(*) >=3
order by 1
===Users Thord Transaction===
with cte as (
SELECT *,
dense_Rank() over (PARTITION BY user_id order by transaction_date) as rn
FROM transactions
)
select user_id,spend,transaction_date
from cte
where rn=3
====First Transaction=====
with cte as (
select t.*,
row_number() over(PARTITION BY user_id order by transaction_date) as rn
from user_transactions t
)
select count(user_id)  as users
from cte c
where c.rn=1 and c.spend>50 
====Fill Client Missing Data===
with products_cte as (
SELECT *
FROM products
),
fill_na_cte as 
(
select *,
lead(product_id,1,9999) over (ORDER BY product_id) as fill_cycle
from cte1
where category is not null
)
select products_cte.product_id,
fill_na_cte.category,
products_cte.name
from products_cte
inner join fill_na_cte on products_cte.product_id >= fill_na_cte.product_id 
and products_cte.product_id <= fill_na_cte.fill_cycle-1


https://datatofish.com/left-right-substring-sql-server/

SQL LIKE
==========

'a%' - values starts with a
'%a' - values ends with a
'a%o' - values starts with a and end with o
'%or%' - values which may have or in any place of the string
'_r%' - values starts with r in the second position
'a_%' - values starts with a and are at least 2 chars in LENGTH
'a__%' - values starts with a and are at least 3 chars in LENGTH