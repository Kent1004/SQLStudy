use vk;

select  DISTINCT  firstname from users order by firstname  ;

alter table profiles 
add column   is_active enum('true','false') default 'true';


update profiles set is_active = 'false' 
where birthday > '2004-02-01' 

select * from profiles
delete from messages 
where created_at > CURRENT_TIMESTAMP

update friend_requests set target_user_id = (SELECT id FROM users ORDER BY RAND() LIMIT 1);



