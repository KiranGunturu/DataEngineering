-------------
CTE
-------------

This is to simplify the complex queries.

it improves the readability of a query.

order_id,order_date,order_customer_id,order_status
order_customer_id is the column which as how many orders each customer places


--give me total orders per customer

select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id

--give me avg orders placed by each customer

solution 1:using sub query

select avg(total_order_per_customer) from (
select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id
)x

solution 2 : using CTE or with clause

with total_orders (order_customer_id,total_order_per_customer) as (
select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id
)
select avg(total_order_per_customer) as avg_orders_per_customer from total_orders

subquery

query3(query2(query1))

CTE

query1

query2

query3

-- Want to find the premium customers who places more than the avg no of orders

--mathod 1 : subquery

select *from (select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id) total_orders
join
(select avg(total_order_per_customer) from (
select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id) x)average_orders
on total_orders.total_order_per_customer > average_orders.avg_orders_per_customer

--code redundancy
-- overhead as we end up calculating the results of same query multiple TIMESTAMP


--mathod 1 : CTE

1.calculate total orders per customer
2.calculate avg no of orders for the customers
3.get to know the customers who are premium


with total_orders (order_customer_id, total_order_per_customer) as (
select order_customer_id,count(*) as total_order_per_customer 
from orders
group order_customer_id),

avg_orders() as (
select avg(total_order_per_customer) as avg_orders_per_customer from total_orders)
select *from total_orders join avg_orders 
on total_orders.total_order_per_customer > avg_orders.avg_orders_per_customer

--CTE Defines temporary result set that you can refer IN select, insert, update, delete statements immediate that follows the CTE.
-- CTE can improve the performance but not always



