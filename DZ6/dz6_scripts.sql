use vk;

desc messages ;
 -- update messages set from_user_id = (SELECT id FROM users ORDER BY RAND() LIMIT 1);
-- update messages set to_user_id = (SELECT id FROM users ORDER BY RAND() LIMIT 1);
-- 1 
select count(*) as count_message, 
	concat((select firstname from users where id = from_user_id),' ' , (select lastname from users where id = from_user_id)) as name_sender ,
	concat((select firstname from users where id = 44),' ' , (select lastname from users where id = 44)) as name_receiver	
from messages where to_user_id = 44 group by from_user_id limit 1;

-- 2 

desc likes;

select count(*)  from likes where user_id in (select user_id from profiles  where timestampdiff(year,birthday, now()) < 10 ) ;

-- 3 
desc profiles;

select count(*) from profiles  where gender  = 'F';
select count(*) from profiles  where gender  = 'M';
select count(*)  from likes where user_id in (select user_id from profiles  where gender  = 'M' );
select count(*)  from likes where user_id in (select user_id from profiles  where gender  = 'F' )


select if((select count(*) from likes where user_id in (select user_id from profiles  where gender  = 'M' )) > (select count(*) 
from likes where user_id in (select user_id from profiles  where gender  = 'F' )) ,
'Больше лайков у М', 'Больше лайков у F');







