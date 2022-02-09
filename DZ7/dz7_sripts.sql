use shop;
-- 0
desc orders ;
select * from orders;
select * from  users;
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
insert into orders values (default, (SELECT id FROM users ORDER BY RAND() LIMIT 1) , default ,default);
delete from orders  

-- 1 
delete from orders where user_id = 5 or user_id = 6;
select name from users where id in (select user_id from orders group by user_id);

-- 2

desc products  ;
desc catalogs ;

select * from products p ;
select * from  catalogs ;

select  p.name , c.name from products p
join 
catalogs c 
on p.catalog_id  = c.id;

-- 3 
create database avia;
use avia;

DROP TABLE IF exists flights;

create table flights(
id Serial primary key,
`from` varchar(120),
`to` varchar(120)
);

insert into flights(`from`,`to`) values 
('moscow', 'omsk'),
('novgorod', 'kazan'),
('irkutsk', 'moscow'),
('omsk', 'irkutsk'),
('moscow','kazan');

create  table cities(
label varchar(120),
name varchar (120)
);
select * from flights f ;
insert into cities values
('moscow','Москва'),
('irkutsk', 'Иркутск'),
('novgorod' , 'Новгород'),
('kazan', 'Казань'),
('Omsk','Омск');



select f.id , c.name ,c2.name
from flights f
join
cities c
on c.label = f.`from`
join cities c2
on c2.label = f.`to`
order by f.id;




