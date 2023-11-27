import json
import os
from path import *

with open(OPERATOR_PATH, 'r', encoding="utf-8") as f:
    char_data = json.load(f)

    existing = {}

    for info in char_data.values():
        existing[info['charId']] = info['rarity']

    found_ops = 0
    threestars = 0
    twostars = 0
    onestars = 0

    directory = os.fsencode(AVATAR_PATH)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not filename.startswith("char"):
            os.remove(AVATAR_PATH + filename)
        elif not filename.endswith('_2.png'):
            charId = filename.replace('.png', '')
            if charId in existing:
                if existing[charId.replace('.png', '')] == 3:
                    threestars += 1
                elif existing[charId.replace('.png', '')] == 2:
                    twostars += 1
                elif existing[charId.replace('.png', '')] == 1:
                    onestars += 1
                else:
                    print('deleting non e2 art ' + filename)
                    os.remove(AVATAR_PATH + filename)
            else:
                print('deleting operator skin' + filename)
                os.remove(AVATAR_PATH + filename)
        else:
            found_ops += 1

    print(str(found_ops) + ' total operator avatars found vs ' + str(len(existing)) + ' operators in db')
    print(str(threestars) + ' three stars ' + str(twostars) + ' two stars ' + str(onestars) + ' one stars')