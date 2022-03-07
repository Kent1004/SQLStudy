DROP DATABASE IF EXISTS soccer;
Create DATABASE soccer;
use soccer;
Drop table  if exists team;
Create table team (
id BIGINT PRIMARY KEY,
name VARCHAR(255),
code VARCHAR(255),
country VARCHAR(255),
founded INT,
national enum('true','false'),
logo VARCHAR(255),
Index team_name_idx(name));
Insert into team (id,name,code,country,founded,national,logo) values 
('555','CSKA Moscow','CSK','Russia','1911','False','https://media.api-sports.io/football/teams/555.png'),
('558','Spartak Moscow','SPA','Russia','1922','False','https://media.api-sports.io/football/teams/558.png'),
('596','Zenit Saint Petersburg','ZEN','Russia','1925','False','https://media.api-sports.io/football/teams/596.png'),
('597','Lokomotiv Moscow','LOK','Russia','1923','False','https://media.api-sports.io/football/teams/597.png'),
('621','Krasnodar','KRA','Russia','2007','False','https://media.api-sports.io/football/teams/621.png'),
('779','FC Rostov','ROS','Russia','1930','False','https://media.api-sports.io/football/teams/779.png'),
('1077','Arsenal Tula','ARS','Russia','2008','False','https://media.api-sports.io/football/teams/1077.png'),
('1078','FC UFA','UFA','Russia','2009','False','https://media.api-sports.io/football/teams/1078.png'),
('1079','Krylya Sovetov','KRY','Russia','1942','False','https://media.api-sports.io/football/teams/1079.png'),
('1083','Rubin','RUB','Russia','1958','False','https://media.api-sports.io/football/teams/1083.png'),
('1084','Ural','URA','Russia','1930','False','https://media.api-sports.io/football/teams/1084.png'),
('1085','Akhmat Grozny','TER','Russia','1958','False','https://media.api-sports.io/football/teams/1085.png'),
('1088','Dinamo Moscow','DYN','Russia','1923','False','https://media.api-sports.io/football/teams/1088.png'),
('1994','Khimki','KHI','Russia','1997','False','https://media.api-sports.io/football/teams/1994.png'),
('2011','Nizhny Novgorod','None','Russia','2015','False','https://media.api-sports.io/football/teams/2011.png'),
('2012','PFC Sochi','None','Russia','2010','False','https://media.api-sports.io/football/teams/2012.png');