import xml.etree.cElementTree as ET
import os
loop6_path = 'D:\luci\work\Models_and_app\FordS0_AMT_Configuration\Warnings'
loop6_path = loop6_path.replace('\\', '/')

loop7_path = 'D:\luci\work\Models_and_app1\FordS0_AMT_Configuration\Warnings'
loop7_path = loop7_path.replace('\\', '/')
dict = {}
paths=['WarningGroup_NR','WarningGroup_RGA','WarningGroup_SC','WarningGroup_TA_2','WarningGroup_TA_4'\
       ,'WarningGroup_TA_10','WarningGroup_TA_15','WarningGroup_TA_24','WarningGroup_TA_30','WarningGroup_TAstar_4','WarningGroup_TAstar_10']

tree = ET.ElementTree(file=loop6_path + '/' + 'WarningDispatchers' + '.xml')
root = tree.getroot()
warning_views = tree.iterfind(".//WarningView")
warning_views_names = []
name = ''

for elem in warning_views:
    if 'Overlay' not in elem.attrib['WarningName']:
        warning_views_names.append(elem.attrib['WarningName'])



for file in paths:
    search_tree = ET.ElementTree(file=loop6_path + '/' + file + '.xml')
    search_root = search_tree.getroot()
    with open(loop6_path+ '/'+file+ '.xml', 'r+') as f:
        for name in warning_views_names:
           if search_root.find(".//*[@Name='"+name+"']") != None:
               rname = search_root.find(".//*[@Name='"+name+"']").attrib['Name']
               rgroup =  file.replace('WarningGroup_', '')
               #print(rname + 5*' '+rgroup)
               dict[rname] = [rgroup, 'Loop6']



tree = ET.ElementTree(file=loop7_path + '/' + 'WarningDispatchers' + '.xml')
root = tree.getroot()
warning_views = tree.iterfind(".//WarningView")
warning_views_names = []
name = ''

for elem in warning_views:
    if 'Overlay' not in elem.attrib['WarningName']:
        warning_views_names.append(elem.attrib['WarningName'])

for file in paths:
    search_tree = ET.ElementTree(file=loop7_path + '/' + file + '.xml')
    search_root = search_tree.getroot()
    with open(loop6_path+ '/'+file+ '.xml', 'r+') as f:
        for name in warning_views_names:
           if search_root.find(".//*[@Name='"+name+"']") != None:
               rname = search_root.find(".//*[@Name='"+name+"']").attrib['Name']
               rgroup =  file.replace('WarningGroup_', '')
               #print(rname + 5*' '+rgroup)
               if rname in dict:
                dict[rname].append('Loop7')
               else:
                   dict[rname] = [rgroup, 'Loop7']

for key,value in dict.items():
    print(key,value)

