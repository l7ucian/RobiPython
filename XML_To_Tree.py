from __future__ import print_function
import collections
import xml.etree.cElementTree as ET
import os
import pprint

xmlFile1     = 'D:/luci/work/Models_and_app/FordS0_AMT_TPMS/Export/WidgetTrees/prj/TPMS_SC_TPMS.xml'

# Open a file
fo = open("D:/Un_work_related/tree_output.txt", "wb")

tree = ET.ElementTree(file=xmlFile1)
root = tree.getroot()
parent = {}
copy = {}
level = 0

def bfs(root):
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        for child in vertex.getchildren():
            queue.extend(child)
            parent[child] = vertex
bfs(root)
wids = collections.OrderedDict(sorted(parent.items(), reverse=False))


for key, value in wids.items() :
    if key.tag == 'Content':
        for a in key.getchildren():
            if copy != value.attrib['Name']:
                print()
                level += 1
            print(a.attrib['Name'], ' , ',  value.attrib['Name'])
            fo.write(a.attrib['Name'] + ' , ' +  value.attrib['Name']+ ' , ' + str(level) + os.linesep);
            copy = value.attrib['Name']
# Close opened file
fo.close()
