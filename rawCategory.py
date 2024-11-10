import json, csv
from getData import getData

with open("categoryMap.json", "r") as f:
    categoryMap = json.loads(f.read())


projectScores, judgeScores = getData("Overall.csv", {}, True, False)

finalScores = []
for k, v in projectScores.items(): finalScores.append([k, sum(v) / len(v)])

with open("categoryMap.json", "r") as f:
    categoryMap = json.loads(f.read())

finalOutput = {}
for table, score in finalScores:
    if categoryMap[table] not in finalOutput: finalOutput[categoryMap[table]] = []
    finalOutput[categoryMap[table]].append([table, score])

for k, v in finalOutput.items():
    v.sort(key=lambda x: x[1], reverse=True)
    with open(f"Category-{k}-Results.csv", "w") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(["Table Number", "Overall Score"])
        wr.writerows(v)