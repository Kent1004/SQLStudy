use soccer;
Drop table  if exists referee;
Create table referee ( id INT PRIMARY KEY, name VARCHAR(255), country VARCHAR(100),
Index referee_name_idx(name));
Insert into referee (id,name,country) values 
 ('1','Aleksei Vasilevich Suhoi','Russia'),
 ('2','Igor Panin','Russia'),
 ('3','Sergei Ivanov','Russia'),
 ('4','Vasiliy Kazartsev','Russia'),
 ('5','Artem Lyubimov','Russia'),
 ('6','Panin Igor Nikolaevich','Russia'),
 ('7','Lyubimov Artem Mikhailovich','Russia'),
 ('8','Evgeniy Kukulyak','Russia'),
 ('9','Shadyhanov Pavel','Russia'),
 ('10','Sergei Karasev','Russia'),
 ('11','Ivan Sidenkov','Russia'),
 ('12','Aleksei Valerevich Matyunin','Russia'),
 ('13','Artyom Chistyakov','Russia'),
 ('14','Vladislav Bezborodov','Russia'),
 ('15','Pavel Kukuyan','Russia'),
 ('16','Kirill Levnikov','Russia'),
 ('17','Vitaly Meshkov','Russia'),
 ('18','Anton Frolov','Russia'),
 ('19','Vladimir Moskalev','Russia'),
 ('20','Aleksei Amelin','Russia');