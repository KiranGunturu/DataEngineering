TEP 1 )

WHERE AND HAVING
==================

WHERE: 

WHERE CLAUSE WILL GO TO THE EACH ROW AND CHECKS THEM INDIVIDUALLY AND CHECKS IF IT IS BEING SATISFIED

GIVE ME THE EMPLOTESS WHOS SALARY IS > 10000
============================================

SELECT *FROM EMP
WHERE SALARY>10000


GIVE ME THE DEPARTMENTS WHOS AVERAGE SALARY IS > 10000
=========================================================

SELECT DEPT_ID,AVG(SALARY) AS DEPT_AVG_SALARY
FROM EMP
GROUP BY DEPT_ID
HAVING AVG(SALARY) > 10000

WHEN YOU WANT TO APPLY BOTH
===========================

SELECT DEPT_ID,AVG(SALARY) 
FROM EMP
WHERE SALARY>10000
GROUP BY DEPT_ID
HAVING AVG(SALARY) > 10000

TIP 2)

CONVERT ROWS TO COLUMNS AND COLUMNS TO ROWS WITHOUT USING PIVOT
====================================================================

REFER WORD DOC FOR METADATA

PIVOT - USING SUM WITH CASE WHEN
===================================

SELECT 
EMP_ID,
SUM(CASE WHEN SALARY_COMPONENT = 'SALARY' THEN VAL END) AS SALARY,
SUM(CASE WHEN SALARY_COMPONENT = 'BONUS' THEN VAL END) AS BONUS,
SUM(CASE WHEN SALARY_COMPONENT = 'HIKE_PERCENT' THEN VAL END) AS HIKE
FROM EMP_COMPENSATION
GROUP BY EMP_ID


UNPIVOT
========

NOW STORE THE ABOVE QUERY RESULT INTO NEW TABLE SO WE WILL HAVE PIVOT DATA AND BY USING THAT TABLE WE CAN UNPIVOT IT


SELECT 
EMP_ID,
SUM(CASE WHEN SALARY_COMPONENT = 'SALARY' THEN VAL END) AS SALARY,
SUM(CASE WHEN SALARY_COMPONENT = 'BONUS' THEN VAL END) AS BONUS,
SUM(CASE WHEN SALARY_COMPONENT = 'HIKE_PERCENT' THEN VAL END) AS HIKE
INTO EMP_COMPENSATION_PIVOT
FROM EMP_COMPENSATION
GROUP BY EMP_ID



NOW LETS UNPIVOT   - USING UNION ALL
======================================


SELECT *FROM (
SELECT EMP_ID,'SALARY' AS SALARY_COMPONENT, SALARY AS VAL FROM EMP_COMPENSATION_PIVOT
UNION ALL
SELECT EMP_ID,'BONUS' AS SALARY_COMPONENT, BONUS AS VAL FROM EMP_COMPENSATION_PIVOT
UNION ALL
SELECT EMP_ID,'HIKE_PERCENT' AS SALARY_COMPONENT, HIKE_PERCENT AS VAL FROM EMP_COMPENSATION_PIVOT
)
ORDER BY EMP_ID



PIVOTING BASED ON PLAYERS LOCATION
===================================

SELECT
SUM(CASE WHEN CITY='BANGALORE' THEN NAME END) AS BANGALORE,
SUM(CASE WHEN CITY='MUMBAI' THEN NAME END) AS MUMBAI,
SUM(CASE WHEN CITY='DELHI' THEN NAME END) AS DELHI
FROM (
SELECT *,
ROW_NUMBER(), OVER(PARTITION BY CITY ORDER BY NAME ASC) AS PLAYER_ID
FROM PLAYER_LOCATIONS
)A
GROUP BY PLAYER_ID
ORDER BY PLAYER_ID


TIP 3 - TOP 10 INTERVIEW QUESTIONS
==================================

1) HOW TO FIND DUPLICATES IN A GIVEN TABLE

SELECT EMP_ID, COUNT(*) FROM EMP
GROUP BY EMP_ID
HAVING COUNT(*) > 1

2) HOW TO DELETE DUPLICATES FROM TABLE

WITH CTE AS (

SELECT *, ROW_NUMBER() OVER(PARTITION BY EMP_ID ORDER BY EMP_ID) AS RN
FROM EMP
)
DELETE FROM CTE WHERE RN>1

3) DIFFERENCE BETWEEN UNION AND UNION ALL

UNION - WILL COMBINE TWO DATASETS AND REMOVE DUPES

UNION ALL - IT WILL JUST COMBINE TWO DATASETS AND WILL NOT REMOVE ANY DUPES

4) DIFFERENCE BETWEEN ROW_NUMBER, RANK(), DENSE_RANK() ?

SELECT ID,NAME,DEPT_ID,SALARY,NAME,
RANK() OVER (PARTITION BY DEPT ORDER BY SALARY DESC) AS RNK,
DENSE_RANK() OVER (PARTITION BY DEPT ORDER BY SALARY DESC) AS DNK,
ROW_NUMBER() OVER (PARTITION BY DEPT ORDER BY SALARY DESC) AS RNUMCG
FROM EMP

DENSE_RANK() 

	IF THERE IS TIE THEN SAME RANK WILL BE ASSIGNED AND NEXT RANK NUMBER WILL NOT BE SKIPPED
	100 1
	100 1
	200 2
	
RANK()

	IF THERE IS TIE THEN SAME RANK WILL BE ASSIGNED AND NEXT RANK WILL BE SKIPPED
	
	100 1
	100 1
	200 3


5) EMPLOYEES WHO ARE NOT PRESENT IN DEPT TABLE?

	Joins
	===========

SELECT E.*, D.DEPT_ID FROM EMP E
LEFT JOIN DEPT D ON E.EMP_ID = D.EMP_ID
WHERE D.EMP_ID IS NULL

SUB-QUERY
==========

SELECT *FROM EMP WHERE DEPT_ID NOT IN (SELECT DEPT_ID FROM DEPT)

6) SECOND HIGHEST SALARY IN EACH DEPT


WITH CTE AS (
SELECT *,DENSE_RANK() OVER(PARTITION NY DEPT_ID ORDER BY SALARY DESC) AS RN
FROM EMP
)
SELECT *FROM CTE
WHERE RN > 2

7) FIND ALL TRANSACTIONS DONE BY SHILPA

SELECT *FROM ORDERS
WHERE UPPER(CUSTOMER_NAME) = 'SHILPA'

8) SELF JOIN EMP SALARY > MANAGER SALARY

9) JOINS 

10) SWAP THE GENDER

UPDATE ORDERS
SET GENDER = CASE WHEN GENDER = 'MALE' THEN 'FEMALE' 
		          WHEN GENDER = 'FEMALE' THEN 'MALE' 
				  END;
				  
TIP 4) 

SELF JOIN
==========

FIND THE EMPLOYESS WHOS SALARY IS HIGHER THAN MANAGER SALARY
=================================================================

EMP_ID	NAME SALARY MANAGER_ID

SELECT E.EMP_ID,E.SALARY AS EMP_SALARY,M.SALARY AS MANAGER_SALARY ,M.NAME AS MANAGER_NAME ,
FROM EMP E
JOIN EMP M ON E.MANAGER_ID = M.EMP_ID
WHERE E.SALARY > M.SALARY

MANAGERS MANAGER NAME (SENIOR MANAGER NAME)
=============================================

EMP_ID	NAME MANAGER_ID


SELECT E.EMP_ID,E.NAME AS EMP_NAME , M.EMP_NAME AS MANAGER_NAME, SM.NAME AS SENIOR_MANAGER_NAME
 FROM EMP E
LEFT JOIN EMP M ON E.MANAGER_ID = M.EMP_ID
LEFT JOIN EMP SM ON M.MANAGER_ID = SM.EMP_ID









JOINS
======


IF ALL KEYS ARE MATCHING THEN RESULT OF ALL JOINS WILL BE SAME

FULL OUTER : INNER JOIN + NON MATCHING RECORDS FROM LEFT AND RIGHT

CALCULATE MODE IN SQL
======================

MOST FREQUED VALUE IN THE TABLE


1,2,3,3,3,4,5,6,6,6 // 3,6

1,2,2,3,3,3,3,4,5 // 3

WITH CTE
============

WITH CTE AS (
SELECT ID,COUNT(*) AS FREQ FROM EMP GROUP BY ID
)
SELECT *FROM CTE 
WHERE FREQ = (SELECT MAX(FREQ) FROM CTE)


WITH RANK
===========


WITH CTE AS (
SELECT ID, COUNT(*) AS FREQ FROM EMP GROUP BY ID
)
SELECT *, RANK() OVER (ORDER BY FREQ DESC) AS RN FROM CTE
WHERE RN =1


ASSIGN RANK TO ONLY DUPLICATES
==============================

ID
a DUP1
a DUP1
b NULL
c DUP2
c DUP2
c DUP2
d DUP3
d DUP3
e NULL

WITH TRUE_DUPES 
AS (
SELECT ID FROM EMP GROUP BY ID HAVING COUNT(*) > 1)
,ASSIGN_RANKS 
AS (SELECT *, RANK() OVER (ORDER BY ID ASC) AS RN FROM TRUE_DUPES)

SELECT 
E.*,'DUP' + CAST(A.RN AS VARCHAR(20)) AS OUTPUT
FROM EMP E
LEFT JOIN ASSIGN_RANKS A ON E.ID = A.ID



CUSTOM SORT IN SQL
========================



SELECT *FROM HAPPINESS_INDEX 
ORDER BY 
CASE WHEN COUNTRY='India' then 3
	WHEN COUNTRY='Pakistan' then 2
	WHEN COUNTRY='UK' then 1
	ELSE 0 
	END AS COUNTRIES_DERIVED DESC, HAPPINESS_INDEX_2021 DESC
	
	

MASTER UPDATE
======================

	UPDATE QUERY FOR SINGLE VALUE UPDATE
	=====================================
	
	UPDATE EMP
	SET EMP_NAME = 'HELLO'
	
	
	UPDATE QUERY WITH WHERE CLAISE
	=====================================
	
	UPDATE EMP
	SET EMP_NAME = 'HELLO'
	WHERE EMP_ID = 5678

	UPDATE QUERY FOR MULTI VALUE UPDATE
	=====================================
	
	UPDATE EMP
	SET EMP_NAME = 'HELLO',
		SALARY = 10000
		
	UPDATE WITH CONSTANT VALUES AND DERIVATIONS (COL CALCULATIONS / USING CASE WHEN)
	================================================================================
	
	// INCREASE  BY 1000
	
	UPDATE EMP
	SET EMP_SALARY = SALARY + 1000
	
	
	//INCREASE BY 10%
	
    UPDATE EMP
	SET EMP_SALARY = SALARY * 1.1
	
	// CASE STATEMENT 
	
		//INCREASE SALARY BY 10% FOR DEPT_ID = 100 AND 20% TO DEPT = 200
	
	UPDATE EMP
	SET SALARY = CASE WHEN DEPT_ID = 100 THEN SALARY * 1.1
					WHEN DEPT_ID = 200 THEN SALARY * 1.2
					ELSE SALARY END
					
					
	UPDATE WITH JOIN
	====================
	
	UPDATE EMP
	SET DEPT_NAME = D.DEP_NAME
	FROM EMP E
	INNER JOIN DEPT D ON E.DEP_ID = D.DEPT_ID


	UPDATE INTERVIEW QUESTIONS
	=============================
	
	UPDATE EMP
	SET GENDER = CASE WHEN GENDER = 'Male' then 'Female' else 'Male' END
	
	
	
ALL ABOUT AGGREGATIONS
==============================


CREATE TABLE int_orders(
 order_number int NOT NULL,
 order_date date NOT NULL,
 cust_id int NOT NULL,
 salesperson_id int NOT NULL,
 amount floaT NOT NULL
) 



INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (30, TO_DATE('1995-07-14' , 'YYYY-MM-DD'), 9, 1, 460);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (10, TO_DATE('1996-08-02' ,'YYYY-MM-DD'), 4, 2, 540);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (40, TO_DATE('1998-01-29' ,'YYYY-MM-DD'), 7, 2, 2400);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (50, TO_DATE('1998-02-03' ,'YYYY-MM-DD'), 6, 7, 600);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (60, TO_DATE('1998-03-02' ,'YYYY-MM-DD'), 6, 7, 720);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (70, TO_DATE('1998-05-06' ,'YYYY-MM-DD'), 9, 7, 150);
INSERT INTO int_orders (order_number, order_date, cust_id, salesperson_id, amount) VALUES (20, TO_DATE('1999-01-30' ,'YYYY-MM-DD'), 4, 8, 1800);

select sum(amount) from int_orders;

select salesperson_id, sum(amount) from int_orders
group by salesperson_id4

// sum everything in the table ( as we did not give anything in over then our window is full table)

select salesperson_id,order_number,order_date,amount,
sum(amount) over()
from int_orders

//calculate sum (amount ) for each partition


select salesperson_id,order_number,order_date,amount,
sum(amount) over(partition by salesperson_id)
from int_orders


//running sum in the total table


select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date)
from int_orders

or 

select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date rows between unbounded preceding and current row)
from int_orders


//running sum for each partition


select salesperson_id,order_number,order_date,amount,
sum(amount) over(partition by salesperson_id order by order_date)
from int_orders


//rolling sum of previous two rows and current row


select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date rows between 2 preceding and current row)
from int_orders


/rolling sum of 2 preceding and 1 preceding (first row will get null as it is not considering the current row)

select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date rows between 2 preceding and 1 preceding)
from int_orders


// partition level


select salesperson_id,order_number,order_date,amount,
sum(amount) over(partition by salesperson_id order by order_date rows between 1 preceding and current row)
from int_orders


//lag

select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date rows between 1 preceding and 1 preceding)
from int_orders


//lead

select salesperson_id,order_number,order_date,amount,
sum(amount) over(order by order_date rows between 1 following and 1 following)
from int_orders

remove revere pairs
=====================

select t1.a, t1.b from number_pairs t1
left join number_pairs t2 on t1.b = t2.a and t1.a = t2.b
where t2.a is null or t1.a < t2.a

student marks invert - pivot
==============================

student_id,subject,		marks
1001		english		88
1001		science		90
1001		maths		85
1002		english		70
1002		science		80
1002		maths		83
TO
student_id english science maths
1001		88		90		85
1002		70		80		83

select student_id,
sum(case when subject='english' then marks else 0 end) as english,
sum(case when subject='science' then marks end) as science,
sum(case when subject='maths' then marks end) as maths
from students
group by student_id

ungrouping the DATA
====================

with recursive cte as 
	(select id,item_name, total_count
	from travel_items
	UNION
	select cte.id,cte.name, cte.total_count-1
	from cte
	join travel_items t on t.item_name = cte.item_name and t.id = cte.ID
	where cte.total_count > 1
	)
select id, item_name
from cte
group by id;

fill blank VALUES
=================
with cte1 as (
select *,
row_number() over(order by select null) as rn
from brands
)
,cte2 as (
select *,
lead(rn,1,9999) over(order by rn) as next_rn
from cte1
where category is not null
)
select cte2.category, cte1.brand_name
from cte1
inner join cte2 on cte1.rn >= cte2.rn and cte1.rn <= cte.next_rn-1


multiple rows to single column with comma SEP
===============================================
input
========
ID	name
1   emp1
2   emp2
3   emp3
4   emp4
5   emp5
6   emp6
7   emp7
8   emp8

output
========
1 emp1,2 emp2
3 emp3,4 emp4
5 emp5,6 emp6
7 emp7,8 emp8

with cte as (
select CONCAT(id, ' ',name) as name,
ntile(4) over(order by id) as buckets
from emp_input
)
select string_agg(name,', ') as final_result
from cte
group by buckets
order by 1

exchange seats
===============
i/p
====
ID	Student
1	Abbot
2	Doris
3	Emerson
4	Green
5	Jeames

o/p
====
ID	Student
1	Doris
2	Abbot
3	Green
4	Emerson
5	Jeames


mySQL
======
with cte as (
select *,
lead(id) over(order by id) as next,
lag(id) over(order by id) as prev
from seats
)
select 
case when ((id % 2 = 1) and next is not null) then next
when (id % 2 = 0) then prev
else id
end as id, student
from cte
order by id


Not boring Movies
=================

SELECT 
    *
from Cinema
where mod(id,2)<>0  and description!='boring'
order by rating desc;

find customer referee
=====================

select 
    name 
from Customer
where referee_id!=2 or referee_id is null

Monthly merchant balance
=========================
cumulative sum of every day in a month and reset at every month
with cte as(
select 
transaction_date::date as transaction_date,
sum(case when type='withdrawal' then -1*amount else amount end) as amount
from transactions
group by transaction_date::date
order by transaction_date::date
)
select 
transaction_date,
--amount,
sum(amount) over(partition by extract(year from transaction_date, extract(month from transaction_date) order by transaction_date) as cum_sum
from cte

Actor and DIRECTOR
====================

select 
    actor_id, 
    director_id
from ActorDirector
group by actor_id, director_id
having count(actor_id) >=3

Reformat dep TABLE
===================

select
id,
sum(case when month='Jan' then revenue end) as Jan_Revenue,
sum(case when month='Feb' then revenue end) as Feb_Revenue,
sum(case when month='Mar' then revenue end) as Mar_Revenue,
sum(case when month='Apr' then revenue end) as Apr_Revenue,
sum(case when month='May' then revenue end) as May_Revenue,
sum(case when month='Jun' then revenue end) as Jun_Revenue,
sum(case when month='Jul' then revenue end) as Jul_Revenue,
sum(case when month='Aug' then revenue end) as Aug_Revenue,
sum(case when month='Sep' then revenue end) as Sep_Revenue,
sum(case when month='Oct' then revenue end) as Oct_Revenue,
sum(case when month='Nov' then revenue end) as Nov_Revenue,
sum(case when month='Dec' then revenue end) as Dec_Revenue
from 
Department
group by id

Article Views
==============

select distinct author_id as id
from Views
where author_id = viewer_id
order by id 

customers who visited but did not make any transactions
=============================================================

select 
    v.customer_id,
    count(v.customer_id) as count_no_trans
    from 
    Visits v
    left join Transactions T
    on v.visit_id = T.visit_id
    where T.visit_id is null
    group by v.customer_id
    order by count_no_trans desc

Game play Analysis
===================
1) find the players who logged in for the first time

select player_id, min(event_date) as first_login
from Activity
group by player_id

2) find the device_ids when they logged in for the TIME

with cte as (
select 
device_id,
rank() over(partition by player_id order by event_date) as rn
from Activity
)
select device_id
from cte
where rn=1

3) cumulative sum of games played by each player

select 
*,
sum(games_played) over(partition by player_id order by event_date) as cum_sum
from Activity

4) players who logged in for the first time and again the next DAY

with min_date as (
select 
player_id,
min(event_date) as first_logged
from
activity
group by player_id
)
select
a.*,first_logged
from activity a
inner join min_date md on a.player_id = md.player_id
where datediff(day,first_logged,event_date)=1

calculate special bonus
========================

select 
    employee_id,
    case when employee_id%2=1 and name not like 'M%' then salary else 0 end as bonus
from Employees
order by 1

patients with condition
========================


select
	patient_id,
	patient_name,
	conditions
from Patients
where conditions like 'DIAB1%' OR conditions LIKE '% DIAB1%'

same dept and same salary employess
====================================

with cte as (
select 
	dept_id
	salary
from EMP
group by dept_id,salary
having count(1)>1
)
select *
from emp
inner join cte on cte.dept_id = emp.dept_id and cte.salary = emp.salary

third highest salary in each dept and if there are less than 3 employess then return emp details with lowest salary in that emp
================================================================================================================================

with cte as (
select 
	*,
	DENSE_RANK() over(partition by dept_id order by salary desc) as rn,
	count(1) over(partition by dept_id) as dept_count
from 
EMP 
)
select *from cte where rn=3 or (dept_count <3 and rn=dept_count)

query to return second most recent activity per user. if there is only activity per user then return the same
===============================================================================================================
with cte as (
select 
	*,
	row_number() over(partition by username order by startdate) as rn,
	count(1) over(partition by username order by startdate rows between unbounded preceding and unbounded following) as total_count
	from user_activity
)
select *from cte
where rn = case when total_count=1 then 1 else total_count -1 end;

find the max amount for each salesperson_id
==============================================

select 
	a.order_number,a.order_date,a.cust_id,a.salesperson_id.a.amount
from orders a
left join orders b on a.salesperson_id = b.salesperson_id
group by a.order_number,a.order_date,a.cust_id,a.salesperson_id.a.amount
having a.amount >= max(b.amount)


DDL
====

CREATE
ALTER
DROP
TRUNCATE

DML
====
INSERT
UPDATE
DELETE
CALL
LOCK
EXPLAIN CALL

TCL
====

COMMIT
ROLLBACK
SAVEPOINT
SET TRANSACTION

DQL
====

SELECT

DCL
====

GRANT
REVOKE








































