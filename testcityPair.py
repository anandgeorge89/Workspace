import csv
import json
from collections import OrderedDict
csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("origin","destination")
reader = csv.DictReader( csvfile, fieldnames)
cityPairList = json.dumps([ row for row in reader ])
#print >> jsonfile, cityPairList
cityPairList = json.loads(cityPairList)
cityPairList.pop(0)
d = OrderedDict()

d["schemaVersion"] = "1.0.0"
d["dbVersion"] = "1.0"
d["description"] = "American Airlines Default"
d["waveformSearchOrder"] = [
                                "AfterBurner",
                                "SurfBeam2"
                              ]

afterBurnerCityPairs = {}
afterBurnerCityPairs["AfterBurner"] = cityPairList

d["enabledCityPairs"] = afterBurnerCityPairs


#parsedd = json.loads(dict)
print >> jsonfile , json.dumps(d, indent=4)
jsonfile.close()
jsonfile = open('file.json', 'r')
test =  json.load(jsonfile)

print test["schemaVersion"]
