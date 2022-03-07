import os
import json
from datetime import datetime
coaches_list = []
str_stand = ''
str_stand2 = ''
str_stand3 = ''
standings= open('8_standings.sql', 'w+',encoding='utf-8')
f = open('standings.txt',encoding='utf-8')
data = json.load (f)
for l in data["response"][0]["league"]['standings'][0]:
    str_stand3 += '('
    for k,v in l.items():
        if isinstance(v, dict) and l['rank']==1 and k!='update':
            for k1, v1 in v.items():

                if isinstance(v1, dict) and l['rank'] == 1:
                    for k2, v2 in v1.items():
                        if isinstance(v2,int) or v2 == None: str_stand2 += f'{k}_{k1}_{k2} INT,\n'
                        elif isinstance(v2,str) : str_stand2 += f'{k}_{k1}_{k2} VARCHAR(255),\n'
                        str_stand += f'{k}_{k1}_{k2},'
                elif k == 'team' and k1 == 'id':
                    str_stand2 += f'{k}_{k1} BIGINT,\n'
                    str_stand+= f'{k}_{k1},'
                elif l['rank'] == 1:
                    if isinstance(v1, int) or v1 == None: str_stand2 += f'{k}_{k1} INT,\n'
                    elif isinstance(v1, str): str_stand2 += f'{k}_{k1} VARCHAR(255),\n'
                    str_stand += f'{k}_{k1},'
        elif l['rank'] == 1 and k!='update':
            if k == 'rank':
                str_stand += f'rank_team,'
                str_stand2 += f'rank_team INT,\n'

            elif k== 'group':
                str_stand += f'group_team,'
                str_stand2 += f'group_team VARCHAR(255),\n'
            else :
                str_stand += f'{k},'
                if isinstance(v, int) or v == None: str_stand2 += f'{k} INT,\n'
                elif isinstance(v, str): str_stand2 += f'{k} VARCHAR(255),\n'
        '''values'''
        if isinstance(v, dict) and k != 'update':
            for k1, v1 in v.items():
                if isinstance(v1, dict):
                    for k2, v2 in v1.items():
                        if v2 == None: str_stand3 += f'null,'
                        else:
                            str_stand3 += f"'{v2}',"
                else : str_stand3 += f"'{v1}',"
        elif k != 'update' : str_stand3 += f"'{v}',"
    str_stand3 = str_stand3[:-1]+'),\n'

standings.write (f'use soccer;' + '\n')
standings.write (f'Drop table  if exists standings;'+'\n')
standings.write (f'Create table standings ('+ '\n')
standings.write (str_stand2[:-2] + ');\n')

standings.write(f'''Insert into standings ({str_stand[:-1]}) values ''')
standings.write('\n')
standings.write(f'''{str_stand3[:-3]}); ''')




