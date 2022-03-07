import json
import re
from datetime import datetime
str_player = ''
str_player1 = ''
str_player2 = ''
unigue_player = ''
player_list = []
player = open('7_player.sql', 'w+',encoding='utf-8')
with open('players_2.txt') as f:
    for obj in f:
        players_dict = json.loads(obj)
        player_list.append (players_dict)
# print
player.write (f'use soccer;' + '\n')
player.write (f'Drop table  if exists player;'+'\n')
player.write (f'Create table player ('+ '\n')

# player.write(f'''Insert into fixture ({str_fix1[:-1]}) values ''')
# player.write('\n')
for k,v  in player_list[0]["response"][0]['player'].items():
    if k == 'injured':
        str_player += f"{k} enum('true','false')," + '\n'
        str_player1 += f'{k},'
    elif k == 'id' :
        str_player += f"{k} BIGINT PRIMARY KEY," + '\n'
        str_player1 += f'{k},'
    elif isinstance(v, int)  or k== 'weight' or k== 'height':
        str_player += f"{k} INT," + '\n'
        str_player1+= f'{k},'
    elif isinstance(v, str):
        str_player += f"{k} VARCHAR(255)," + '\n'
        str_player1 += f'{k},'
    elif isinstance(v, dict):
        for k2, v2 in v.items():
            if isinstance(v2, int) :
                str_player += f"{k}_{k2} INT," + '\n'
                str_player1 += f'{k}_{k2},'
            elif isinstance(v2, str):
                str_player += f"{k}_{k2} VARCHAR(255)," + '\n'
                str_player1 += f'{k}_{k2},'
            elif k2 == 'date':
                str_player += f'date DATETIME,' + '\n'
                str_player1 += f'date,'
str_player += f'team_id BIGINT,'
str_player1 += f'team_id,'
str_player += f'position VARCHAR(255),' + '\n'
str_player1 += f'position ,'
str_player += f'rating FLOAT,' + '\n'
str_player1 += f'rating  ,'
str_player+= f'Index player_name_idx(name,firstname,lastname));'
# str_player2 += f'Insert into player ({str_player1[:-1]}) values' + '\n'
for j in player_list:
    for j1 in j['response']:
        str_player2 += '('
        for k,v in j1['player'].items():
            if v == None: str_player2 += f'null,'
            elif isinstance(v, dict):
                for k1,v1 in v.items(): str_player2+= f'"{v1}",'
            elif v != None and ( k == 'height' or k == 'weight'):
                str_player2+= f'''"{v.split(' ')[0]}",'''
            elif v == None : str_player2+= f'null,'
            elif k== 'id' :
                str_player2+= f'{v},'
            else:
                str_player2+= f'"{v}",'
        str_player2 +=  f'''{j1['statistics'][0]['team']['id']},'''
        str_player2 += f''''{j1['statistics'][0]['games']['position']}','''
        if j1['statistics'][0]['games']['rating'] == None:
            str_player2 += f'''null),'''
        else: str_player2 += f''''{j1['statistics'][0]['games']['rating']}'),'''

        str_player2 += '\n'
unigue_player += f'Insert into player ({str_player1[:-1]}) values' + '\n'
print (str_player)

# a = re.findall(r'\b\w*_id\b',unigue_player)
# b = re.findall(r'\b\w*name\b',unigue_player)
# c = re.findall(r'?\w+\w+',unigue_player)
# print (c,b)


a = str_player2.splitlines()
unique_rows = dict.fromkeys (a)
unigue_player += "\n".join(unique_rows)



player.write (str_player[:-2] + ');\n')
player.write(f'{unigue_player[:-1]}; ')
player.write('\n')

