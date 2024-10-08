#!/usr/bin/env python

import json
import os

for filename in os.listdir("."):
    if os.path.isfile(filename) and os.path.splitext(filename)[-1].lower() == ".json":
        with open(filename) as in_file:
            data = json.load(in_file)
        with open(filename, "w") as out_file:
            # indent=4 makes the files human readable
            json.dump(data, out_file, indent=4)
