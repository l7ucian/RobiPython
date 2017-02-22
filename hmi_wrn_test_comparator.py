import xml.etree.cElementTree as ET
import sys
import re
import csv
import collections


globalMsgListFile = "C:/Users/robert.ilitoi/Desktop/Warning View_subpriorities/Global_Msg_List.csv"
xmlFile1     = "d:/FordProject/Repository/Loop 7/FordS0_AMT_Configuration/Warnings/WarningDispatchers.xml"
translationFile2     = 'C:/Users/robert.ilitoi/Desktop/Warning View_subpriorities/WarningDispatchers2.xml'
warningMap = {}
warningMap2 = {}
globalMsgList = {}
data = []

tree = ET.ElementTree(file=xmlFile1)
container = tree.iterfind('.//WarningView')

def copy_tree( tree_root ):
    return ET.ElementTree( tree_root );

def loadGlobalWarningList():   
    with open(globalMsgListFile, mode='r') as infile:
        reader = csv.DictReader(infile)
        key = ''
        priority = 2
        subprio = 1.0
        
        for rows in reader:
            key=rows['ID'].strip( ) #WARN_TYPE,TIME_OUT,LM,ICON,COLOR,CHIME_TYPE,TEXT
           
           
            try:
                priority = int(rows['PRIORITY'].strip( ) )
            except Exception:
                priority = 2
                
            try:
                subprio = float(rows['SUBPRIO'] )
            except Exception:
                subprio = 255
                               
            warningObj = (key,priority,subprio)
            globalMsgList[key]=warningObj
 
             
loadGlobalWarningList()
root = tree.getroot()
for elem in container:
    key = elem.attrib["WarningName"]
    if(key in globalMsgList):
        w = globalMsgList[key]
        prio =    w[1]
        subprio = w[2]
        data.append ( (key, prio, subprio, elem) )
        
        
    
    #sortedMap = collections.OrderedDict( sorted( warningMap.items( ) ) )
    # insert the last item from each tuple
    
    #with open('TestDispatcher1.txt','w') as f:
    #    for index, wrnObject in sortedMap.items():
    #        f.write(wrnObject)
    #        f.write("\n")
          
data.sort( key=lambda row: (row[1], row[2]) )



myNewTree = ET.ElementTree(root)
myNewRoot = myNewTree.getroot()
myNewRoot.getchildren()[0].getchildren()[0].getchildren()[0].getchildren()[1].clear( )

for item in data:
    #print(ET.tostring(item[3] ) )
    myNewRoot.getchildren()[0].getchildren()[0].getchildren()[0].getchildren()[1].append(item[3])


myNewTree.write("NewWarningsDispatchers.xml")
print("SUCCESS, Warning Views have been ordered, compare the output with your original file!")
#container[:] = [item[-3] for item in data]  

#tree.write("new-data.xml")            
            
#tree2 = ET.ElementTree(file=translationFile2)

#for elem in tree2.iterfind('.//WarningView'):
#    key = elem.attrib["WarningName"]
#    warningMap2[key] = elem
    
#    sortedMap = collections.OrderedDict( sorted( warningMap2.items( ) ) )
    
#    with open('TestDispatcher2.txt','w') as f:
#        for index, wrnObject in sortedMap.items():
#            f.write(wrnObject)
#            f.write("\n")