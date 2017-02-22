import xml.etree.cElementTree as ET

xmlFile1 = 'D:/luci/work/Models_and_app/FordS0_AMT_SettingsMenu/FordS0_AMT_ExhaustFilter/expy/WidgetTrees/prj/ExhaustFilter_SC_Main.xml'

# Open a file

tree = ET.ElementTree(file=xmlFile1)
root = tree.getroot()
props = root.iterfind('.//Property')
for p in props:
    if 'Enumeration' in p.attrib['Content']:
        print ('boobies1',p.attrib['Content'])

props = root.iterfind('.//Transition')
for p in props:
    if 'Enumeration' in p.attrib['Content']:
        print ('boobies',p.attrib['Content'])
# for p in root.getchildren()[0]:
#     print(p.attrib['Content'])

# for wid in root.iterfind('.//Widget'):
#     print(wid.attrib['Name'])
