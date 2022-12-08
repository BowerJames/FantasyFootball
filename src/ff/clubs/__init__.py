import os
from .Club import Club
import ff
import json

with open(os.path.join(ff.PROJECT_ROOT,'src','ff','clubs','configs','clubs.json')) as f:
    clubs_json = json.load(f)

CLUBS={}

for club_dict in clubs_json['clubs']:
    CLUBS[club_dict['name']] = Club(club_dict)