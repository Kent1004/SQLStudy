use shop;


-- 1
update users set created_at = NOW(),updated_at = NOW();

-- 2
--  20.10.2017 8:10
alter table users change created_at Datetime default NOW();
show columns from users;
update ignore users set created_at = str_to_date(created_at , '%d.%m.%Y %H:%i');
show columns from users;
alter table users  Modify column created_at Datetime default NOW();

-- 3
select * from  storehouses_products;

insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,300);
insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,150);
insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,20);
insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,1110);
insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,0);
insert  into storehouses_products (storehouse_id,product_id,value) values (1,1,0);


select value from storehouses_products order by  value = 0 , value;

-- 4 
 
select name , birthday_at , 
( case  
   when month(birthday_at) = 5 then 'may'
  when month(birthday_at) = 8 then 'august'
  end) as birthday_month
 from users where month(birthday_at) = 5 or month(birthday_at) = 8 ;

-- 5

SELECT * FROM catalogs WHERE id IN (5, 1, 2) order by id = 5 DESC , id =1 DESC , id= 2 desc

-- 6

select name , timestampdiff (year, birthday_at,now()) as years from users;
select sum(timestampdiff (year, birthday_at,now()))/count(*) as average from users ;
select ROUND (AVG(timestampdiff (year, birthday_at,now())),1) as average2 from users ;

-- 7
select name , dayname(date_format(birthday_at, '2022-%m-%d')) as dayname from users

select  dayname(date_format(birthday_at, '2022-%m-%d')) as dayname1 , 
count(dayname(date_format(birthday_at, '2022-%m-%d'))) as count from users  group by dayname1


-- 8

SELECT exp(SUM(log(value))) product FROM (
values (1),(2),(3),(4),(5)
) X(value);


 