import xml.etree.cElementTree as ET

xmlFile1 = 'D:\luci\work\Models_and_app\FordS0_AMT_TPMS\Exporty\WidgetTrees\prj\TPMS_SC_TPMS.xml'
xmlFile1 = xmlFile1.replace('\\', '/')
# Open a file

tree = ET.ElementTree(file=xmlFile1)
root = tree.getroot()
msg1 = root.iterfind('.//UpdateMessageID')
for p in msg1:
    print(p.attrib['Name'])