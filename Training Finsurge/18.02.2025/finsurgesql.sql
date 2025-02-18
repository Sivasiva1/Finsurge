use finsurge
/*DDL Commands */
create table Interns (
	intern_id int auto_increment primary key,
    intren_names varchar(20),
    phone_no long,
    designation varchar(20),
    salary double
); 
#alter 
alter table Interns add column(City varchar(20));
#rename 
alter table interns rename column phone_no to phone;

/*DML Commands*/ 
#insert 
insert into interns(intren_names, phone_no, designation,salary) values("siva",8667244667,"python intern",10000);

insert into interns values(4,"santhosh",12345678,"java intern",10000);
#delete 
delete  from interns where intern_id = 4;
#update 
SET SQL_SAFE_UPDATES = 0;
update interns set city ="chennai" where city is null ; 
insert into interns values(default,"santhosh",12345678,"java intern",10000,"madurai");
insert into interns values(default,"mani",4276235962,"java intern",10000,"trichy");
insert into interns values(default,"bala",7498173198,"java intern",10000,"tirunelveli");
insert into interns values(default,"karthi",74987321,"java intern",10000,"babanasam");
/*DQL Commands */ 
select * from interns;
select distinct( intren_names) from interns;
select count(*) from interns;
select sum(salary) from interns;
select avg(salary) from interns;
select min(salary) from interns;
select max(salary) from interns;
select avg(salary),intren_names from interns group by intren_names; 
select salary from interns limit 2;
select * from interns order by intren_names;
select * from interns order by intren_names desc;
select avg(salary),intren_names from interns group by intren_names having intren_names = "siva";

select empname from dummy.employee union all select intren_names from finsurge.interns;
select empname from dummy.employee union  select intren_names from finsurge.interns;
explain select * from interns;
#sleep 
select sleep(2); 
select * FROM interns;
SELECT SLEEP(2), intern_id, intren_names, phone, designation, salary FROM interns;

/*Program Exceution Time */
explain select * from interns;
set profiling = 1 ; 
select * from interns ;
show profiles;
select now();
	select * from dummy.employee ;
select now(); 

/*joins*/
#inner join 
SELECT dummy.employee.empname, finsurge.interns.intren_names 
FROM finsurge.interns
INNER JOIN dummy.employee ON dummy.employee.id = finsurge.interns.intern_id;

#left join 
SELECT finsurge.interns.intren_names,finsurge.interns.salary 
FROM finsurge.interns
left JOIN dummy.employee ON dummy.employee.id = finsurge.interns.intern_id;


#right join 
SELECT dummy.employee.empname,dummy.employee.salary 
FROM  dummy.employee
right JOIN finsurge.interns ON dummy.employee.id = finsurge.interns.intern_id;
