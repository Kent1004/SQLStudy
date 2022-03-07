use soccer;
Drop table  if exists coaches;
Create table coaches (
coach_id INT PRIMARY KEY,
team_id BIGINT,
start DATETIME,
name VARCHAR(255),
firstname VARCHAR(255),
lastname VARCHAR(255),
age INT,
birth_date DATETIME,
birth_place VARCHAR(255),
birth_country VARCHAR(255),
 Index coach_name_idx(name,firstname,lastname));
Insert into coaches (coach_id, team_id, start, name, firstname, lastname, age, birth_date, birth_place, birth_country) values
(1308, '555', '2021-09-01','A. Grigoryan', 'Aleksandr','Grigoryan', 56, '1966-09-28','Yerevan','Armenia'),
(14981, '555', '2021-06-01','A. Berezutski', 'Aleksey','Berezutskiy', 40, '1982-06-20','Moskva','Russia'),
(1307, '596', '2018-05-01','S. Semak', 'Sergey','Semak', 46, '1976-02-27','Sychanske','Ukraine'),
(6475, '597', '2021-10-01','M. Gisdol', 'Markus','Gisdol', 53, '1969-08-17','Geislingen','Germany'),
(2, '621', '2022-01-01','D. Farke', 'Daniel','Farke', 46, '1976-10-30','None','Germany'),
(16058, '779', '2021-10-01','V. Kafanov', 'Vitali','Kafanov', 62, '1960-05-24','None','Russia'),
(1319, '1077', '2021-09-01','M. Božović', 'Miodrag','Božović', 54, '1968-06-22','Mojkovac','Montenegro'),
(7845, '1078', '2021-04-01','A. Stukalov', 'Aleksey','Stukalov', 39, '1983-11-24','None','Russia'),
(1086, '1079', '2020-07-01','I. Osinkin', 'Igor','Osinkin', 57, '1965-06-04','None','Russia'),
(1992, '1083', '2019-12-01','L. Slutskiy', 'Leonid','Slutskiy', 51, '1971-05-04','Volgograd','Russia'),
(1327, '1084', '2021-08-01','I. Shalimov', 'Igor','Shalimov', 53, '1969-02-02','Moskva','Russia'),
(1072, '1085', '2020-07-01','A. Talalaev', 'Andrey','Talalaev', 50, '1972-10-05','Moskva','Russia'),
(1539, '1088', '2020-10-01','S. Schwarz', 'Sandro','Schwarz', 44, '1978-10-17','Mainz','Germany'),
(8914, '1088', '2022-01-01','S. Lavrentyev', 'Sergey','Lavrentjev', 50, '1972-04-09','Klimovsk','Russia'),
(1317, '1994', '2021-11-01','I. Cherevchenko', 'Igor','Cherevchenko', 48, '1974-08-21','Dushanbe','Tajikistan'),
(9204, '2011', '2021-06-01','A. Kerzhakov', 'Aleksandr','Kerzhakov', 40, '1982-11-27','Kingisepp','Russia'),
(1312, '2012', '2019-12-01','V. Fedotov', 'Vladimir','Fedotov', 56, '1966-08-12','Mikhaylovsk','Russia');