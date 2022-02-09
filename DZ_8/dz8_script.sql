use vk;
-- 1

select u2.firstname,u2.lastname , count(*)
from users u
join messages m on m.to_user_id =u.id
join users u2 on m.from_user_id = u2.id
where u.id= 44
group by u2.id
limit 1;

--  from dz6
select count(*) as count_message, 
	concat((select firstname from users where id = from_user_id),' ' , (select lastname from users where id = from_user_id)) as name_sender ,
	concat((select firstname from users where id = 44),' ' , (select lastname from users where id = 44)) as name_receiver	
from messages where to_user_id = 44 group by from_user_id limit 1;


-- 2

select count(*)
from likes l 
join profiles p  on l.user_id = p.user_id 
where TIMESTAMPDIFF(year,p.birthday,now()) < 10;

-- from dz6
select count(*)  from likes where user_id in (select user_id from profiles  where timestampdiff(year,birthday, now()) < 10 ) ;

-- 3

select p.gender , count(*)
from likes l 
join profiles p  on l.user_id = p.user_id 
group by p.gender
limit 1;

-- from dz6

select if((select count(*) from likes where user_id in (select user_id from profiles  where gender  = 'M' )) > (select count(*) 
from likes where user_id in (select user_id from profiles  where gender  = 'F' )) ,
'Больше лайков у М', 'Больше лайков у F');
