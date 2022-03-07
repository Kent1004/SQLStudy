import os
import json
from datetime import datetime
coaches_list = []
str_coach = ''
coaches = open('4_coaches.sql', 'w+',encoding='utf-8')
with open('coaches1.txt',encoding='utf-8') as f:
    for obj in f:
        coaches_dict = json.loads(obj)
        coaches_list.append (coaches_dict)

for l in coaches_list:
    for k,v in l.items():
        if k == 'response':
            for l2 in  v:
                for k1,v1 in l2.items():
                    if k1 == 'career':
                        for l3 in v1:
                            if l3['end'] == None:
                                str_coach += f"({l2['id']}, '{l2['team']['id']}', '{l3['start']}','{l2['name']}', '{l2['firstname']}'," \
                                             f"'{l2['lastname']}', {l2['age']}, '{l2['birth']['date']}','{l2['birth']['place']}'," \
                                             f"'{l2['birth']['country']}')," + '\n'


print (str_coach)
coaches.write (f'use soccer;' + '\n')
coaches.write (f'Drop table  if exists coaches;'+'\n')
coaches.write (f'Create table coaches ('+ '\n')
coaches.write  ( f'coach_id INT PRIMARY KEY,\nteam_id BIGINT,\nstart DATETIME,\nname VARCHAR(255),\nfirstname VARCHAR(255),'
                 f'\nlastname VARCHAR(255),\nage INT,\nbirth_date DATETIME,\nbirth_place VARCHAR(255),\nbirth_country VARCHAR(255),\n Index coach_name_idx(name,firstname,lastname));\n')


coaches.write(f'Insert into coaches (coach_id, team_id, start, name, firstname, lastname, age, birth_date, birth_place, birth_country) values\n')
coaches.write(str_coach[:-2]+';')
