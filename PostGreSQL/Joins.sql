CREATE TABLE TABLEONE (
ID INT,
DESCRIPTION VARCHAR2(30)
);


CREATE TABLE TABLETWO (
ID INT,
DESCRIPTION VARCHAR2(30)
);


INSERT INTO TABLEONE VALUES (1,'TEST1');
INSERT INTO TABLEONE VALUES (2,'TEST2');
INSERT INTO TABLEONE VALUES (3,'TEST3');
INSERT INTO TABLEONE VALUES (4,'TEST4');
INSERT INTO TABLEONE VALUES (5,'TEST5');
INSERT INTO TABLEONE VALUES (6,'TEST11');

COMMIT;

SELECT *FROM TABLEONE;


INSERT INTO TABLETWO VALUES (1,'TEST6');
INSERT INTO TABLETWO VALUES (2,'TEST7');
INSERT INTO TABLETWO VALUES (3,'TEST8');
INSERT INTO TABLETWO VALUES (4,'TEST9');
INSERT INTO TABLETWO VALUES (5,'TEST10');
INSERT INTO TABLETWO VALUES (7,'TEST12');

--INNER

SELECT *FROM TABLEONE A
INNER JOIN TABLETWO B ON A.ID = B.ID;

--LEFT
SELECT *FROM TABLEONE A
LEFT JOIN TABLETWO B ON A.ID = B.ID;

--RIGHT
SELECT *FROM TABLEONE A
RIGHT JOIN TABLETWO B ON A.ID = B.ID;

--FULL
SELECT *FROM TABLEONE A
FULL JOIN TABLETWO B ON A.ID = B.ID;

-- RECORDS FROM TABLEONE , WHICH ARE NOT THERE IN TABLETW0

SELECT *FROM TABLEONE A
LEFT JOIN TABLETWO B ON A.ID = B.ID
WHERE B.ID IS NULL;

-- RECORDS FROM TABLETWO, WHICH ARE NOT THERE IN TABLEONE
SELECT *FROM TABLEONE A
RIGHT JOIN TABLETWO B ON A.ID = B.ID
WHERE A.ID IS NULL;

-- RECORDS WHICH ARE UNIQUE TO BOTH TABLES
SELECT *FROM TABLEONE A
FULL JOIN TABLETWO B ON A.ID = B.ID
WHERE A.ID IS NULL OR B.ID IS NULL;

OR

SELECT *FROM TABLEA
MINUS/INTERSECT
SELECT *FROM TABLEB

-- CARTESIAN JOIN

SELECT *FROM TABLEONE A
INNER JOIN TABLETWO B ON 1=1;

--
SELECT *FROM TABLEONE NATURAL JOIN TABLETWO

===================
LEFT JOIN
===================

SELECT *FROM EMP
LEFT JOIN DEPT ON EMP.EMP_ID = DEP.DEP_ID AND DEP.DEPT_NAME = 'Analytics'

here all records from emp will be retreived and then and clause will be applied then the join

SELECT *FROM EMP
LEFT JOIN DEPT ON EMP.EMP_ID = DEP.DEP_ID 
WHERE DEP.DEPT_NAME = 'Analytics'

there join will be performed first and then the where clause will be applied.

==================

Join scenarios
================


All matching rows from two tables

t1
==
1
1

t2
==
1
1
1

Inner Join
===========
6 rows
left join
==========
matching + all from left
6
right join
==========
matching + all from right
6
full join
==========
matching + non matching from left + non matching from right
6
=====================================================================
t1
==
1
1
2

t2
==
1
1
1
3

we have one non matching in left and also in right

inner - 6
left - 6+1=7
right - 6+1=7
full - 6 + 1 + 1 = 8

=======================================================================

t1
==
1
1
2
2

t2
==
1
1
1
3
2

inner - 6 + 2 = 8
left - 6 + 2 = 8
right - 6 + 2 + 1 = 9
full - 6 + 2 + 1 = 9

=============================================================================

t1
==
1
1
2
2
4
null

t2
==
1
1
1
3
2
2
null

inner - 6 + 4 = 10
left - 6 + 4 + 1 + 1 = 12
right - 6 + 4 + 1 + 1 = 12
full - 6 + 4 + 1 + 1 + 1 + 1 = 14

===============================================================================

t1 has 5 records and t2 has 10 records
you can assume any values in each of the tables. how many max and min reocrds possible in in case of
inner, left, right and full

maximum
=========
	t1			
	===			
	1				
	1
	1
	1
	1

	t2
	===
	1				
	1
	1
	1
	1
	1				
	1
	1
	1
	1

inner - 50
left - 50
right - 50
full - 50

maximum
=========
	t1			
	===			
	1				
	1
	1
	1
	1

	t2
	===
	2				
	2
	2
	2
	2
	2				
	2
	2
	2
	2
	
inner  - 0
left - 5
right - 10
full - 0 + 5 + 10 = 15






