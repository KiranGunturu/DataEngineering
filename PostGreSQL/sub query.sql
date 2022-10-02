sub query
==========

find employees whos salary is more than the average salary earned by all employees

two parts
==========
1) find the avg salary
	select avg(salary) from emp;
2) filter the employees based on the above result
	select *from emp where salary

now combine two parts

select * -- outer query
from emp 
where salary > (select avg(salary) from emp); -- sub query / inner query

types
=====

scalar
multiple ROW
corelated 

scalar subquery
===============
it always returns one row and one column

select avg(salary) from emp

OR

select *
from emp e
inner join (select avg(salary) as sal from from emp) avg_sal
on e.salary > avg_sal.sal

multiple row subquery
======================
two types
=========
	-- sub query returns multiple column and multiple ROW

	
	find the employees who earn the highest salary in each dept?

	--sub query
	select dept_name, max(salary)
	from 
	emp
	group by dept_name

	-- outer and sub
	select *
	from 
	emp
	where (dept_name,salary) in (select dept_name, max(salary)
								from 
								emp
								group by dept_name)
						
	-- sub query returns single column and multiple ROW
	
	select *
	from 
	emp
	where  dept_name not in (select distinct dept_name from emp)

in above two cases (scalar and multiple row) sub query is not dependent on outer query
meaning we can execute just the sub query without having any dependency on the outer query

and also sub query is executed only once.
		
correlated sub query
=====================

sub query which is related to the outer query

find the employess in each dept who earn more than the avg salary in that dept

select avg(salary)
from 
emp
where dept_name = "specific dept"

select *
FROM
emp e1
where salary > (select avg(salary)
				from 
				emp e2
				where e2.dept_name = e1.dept_name
				)
				
this means sub query will get executed for every row in the outer query
and we can't alone execute the sub query as some of its values are dependent on outer query




		












 