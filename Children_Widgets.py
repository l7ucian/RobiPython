import xml.etree.cElementTree as ET

xmlFile1     = 'D:/luci/work/Models_and_app/FordS0_AMT_SettingsMenu/FordS0_AMT_ExhaustFilter/expy/WidgetTrees/prj/ExhaustFilter_SC_Main.xml'

# Open a file

tree = ET.ElementTree(file=xmlFile1)
root = tree.getroot()

specific = root.find(".//*[@Name='WRN_SC_Main']")
for wid in specific.iterfind('.//Widget'):
    print(wid.attrib['Name'])
    for res in wid.iterfind('.//Content'):
        print(res)