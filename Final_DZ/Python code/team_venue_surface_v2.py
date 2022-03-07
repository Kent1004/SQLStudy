import os
import json


f = open('teams.txt' , 'r' )
team = open('1_teams.sql', 'w+')
venue = open('2_venue.sql', 'w+')
surface = open ('3_surface.sql', 'w+')

team.write(f'DROP DATABASE IF EXISTS soccer;'+'\n')
team.write(f'Create DATABASE soccer;'+'\n')



str_venue=''
str_team=''
str_surface=''
surface_list = []
i=1
data = json.load (f)

team.write (f'use soccer;' + '\n')
team.write (f'Drop table  if exists team;'+'\n')
team.write (f'Create table team ('+ '\n')
venue.write (f'use soccer;' + '\n')
venue.write (f'Drop table  if exists venue;'+'\n')
venue.write (f'Create table venue ('+ '\n')
surface.write (f'use soccer;' + '\n')
surface.write (f'Drop table  if exists surface;'+'\n')
surface.write (f'Create table surface (id INT PRIMARY KEY , surface_type VARCHAR (100));'+ '\n')


''' Таблица surface'''
for l in list(set(kk for m in data['response'] for  mm,k in m.items() for mmm,kk  in k.items() if mmm == 'surface' and kk != None)):
    surface_list.append ((f'''{i},{l}''').split(','))
    str_surface+= (f''' ('{i}','{l}'),''')+'\n'
    i+=1
'''Таблицы team an venue'''
for key,vals in data.items():
    if key == "response":
        for k,v in vals[0]['team'].items():
            if k == 'id':
                str_team+=(f'{k} BIGINT PRIMARY KEY,' + '\n')
            elif isinstance(v, int) and k != 'national' :
                str_team+=(f'{k} INT,'+'\n')
            elif k == 'national':
                str_team+=(f"{k} enum('true','false')," + '\n')
            else: str_team+=f'{k} VARCHAR(255),' + '\n'
        # str_team = str_team[:-2] + ');\n'
        for k,v in vals[0]['venue'].items():
            if k == 'id':
                str_venue+=(f'{k} INT PRIMARY KEY,' + '\n')
            elif k == 'surface':
                str_venue+=(f'surface_id INT,' + '\n')
            elif isinstance(v, int) :
                str_venue+=(f'{k} INT,'+'\n')
            else: str_venue+=(f'{k} VARCHAR(255),'+'\n')
        str_venue+=f'team_id BIGINT);' +'\n'
        # venue.write(f'{k} VARCHAR(255),' + '\n')
        str_team+=(f'''Index team_name_idx(name));\nInsert into team ({','.join(str(k) for k in vals[0]['team'].keys())}) values ''' +'\n')
        str_venue += f'Insert into venue ('
        if vals[0]['venue'] == 'surface' : str_venue += 'surface_id,'
        for k in vals[0]['venue'].keys():
            if k == 'surface': str_venue += 'surface_id,'
            else: str_venue+=f'{k},'
        str_venue+=f'team_id) values'+'\n'

        for val in vals:
            for key1,val1 in val.items():
                if key1 == 'team':
                    str_team +=  (f'''('{"','".join(str(v).replace("'","") for k,v in val1.items() )}'),''') + '\n'
                if key1 == 'venue':
                    str_venue += '('
                    for k, v in val1.items():
                        if k =='surface':
                            for surf in surface_list:
                                if surf[1] == v:
                                    str_venue += f'{surf[0]},'
                                    # print(str_venue)
                        else:
                            if isinstance(v,int) : str_venue+= f''''{v}','''
                            else: str_venue+=f''''{v.replace("'","")}','''
                    str_venue+= f"{val['team']['id']}"
                    str_venue +=  '),\n'
print (str_team)
team.write(str_team[:-2]+';')
venue.write(str_venue[:-2]+';')
surface.write('Insert into surface (id,surface_type) values'+'\n' +str_surface[:-2] +';')
f.close()
team.close()
venue.close()
surface.close()
