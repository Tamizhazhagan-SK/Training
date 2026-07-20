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




/* 
Name	Description
%, MOD	Modulo operator
*	Multiplication operator
+	Addition operator
-	Minus operator
-	Change the sign of the argument
/	Division operator



TRUNCATE()	Truncate to specified number of decimal places

CURDATE()	Return the current date
CURRENT_DATE(), CURRENT_DATE	Synonyms for CURDATE()
CURRENT_TIME(), CURRENT_TIME	Synonyms for CURTIME()
CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP	Synonyms for NOW()
CURTIME()	Return the current time
DATE()	Extract the date part of a date or datetime expression
DATE_ADD()	Add time values (intervals) to a date value
DATE_FORMAT()	Format date as specified

DATE_ADD()	Add time values (intervals) to a date value
DATE_FORMAT()	Format date as specified
DATE_SUB()	Subtract a time value (interval) from a date
DATEDIFF()	Subtract two dates
DAY()	Synonym for DAYOFMONTH()
DAYNAME()	Return the name of the weekday
DAYOFMONTH()	Return the day of the month (0-31)
DAYOFWEEK()	Return the weekday index of the argument
DAYOFYEAR()	Return the day of the year (1-366)
EXTRACT()	Extract part of a date
FROM_DAYS()	Convert a day number to a date


Name	Description
ADDDATE()	Add time values (intervals) to a date value
ADDTIME()	Add time
CONVERT_TZ()	Convert from one time zone to another
CURDATE()	Return the current date
CURRENT_DATE(), CURRENT_DATE	Synonyms for CURDATE()
CURRENT_TIME(), CURRENT_TIME	Synonyms for CURTIME()
CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP	Synonyms for NOW()
CURTIME()	Return the current time
DATE()	Extract the date part of a date or datetime expression
DATE_ADD()	Add time values (intervals) to a date value
DATE_FORMAT()	Format date as specified
DATE_SUB()	Subtract a time value (interval) from a date
DATEDIFF()	Subtract two dates
DAY()	Synonym for DAYOFMONTH()
DAYNAME()	Return the name of the weekday
DAYOFMONTH()	Return the day of the month (0-31)
DAYOFWEEK()	Return the weekday index of the argument
DAYOFYEAR()	Return the day of the year (1-366)
EXTRACT()	Extract part of a date
FROM_DAYS()	Convert a day number to a date
FROM_UNIXTIME()	Format Unix timestamp as a date
GET_FORMAT()	Return a date format string
HOUR()	Extract the hour
LAST_DAY	Return the last day of the month for the argument
LOCALTIME(), LOCALTIME	Synonym for NOW()
LOCALTIMESTAMP, LOCALTIMESTAMP()	Synonym for NOW()
MAKEDATE()	Create a date from the year and day of year
MAKETIME()	Create time from hour, minute, second
MICROSECOND()	Return the microseconds from argument
MINUTE()	Return the minute from the argument
MONTH()	Return the month from the date passed
MONTHNAME()	Return the name of the month
NOW()	Return the current date and time
PERIOD_ADD()	Add a period to a year-month
PERIOD_DIFF()	Return the number of months between periods
QUARTER()	Return the quarter from a date argument
SEC_TO_TIME()	Converts seconds to 'hh:mm:ss' format
SECOND()	Return the second (0-59)
STR_TO_DATE()	Convert a string to a date
SUBDATE()	Synonym for DATE_SUB() when invoked with three arguments
SUBTIME()	Subtract times
SYSDATE()	Return the time at which the function executes
TIME()	Extract the time portion of the expression passed
TIME_FORMAT()	Format as time
TIME_TO_SEC()	Return the argument converted to seconds
TIMEDIFF()	Subtract time
TIMESTAMP()	With a single argument, this function returns the date or datetime expression; with two arguments, the sum of the arguments
TIMESTAMPADD()	Add an interval to a datetime expression
TIMESTAMPDIFF()	Return the difference of two datetime expressions, using the units specified
TO_DAYS()	Return the date argument converted to days
TO_SECONDS()	Return the date or datetime argument converted to seconds since Year 0
UNIX_TIMESTAMP()	Return a Unix timestamp
UTC_DATE()	Return the current UTC date
UTC_TIME()	Return the current UTC time
UTC_TIMESTAMP()	Return the current UTC date and time
WEEK()	Return the week number
WEEKDAY()	Return the weekday index
WEEKOFYEAR()	Return the calendar week of the date (1-53)
YEAR()	Return the year
YEARWEEK()	Return the year and week

Name	Description
ASCII()	Return numeric value of left-most character
BIN()	Return a string containing binary representation of a number
BIT_LENGTH()	Return length of argument in bits
CHAR()	Return the character for each integer passed
CHAR_LENGTH()	Return number of characters in argument
CHARACTER_LENGTH()	Synonym for CHAR_LENGTH()
CONCAT()	Return concatenated string
CONCAT_WS()	Return concatenate with separator
ELT()	Return string at index number
EXPORT_SET()	Return a string such that for every bit set in the value bits, you get an on string and for every unset bit, you get an off string
FIELD()	Index (position) of first argument in subsequent arguments
FIND_IN_SET()	Index (position) of first argument within second argument
FORMAT()	Return a number formatted to specified number of decimal places
FROM_BASE64()	Decode base64 encoded string and return result
HEX()	Hexadecimal representation of decimal or string value
INSERT()	Insert substring at specified position up to specified number of characters
INSTR()	Return the index of the first occurrence of substring
LCASE()	Synonym for LOWER()
LEFT()	Return the leftmost number of characters as specified
LENGTH()	Return the length of a string in bytes
LIKE	Simple pattern matching
LOAD_FILE()	Load the named file
LOCATE()	Return the position of the first occurrence of substring
LOWER()	Return the argument in lowercase
LPAD()	Return the string argument, left-padded with the specified string
LTRIM()	Remove leading spaces
MAKE_SET()	Return a set of comma-separated strings that have the corresponding bit in bits set
MATCH()	Perform full-text search
MID()	Return a substring starting from the specified position
NOT LIKE	Negation of simple pattern matching
NOT REGEXP	Negation of REGEXP
OCT()	Return a string containing octal representation of a number
OCTET_LENGTH()	Synonym for LENGTH()
ORD()	Return character code for leftmost character of the argument
POSITION()	Synonym for LOCATE()
QUOTE()	Escape the argument for use in an SQL statement
REGEXP	Whether string matches regular expression
REGEXP_INSTR()	Starting index of substring matching regular expression
REGEXP_LIKE()	Whether string matches regular expression
REGEXP_REPLACE()	Replace substrings matching regular expression
REGEXP_SUBSTR()	Return substring matching regular expression
REPEAT()	Repeat a string the specified number of times
REPLACE()	Replace occurrences of a specified string
REVERSE()	Reverse the characters in a string
RIGHT()	Return the specified rightmost number of characters
RLIKE	Whether string matches regular expression
RPAD()	Append string the specified number of times
RTRIM()	Remove trailing spaces
SOUNDEX()	Return a soundex string
SOUNDS LIKE	Compare sounds
SPACE()	Return a string of the specified number of spaces
STRCMP()	Compare two strings
SUBSTR()	Return the substring as specified
SUBSTRING()	Return the substring as specified
SUBSTRING_INDEX()	Return a substring from a string before the specified number of occurrences of the delimiter
TO_BASE64()	Return the argument converted to a base-64 string
TRIM()	Remove leading and trailing spaces
UCASE()	Synonym for UPPER()
UNHEX()	Return a string containing hex representation of a number
UPPER()	Convert to uppercase
WEIGHT_STRING()	Return the weight string for a string
Table 14.15 Cast Functions and Operators

Name	Description	Deprecated
BINARY	Cast a string to a binary string	Yes
CAST()	Cast a value as a certain type	
CONVERT()	Cast a value as a certain type	
*/








































