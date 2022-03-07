import os
import json
from datetime import datetime
top_list = []
top_sc = ''
top_sc1 = ''
top_sc2 = ''
top= open('10_top_scores.sql', 'w+',encoding='utf-8')
f = open('top_scorers.txt',encoding='utf-8')
data = json.load (f)
for k,v in data["response"][0].items():
    if k == 'player':
        top_sc += 'player_id BIGINT PRIMARY KEY,\n'
        top_sc1 += '(player_id, '
    if k == 'statistics':
        for l1 in v:
            for k1,v1 in l1.items():
                if k1=='games' or k1 == "substitutes" or k1 == "shots" or k1 == "goals" or k1 ==  "penalty":
                    for k2, v2 in v1.items():
                        if k2== 'rating' : top_sc+= f'{k1}_{k2} Float,\n '
                        elif k2 == 'captain': top_sc+= f"{k1}_{k2} enum('true','false')," + '\n'
                        elif isinstance(v2, int)  or v2 == None: top_sc+= f'{k1}_{k2} INT, \n'
                        elif isinstance(v2, str): top_sc+= f'{k1}_{k2} VARCHAR(255),\n '
                        top_sc1+= f'{k1}_{k2},'
for l in data["response"]:
    top_sc2 += '('
    # print (l['player']['id'])
    if l['player'] : top_sc2 += f"{l['player']['id']}, "
    for l1 in l['statistics']:
        for k,v in l1.items():
            if k=='games' or k == "substitutes" or k == "shots" or k == "goals" or k ==  "penalty":
                for k1,v1 in v.items():
                    if v1 == None: top_sc2 += f"null, "
                    else: top_sc2 += f"'{v1}', "
    top_sc2= top_sc2[:-2] + '),\n'

top.write (f'use soccer;' + '\n')
top.write (f'Drop table  if exists top_scores;'+'\n')
top.write (f'Create table top_scores ('+ '\n')
top.write (top_sc[:-3] + ');\n')
top.write(f'''Insert into top_scores {top_sc1[:-1]}) values ''')
top.write('\n')
top.write(f'''{top_sc2[:-3]}); ''')

        #     print(type(l['statistics']['games']))
            # top_sc2 += f"({l['statistics']['team']['id']}, "



            # top_sc2 += f"({l['player']['id']},"
            # top_sc2 += f"({l['statistics']['team']['id']}, "
#
#             top_sc += 'player_id BIGINT,\n'
#             top_sc1 += '(player_id, '
# top_sc += 'team_id BIGINT,\n'
#         top_sc1 += 'team_id, '
