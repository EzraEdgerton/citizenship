import pandas as pd
import json

cf = open("DataViz-Citizenships.csv", "r")
cz = pd.read_csv(cf)
mf = open("DataViz-DSMaking_Skills.csv","r")
ms = pd.read_csv(mf)


f = open("transcripts.txt", "r")

trans = f.read()


#print(cz)
#print(ms)


result = dict()
split_trans = trans.split('<break>')
for x in split_trans:
	a = x.split("\n")

	a = list(filter(lambda x: len(x) > 0, a))
	if a[0] not in result:
		result[a[0]] = {
			'text' : a[1],
			'cz' : [],
			'ms' : []
		}
	#for i in a:
	#	print(i)

print(result.keys())


the_cz = cz.to_dict(orient="records")

for x in the_cz:
	result[x["Name"]]["cz"] = x

the_ms = ms.to_dict(orient="records")

for x in the_ms:
	result[x["Name"]]["ms"] = x

for x in result:
	print(result[x])

wf = open("formatted_citizenship.json", "w")

json.dump(result, wf, indent=4)

