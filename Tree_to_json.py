import os
import json
import re
import collections
from os import path

file_path = path.abspath('D:/Un_work_related/tree_output.txt')
file = open(file_path, "r")
out = open("workfile.txt", 'w')
lines = file.readlines()
d = {}

for line in lines:
    split = re.findall(r"[\w']+", line)
    d[split[0]] = [split[1] , split[2]]
    print(split[0])
    print(split[1])
    print(split[2])
d = collections.OrderedDict(sorted(d.items(), reverse=True))
with open('D:/RobiPython/data.js', 'w') as outfile:
    outfile.write('var DATA = ')
    outfile.seek(11,0)
    json.dump(d, outfile)