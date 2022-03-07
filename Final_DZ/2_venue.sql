use soccer;
Drop table  if exists venue;
Create table venue (
id INT PRIMARY KEY,
name VARCHAR(255),
address VARCHAR(255),
city VARCHAR(255),
capacity INT,
surface_id INT,
image VARCHAR(255),
team_id BIGINT);
Insert into venue (id,name,address,city,capacity,surface_id,image,team_id) values
('1333','VEB Arena','3-ya Peschanaya ul.','Moskva','30000',2,'https://media.api-sports.io/football/venues/1333.png',555),
('1352','Otkrytiye Arena','Volokolamskoye shosse, Tushino','Moskva','45360',2,'https://media.api-sports.io/football/venues/1352.png',558),
('1356','Saint-Petersburg Stadium','Futbolnaya al.','St. Petersburg','68134',2,'https://media.api-sports.io/football/venues/1356.png',596),
('1327','RZD Arena','ul. Bol&apos;shaya Cherkizovskaya 125','Moskva','28800',2,'https://media.api-sports.io/football/venues/1327.png',597),
('1338','Stadion FK Krasnodar','ul. Vostochno-Kruglikovskaya 126','Krasnodar','35074',2,'https://media.api-sports.io/football/venues/1338.png',621),
('1339','Rostov Arena','ul. Levoberezhnaya','Rostov-na-Donu','45000',2,'https://media.api-sports.io/football/venues/1339.png',779),
('1329','Stadion Arsenal','pr. Lenina, 87','Tula','20048',2,'https://media.api-sports.io/football/venues/1329.png',1077),
('12043','BetBoom Àrena','ul. Komarova 9','Ufa','15132',1,'https://media.api-sports.io/football/venues/12043.png',1078),
('11911','Solidarnost Arena','ul. Dal&apos;nyaya','Samara','44918',2,'https://media.api-sports.io/football/venues/11911.png',1079),
('1349','Kazan Arena','Prospekt Husaina Yamasheva 115a','Kazan&apos;','45105',2,'https://media.api-sports.io/football/venues/1349.png',1083),
('1355','Ekaterinburg Arena','ul. Repina 5','Ekaterinburg','35696',2,'https://media.api-sports.io/football/venues/1355.png',1084),
('1353','Akhmat Arena','Zhukavskogo per. 9, Staraya Sunzha','Groznyi','30597',2,'https://media.api-sports.io/football/venues/1353.png',1085),
('1334','VTB Arena','Leningradskiy pr., 36','Moskva','26700',2,'https://media.api-sports.io/football/venues/1334.png',1088),
('1337','Stadion Rodina','ul. Chkalova 4a','Khimki','10033',2,'https://media.api-sports.io/football/venues/1337.png',1994),
('2835','Stadion Nizhny Novgorod','ul. Dolzhanskaya','Nizhniy Novgorod','44899',2,'https://media.api-sports.io/football/venues/2835.png',2011),
('2834','Olimpiyskiy Stadion Fisht','Olimpiyskiy prospekt 15','Sochi','48000',2,'https://media.api-sports.io/football/venues/2834.png',2012);