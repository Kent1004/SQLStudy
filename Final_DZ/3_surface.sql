use soccer;
Drop table  if exists surface;
Create table surface (id INT PRIMARY KEY , surface_type VARCHAR (100));
Insert into surface (id,surface_type) values
 ('1','artificial turf'),
 ('2','grass');