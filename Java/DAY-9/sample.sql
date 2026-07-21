-- --
-- /*CREATE TABLE EMPLOYEE (
--   ID INT PRIMARY KEY AUTO_increment,
--   NAME VARCHAR(20),
--   GENDER CHAR(1) CHECK (GENDER IN ('M', 'F')),
--   SALARY FLOAT,
--   DOB DATE
-- );
-- --
-- */
 
 
-- -- OUTPUT THE TABLE STRUCTURE
-- -- DESC EMPLOYEE;
 
 
-- -- -- INSERTING THE RECORDS TO EMPLOYEE TABLE
-- -- INSERT INTO EMPLOYEE(NAME, GENDER, SALARY, DOB) VALUES('Alice', 'F', 45000.0, '2001-09-11');
-- -- INSERT INTO EMPLOYEE(NAME, GENDER, SALARY, DOB) VALUES('Bob', 'F', 45000.0, '2002-12-31');
-- -- INSERT INTO EMPLOYEE(NAME, GENDER, SALARY, DOB) VALUES('Charles', 'M', 45000.0, '2003-06-08');
 
 
-- -- RETRIEVE ALL THE RECORDS
-- -- SELECT * FROM EMPLOYEE;

-- -- DROP TABLE EMPLOYEE;


-- CREATE TABLE PROFILE (
--     ID INT PRIMARY KEY,
--     NAME VARCHAR(20) NOT NULL,
--     GENDER CHAR(1) CHECK (GENDER IN ('M', 'F')),
--     PHONE BIGINT UNIQUE,
--     EMAIL VARCHAR(100) UNIQUE,
--     DOB DATE
-- );

-- INSERT INTO PROFILE (ID, NAME, GENDER, PHONE, EMAIL, DOB) VALUES
-- (1, 'Rajesh', 'M', 9876543210, 'raj@gmail.com', '1995-03-15'),
-- (2, 'Priya', 'F', 9876543211, 'pri@gmail.com', '1998-07-22'),
-- (3, 'Vikram', 'M', 9876543212, 'vik@gmail.com', '1992-11-08'),
-- (4, 'Sneha', 'F', 9876543213, 'sne@gmail.com', '2000-05-18'),
-- (5, 'Arjun', 'M', 9876543214, 'arj@gmail.com', '1997-09-25');



-- UPDATE PROFILE SET NAME = 'Arjunan' where ID = 5;

-- ALTER TABLE PROFILE ADD NOTES VARCHAR(100);

-- ALTER TABLE PROFILE ADD(SALARY INT, ISACTIVE BOOLEAN, LOCATION VARCHAR(20));

-- ALTER TABLE PROFILE MODIFY EMAIL VARCHAR(100) NOT NULL;

-- ALTER TABLE PROFILE MODIFY DOB INT;

-- ALTER TABLE PROFILE ADD CONSTRAINT GENDER CHECK (GENDER IN ('M', 'F','T'));

-- ALTER TABLE PROFILE 
--     DROP COLUMN LOCATION,
--     DROP COLUMN SALARY,
--     DROP COLUMN ISACTIVE,
--     DROP COLUMN NOTES;

-- SELECT * FROM PROFILE;

DROP TABLE IF EXISTS emp;

CREATE TABLE emp (
  empno decimal(4,0) NOT NULL,
  ename varchar(10) default NULL,
  job varchar(9) default NULL,
  mgr decimal(4,0) default NULL,
  hiredate date default NULL,
  sal decimal(7,2) default NULL,
  comm decimal(7,2) default NULL,
  deptno decimal(2,0) default NULL
);

DROP TABLE IF EXISTS dept;

CREATE TABLE dept (
  deptno decimal(2,0) default NULL,
  dname varchar(14) default NULL,
  loc varchar(13) default NULL
);

INSERT INTO emp VALUES ('7369','SMITH','CLERK','7902','1980-12-17','800.00',NULL,'20');
INSERT INTO emp VALUES ('7499','ALLEN','SALESMAN','7698','1981-02-20','1600.00','300.00','30');
INSERT INTO emp VALUES ('7521','WARD','SALESMAN','7698','1981-02-22','1250.00','500.00','30');
INSERT INTO emp VALUES ('7566','JONES','MANAGER','7839','1981-04-02','2975.00',NULL,'20');
INSERT INTO emp VALUES ('7654','MARTIN','SALESMAN','7698','1981-09-28','1250.00','1400.00','30');
INSERT INTO emp VALUES ('7698','BLAKE','MANAGER','7839','1981-05-01','2850.00',NULL,'30');
INSERT INTO emp VALUES ('7782','CLARK','MANAGER','7839','1981-06-09','2450.00',NULL,'10');
INSERT INTO emp VALUES ('7788','SCOTT','ANALYST','7566','1982-12-09','3000.00',NULL,'20');
INSERT INTO emp VALUES ('7839','KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,'10');
INSERT INTO emp VALUES ('7844','TURNER','SALESMAN','7698','1981-09-08','1500.00','0.00','30');
INSERT INTO emp VALUES ('7876','ADAMS','CLERK','7788','1983-01-12','1100.00',NULL,'20');
INSERT INTO emp VALUES ('7900','JAMES','CLERK','7698','1981-12-03','950.00',NULL,'30');
INSERT INTO emp VALUES ('7902','FORD','ANALYST','7566','1981-12-03','3000.00',NULL,'20');
INSERT INTO emp VALUES ('7934','MILLER','CLERK','7782','1982-01-23','1300.00',NULL,'10');

INSERT INTO dept VALUES ('10','ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES ('20','RESEARCH','DALLAS');
INSERT INTO dept VALUES ('30','SALES','CHICAGO');
INSERT INTO dept VALUES ('40','OPERATIONS','BOSTON');


show tables;


select count(*) from dept;
select count(*) from emp;

desc emp;

select "===================================================";

desc dept;

select "===================================================";

select upper('mercedes') as upper_case;
select lower('BMW') as lower_case;
select length('porsche') as length_check;

select "===================================================";


select replace('hail mary', 'h','j') as letter_replace;
select replace('Hello Me', 'Me','Everyone') as letter_replace;

select "===================================================";

select ename, lower(ename) as name, length(ename) as len from emp;

select concat('Vandu',' ','Murugan') as name;

select ename as Employees, sal from emp where empno between 7700 and 8000;

select empno, ename, sal from emp where ename like "S%"; 


select empno, ename, sal as crnt_sal, sal+(sal*0.10) as hike_salary, (sal+(sal*0.10))*96.43 as INR_rate from emp;

-- write a query where you replace the job with simple alternative names
-- example : clerk as assistant

SELECT
    empno,
    ename,
    CASE
        WHEN job = 'CLERK' THEN 'ASSISTANT'
        WHEN job = 'SALESMAN' THEN 'SALES EXECUTIVE'
        WHEN job = 'MANAGER' THEN 'TEAM LEAD'
        WHEN job = 'ANALYST' THEN 'DATA ANALYST'
        WHEN job = 'PRESIDENT' THEN 'CEO'
    END AS role_name,
    sal as crnt_sal, 
    sal+(sal*0.10) as hike_salary, 
    (sal+(sal*0.10))*96.43 as INR_rate
FROM emp;


SELECT ename, LEFT(ename,3) AS first_three_char FROM emp;

SELECT ename, RIGHT(ename,2) AS last_two_char FROM emp;

SELECT ename, SUBSTRING(ename,2,3) AS partial_name FROM emp;
-- the first field refers to the column, then the index and then the length upto n

SELECT ename, REPLACE(job,'MANAGER','LEAD') AS new_role FROM emp;

SELECT TRIM('   MERCEDES') AS trimmed_value;

SELECT ename, REVERSE(ename) AS reverse_name FROM emp;

SELECT ename, LPAD(ename,10,'*') AS pad_name FROM emp;

SELECT ename, RPAD(ename,10,'*') AS pad_name FROM emp;

SELECT ename, FORMAT(sal,2) AS format_salary FROM emp;

SELECT ename, ROUND(sal*1.15,0) AS revised_salary FROM emp;

SELECT ename, TRUNCATE(sal*1.15678,2) AS truncat_salary FROM emp;

SELECT empno, MOD(empno,2) AS odd_even_check FROM emp;

SELECT CURDATE() AS todays_date;

SELECT NOW() AS current_datetime;

SELECT ename, YEAR(hiredate) AS hire_year FROM emp;

SELECT ename, MONTHNAME(hiredate) AS hire_month FROM emp;

SELECT ename, DAYNAME(hiredate) AS hire_day FROM emp;

SELECT ename, DATEDIFF(CURDATE(),hiredate) AS days_worked FROM emp;

SELECT ename, DATE_FORMAT(hiredate,'%d-%b-%Y') AS formatted_hiredate FROM emp;
SELECT ename, DATE_FORMAT(hiredate,'%d-%M-%Y') AS formatted_hiredate FROM emp;
SELECT ename, DATE_FORMAT(hiredate,'%d-%m-%Y') AS formatted_hiredate FROM emp;


SELECT ename, TIMESTAMPDIFF(YEAR,hiredate,CURDATE()) AS experience FROM emp;

SELECT ename, DATE_ADD(hiredate,INTERVAL 1 YEAR) AS confirmation_date FROM emp;



select "__________________________________" as "************************************";
 
-- second max and min
select max(sal) as 'second max salary' from emp
    where sal < (select max(sal) from emp);
 
select "__________________________________" as "************************************";
 
-- alternative way to find the 2nd max using distinct and limit
select distinct sal from emp order by sal desc limit 1,1;
 
select "__________________________________" as "************************************";
 
-- alternative way to find the 3rd max using distinct and limit
-- limit 2, 1 means skip 1st 2 rows and retyrns the next row
select distinct sal from emp order by sal desc limit 2,1;
 
select "__________________________________" as "************************************";
 
-- write the query in an alternative way to find the 2nd and 3rd min sal
select distinct sal as 'second min salary' from emp order by sal asc limit 1,1;
 
select "__________________________________" as "************************************";
 
select distinct sal as 'third min salary' from emp order by sal asc limit 2,1;
 
select "__________________________________" as "************************************";
 
-- GROUP BY CLAUSE -  mainly used in aggregate function
select deptno, count(*) from emp group by deptno;

select "__________________________________" as "************************************";

-- Find employees who are more than company average
select ename, sal as 'more than average salary' from emp where sal > (select avg(sal) from emp); 

select "__________________________________" as "************************************";

-- Find employees who make more than at least one person in the department;
SELECT ename, sal as 'more than one person in dept', deptno FROM emp WHERE sal > ANY (SELECT sal FROM emp WHERE deptno = 30);

select "__________________________________" as "************************************";

-- Find employees who make more than every person in the department;
SELECT ename, sal 'more than every person in dept', deptno FROM emp WHERE sal > ALL (SELECT sal FROM emp WHERE deptno = 40);

select "__________________________________" as "************************************";

select e.ename, d.dname, d.loc
    from emp e left join dept d on e.deptno = d.deptno;

select "__________________________________" as "************************************";

select e.ename, d.dname, d.loc
    from emp e right join dept d on e.deptno = d.deptno;
 
-- inner join - shows only the matching results of 2 tables
 
select "______________________________" as "******************************";
 
 
-- left join : lists all the rows of left table and from the right table

-- lists only the matching rows
 
select empno, ename, sal, e.deptno, dname, loc

    from emp e LEFT JOIN dept d on e.deptno = d.deptno;
 
select "______________________________" as "******************************";
 
-- right join : lists all the rows of right table and from the left table lists

-- only the matching rows
 
select empno, ename, sal, e.deptno, dname, loc

    from emp e RIGHT JOIN dept d on e.deptno = d.deptno;
 
select "______________________________" as "******************************";

-- full join: lists all the rows of both the tables even unmatched rows
 
 
select "______________________________" as "******************************";

-- cross join: it is a cartesian product of both the tables; every row of a left table 

-- will have all the rows of right table

-- self join: it is to join the same table, eg- u have manager id which is an

-- employee id , for the employee you have to show the manager and manager name\
 
create table meals(name varchar(20), price double);

create table drinks(name varchar(20), price double);
 
insert into meals values('Veg Biryani', 200), ('Chicken Biryani', 250), ('Tandoori Roti', 40);

insert into drinks values('Lemonade', 50), ('Coke', 40), ('Iced tea', 70);

select * from meals;

select "______________________________" as "******************************";

select * from drinks;

-- cross-join

select "______________________________" as "******************************";

select m.name, m.price, RPAD(d.name,8,'*'), d.price, m.price + d.price as "Total Price" from meals m CROSS JOIN drinks d;
 



 








/*
SQL JOINS:

INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
SELF JOIN
CROSS JOIN


*/












































