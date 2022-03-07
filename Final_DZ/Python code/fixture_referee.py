import os
import json
from datetime import datetime


f = open('games.txt' , 'r' )
fixture = open('5_fixture.sql', 'w+')
ref = open('6_referee.sql', 'w+')

ref_list=[]
str_ref=''
str_fix=''
str_fix1=''
str_fix2=''
str_fix3=''
str_team=''
data = json.load(f)
i=1
for l in list(set(kk for m in data['response'] for  mm,k in m.items() for mmm,kk  in k.items() if mmm == 'referee' and kk != None)):
    ref_list.append ((f'''{i},{l}''').split(','))
    str_ref+= (f''' ('{i}','{l.replace(', ', "','")}'),''')+'\n'
    i+=1

for key,vals in data.items():
    if key == "response":
        for val in vals:
            str_fix2+='('
            for k,v in val.items():
                for k1,v1 in v.items():
                    '''Список наименвоаний значений'''
                    if vals.index(val)==0:
                        if isinstance(v1, dict):
                            for k2,v2 in v1.items():
                                str_fix1+= f'{k1}_{k2},'
                                if k2 == 'winner':
                                    str_fix3 += f"{k1}_{k2} enum('true','false')," + '\n'
                                elif (k2 == 'id' and k1== 'away')  or (k2 == 'id' and k1== 'home' ) :
                                    str_fix3+= f"{k1}_{k2} BIGINT,"+ '\n'
                                elif isinstance(v2, int) and k2!= 'winner' :
                                    str_fix3+= f"{k1}_{k2} INT,"+ '\n'
                                elif isinstance(v2, str):
                                    str_fix3+= f"{k1}_{k2} VARCHAR(255),"  + '\n'
                                else  :
                                    str_fix3 += f"{k1}_{k2} INT," + '\n'
                        elif k1 == 'referee':
                            str_fix1 += f'referee_id,'
                            str_fix3 += f'referee_id INT,' + '\n'
                        elif k1 == 'id' and k!= 'league':
                            str_fix1 += f'id,'
                            str_fix3 += f'id BIGINT PRIMARY KEY,' + '\n'
                        elif k1=='date':
                            str_fix1 += f'date,'
                            str_fix3 += f'date DATETIME,' + '\n'
                        elif k == 'league' or k == 'goals' :
                            str_fix1 += f'{k}_{k1},'
                            if isinstance(v1, int):
                                str_fix3 += f"{k}_{k1} INT," + '\n'
                            elif isinstance(v1, str):
                                str_fix3 += f"{k}_{k1} VARCHAR(255)," + '\n'
                        else:
                            str_fix1+= f'{k1},'
                            if isinstance(v1, int) :
                                str_fix3 += f"{k1} INT," + '\n'
                            elif isinstance(v1, str) :
                                str_fix3 += f"{k1} VARCHAR(255)," + '\n'
                            else: str_fix3 += f"{k1} VARCHAR(255)," + '\n'
                    '''Строки для value'''
                    if isinstance(v1, dict):
                        for k2, v2 in v1.items():
                            if v2 == None: str_fix2 += f'''null,'''
                            elif isinstance(v2, int) : str_fix2 += f''''{v2}','''
                            else:  str_fix2 += f''''{v2.replace("'", "")}','''
                    else:
                        if k1 == 'referee':
                            if v1 == None: str_fix2 += f'null,'
                            else:
                                for referee in ref_list:
                                    if v1!= None and referee[1] == v1.split(',')[0]:
                                        str_fix2 += f'{referee[0]},'
                        elif k1=='date':
                            output_date = datetime.strptime(v1, '%Y-%m-%dT%H:%M:%S%z')
                            v1 = output_date.strftime('%Y-%m-%d %H:%M:%S')
                            str_fix2 += f''''{v1}','''
                        else:
                            if v1 == None: str_fix2 += f'''null,'''
                            elif isinstance(v1,int) : str_fix2 += f''''{v1}','''
                            else: str_fix2 += f''''{v1.replace("'","")}','''
            str_fix2= str_fix2 [:-1] + '),\n'

print (str_fix3)
fixture.write (f'use soccer;' + '\n')
fixture.write (f'Drop table  if exists fixture;'+'\n')
fixture.write (f'Create table fixture ('+ '\n')
fixture.write (str_fix3[:-2] + ');\n')

fixture.write(f'''Insert into fixture ({str_fix1[:-1]}) values ''')
fixture.write('\n')
fixture.write(f'''{str_fix2[:-3]}); ''')

ref.write (f'use soccer;' + '\n')
ref.write (f'Drop table  if exists referee;'+'\n')
ref.write (f'Create table referee ( id INT PRIMARY KEY, name VARCHAR(255), country VARCHAR(100),'+ '\n')
ref.write (f'Index referee_name_idx(name));'+ '\n')

ref.write(f'''Insert into referee (id,name,country) values ''')
ref.write('\n')
ref.write(str_ref[:-2]+';')


f.close()
fixture.close()
ref.close()
