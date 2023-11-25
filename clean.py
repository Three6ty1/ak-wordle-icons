import json
import os
from path import *

with open(OPERATOR_PATH, 'r', encoding="utf-8") as f:
    char_data = json.load(f)

    existing = []

    for info in char_data.values():
        existing.append(info['charId'])

    found_ops = 0
    
    directory = os.fsencode(AVATAR_PATH)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not filename.startswith("char"):
            os.remove(AVATAR_PATH + filename)
        elif not filename.endswith('_2.png'):
            print('deleting non e2 art ' + filename)
            os.remove(AVATAR_PATH + filename)
        else:
            found_ops += 1

    print(str(found_ops) + ' total operator avatars found vs ' + str(len(existing)) + ' operators in db')