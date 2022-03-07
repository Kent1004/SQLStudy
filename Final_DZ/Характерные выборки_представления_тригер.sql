use soccer;
-- Сравнивет количество проигравших команд с выйгравшими на искуственном поле
select if(
(select count(*) from fixture f
join venue v on f.venue_id = v.id 
join surface s on v.surface_id = s.id 
where s.surface_type <>  'grass' and f.away_winner = 'false')> 
(select count(*) from fixture f
join venue v on f.venue_id = v.id 
join surface s on v.surface_id = s.id 
where s.surface_type <>  'grass' and f.away_winner = 'true'),
'Гостевые команды больше проиграли на искусственном поле',
'Гостевые команды больше выигрывали на искусственном поле'
) as 'Кто больше';

-- Кто больше забил голов осенью 2021 на домашнем поле
select t.name, sum(f.goals_home) as sum_goals from team t 
join fixture f  on f.home_id =t.id 
where (f.date > '2021-08-31' and f.date <'2021-12-01') 
group by t.name 
order by sum_goals DESC;

-- При каком рефери зенит больше побеждал

select  r.name,count(*) as count_games from referee r 
join fixture f on f.referee_id  = r.id
join team t on f.away_id = t.id or f.home_id = t.id
where t.name like 'Zenit%' and (f.home_winner ='true' or f.away_winner = 'true')
group by r.name
order by count_games desc
limit 1;

-- Вывести статистику по рефери с количеством побед хозяев матча

select  r.name,count(*) as count_games from referee r 
join fixture f on f.referee_id  = r.id
join team t on f.away_id = t.id or f.home_id = t.id
where  f.home_winner ='true'
group by r.name
order by count_games desc
;

-- Представление1: игроки , которые забивали голы
drop view if exists Players;

create view Players (Player, Team, Goals) as  
select p.name,t.name ,s.goals_total from player p 
join team t on p.team_id = t.id 
join statistics s on s.player_id = p.id 
where s.goals_total > 0
order by s.goals_total desc; 

select * from Players;

-- Представление2: таблица статистиски  побед команд дома и в гостях
drop view if exists Teams;

 

create view Teams AS
select t2.name , (
select count(*) from team t
join fixture f on t.id  = f.home_id 
where f.home_winner = 'true' and t2.id = f.home_id group by t.name) as Home_Win ,
(select count(*) from team t
join fixture f on t.id  = f.away_id 
where f.away_winner = 'true' and t2.id = f.away_id group by t.name ) as Away_win
from team t2;


select * from TEAMS;

-- Тригер проверки  при добавлении команды по стране

drop trigger if exists check_team_country;

DELIMITER // ; 

CREATE TRIGGER check_team_count BEFORE INSERT ON team
FOR EACH row
begin 
	if (new.country <>'Russia') then 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'В текущем чемпионате играют команды только из страны Russia';	
	end if;
end;

DELIMITER ; 

insert into team (id, name, country) values
(123123,'Porto','Portugal');





