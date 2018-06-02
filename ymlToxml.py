#!/usr/bin/python   

import sys
import json
import yaml
import xml.etree.cElementTree
import dicttoxml
import collections



def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield recursive_items(value)
        else:
            yield (key, value)
  
def flatten_json(json):
    if type(json) == dict:
        for k, v in list(json.items()):
            if type(v) == dict:
                flatten_json(v)
                json.pop(k)
                for k2, v2 in v.items():
                    json[k+"."+k2] = v2

def writeDictToFile(ymlData):
    ff = open('output.txt', 'w+')
    for i,v in enumerate(ymlData):
        #print v,':"{}"'.format(ymlData.get(v).encode('utf-8'))
        ff.write(v)
        ff.write(':"{}"\n'.format(ymlData.get(v).encode('utf-8')))
        ff.close()
        
def outputToXML(data):
    ff = open('output.xml','w+')
    ff.write(data)
    ff.close()
              
def main():
    f = open('en.yml', 'rb')
    ymlData = yaml.load(f)
    print(len(ymlData))
    flatten_json(ymlData)
    testDict = collections.OrderedDict(ymlData)
    xmlData = dicttoxml.dicttoxml(ymlData)
    #print(ymlData)
    #print(xmlData)
    #print(ymlData.values())
    outputToXML(xmlData)
    
    
        #print(ymlData[v])
    #print(jsonData)
    
    #yaml.dump(jsonData, ff, allow_unicode=True)
    #json.dump(jsonData, ff, ensure_ascii=False)
    ##yaml.dump(yaml.load(ymlData)), ff, default_flow_style=False, allow_unicode=True)
    f.close()
    
if __name__== "__main__":
  main()
