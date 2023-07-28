------------Consecutive Numbers--------------

CREATE TABLE TABLEFOUR ( id int,value int);

INSERT INTO TABLEFOUR VALUES (1,1);
INSERT INTO TABLEFOUR VALUES (2,1);
INSERT INTO TABLEFOUR VALUES (3,1);
INSERT INTO TABLEFOUR VALUES (4,2);
INSERT INTO TABLEFOUR VALUES (5,1);
INSERT INTO TABLEFOUR VALUES (6,2);
INSERT INTO TABLEFOUR VALUES (7,3);
INSERT INTO TABLEFOUR VALUES (8,3);
INSERT INTO TABLEFOUR VALUES (9,3);
INSERT INTO TABLEFOUR VALUES (10,2);

COMMIT;

SELECT *FROM TABLEFOUR;


SELECT A.VALUE 
FROM TABLEFOUR A JOIN TABLEFOUR B ON A.ID = B.ID+1 AND A.VALUE=B.VALUE
JOIN TABLEFOUR C ON A.ID=C.ID+2 AND A.VALUE = C.VALUE;

--------------------- duplicate email ids  ---------------------

CREATE TABLE TABLEFIVE ( id int,email varchar(30));

insert into tablefive values (1,'ab@gmail.com');
insert into tablefive values (2,'bc@gmail.com');
insert into tablefive values (1,'ab@gmail.com');

commit;

select *from tablefive;


select email from tablefive group by email having count(email) >1 ;

select email from (select email,count(email) as cnt from tablefive group by email)t where t.cnt>1;

----------customers who never oorder---------


create table wnoc (id int , name varchar(10));
insert into wnoc values (1,'Joe');
insert into wnoc values (2,'Henry');
insert into wnoc values (3,'Sam');
insert into wnoc values (4,'Max');
commit;

select *From wnoc;

create table wnoo (id int,cid int);
insert into wnoo values (1,3);
insert into wnoo values (2,1);
commit;

select a.name from WNOC a
left join wnoo b on a.id=b.cid
where b.cid is null;

select id from wnoo where id not in (Select cid from wnoo)


---------- HARD TOTAL SALES BY YEAR ---

create table sales (
product_id int,
period_start date,
period_end date,
average_daily_sales int
);

insert into sales values(1,TO_DATE('2019-01-25','YYYY-MM-DD'),TO_DATE('2019-02-28','YYYY-MM-DD'),100);
insert into sales values(2,TO_DATE('2018-12-01','YYYY-MM-DD'),TO_DATE('2020-01-01','YYYY-MM-DD'),10);
insert into sales values(3,TO_DATE('2019-12-01','YYYY-MM-DD'),TO_DATE('2020-01-31','YYYY-MM-DD'),1);

with r_cte (dates,max_date)as (
select min(period_start) as dates, max(period_end) as max_date from sales
union all
select dates+1 as dates,max_date from r_cte
where dates<max_date
)
select product_id,extract(year from dates) as reporting_year,sum(average_daily_sales) as total_amount from r_cte
inner join sales on dates between PERIOD_START and PERIOD_END
group by product_id,extract(year from dates)
order by product_id,extract(year from dates);

----------------------- SCD2 --------------------

CREATE TABLE EMP_S (
id int,
name varchar(50),
salary varchar(10),
check_sum varchar(10)
);

INSERT INTO EMP_S VALUES (10,'James',10000,'ABCD');
INSERT INTO EMP_S VALUES (20,'Michael',20000,'EFGH');

--step 2:

INSERT INTO EMP_S VALUES (30,'Krish',30000,'IJKL');

--step 3:
INSERT INTO EMP_S VALUES (20,'Michael',20000,'EFGH');

UPDATE EMP_S
SET NAME = 'Mary',
check_sum = 'DUMMY'
where id = 20;

TRUNCATE TABLE EMP_S;

COMMIT;

SELECT *fROM EMP_S;


CREATE TABLE EMP_T (
row_seq int,
id int,
name varchar(50),
salary varchar(10),
check_sum varchar(10)
);

INSERT INTO EMP_T VALUES (1,10,'James',10000,'ABCD');
INSERT INTO EMP_T VALUES (2,20,'Michael',20000,'EFGH');

--find out the inserts

SELECT *FROM EMP_S S
LEFT JOIN EMP_T T ON S.ID=T.ID
WHERE T.ROW_SEQ IS NULL ;
--WHERE T.ID IS NULL OR T.NAME IS NULL OR T.SALARY IS NULL OR T.CHECK_SUM IS NULL
--WHERE T.ID IS NULL 





-- find out both inserts and updates

SELECT *FROM EMP_S S
LEFT JOIN EMP_T T ON S.ID=T.ID
WHERE T.ROW_SEQ IS NULL OR S.CHECK_SUM <> T.CHECK_SUM;

DROP TABLE EMP_S;

DROP TABLE EMP_T;










