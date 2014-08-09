import json, pprint
with open('MySpecialView.pyui') as in_file:
    pprint.pprint(json.load(in_file))
