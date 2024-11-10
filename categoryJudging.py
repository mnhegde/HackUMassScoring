from getData import getData
import json, csv
from helper import fileData, compileData

def categories(f):
    weights, tableMap, nameMap = fileData()

    # Weights are for 35 points initially
    for k in weights.keys(): weights[k] *= 60/35

    # Get overall scores based on judge weights
    projectScores, judgeScores = getData(f, weights, True, False)

    finalScores = []
    for k, v in projectScores.items(): finalScores.append([k, sum(v) / len(v)])

    with open("categoryMap.json", "r") as f:
        categoryMap = json.loads(f.read())

    finalOutput = {}
    for table, score in finalScores:
        if categoryMap[str(table)] not in finalOutput: finalOutput[categoryMap[str(table)]] = []
        finalOutput[categoryMap[str(table)]].append([table, score])

    for k, v in finalOutput.items():
        v.sort(key=lambda x: x[1], reverse=True)
        res = compileData(min(20, len(v)), v, tableMap, nameMap)
        if k == "[HACKUMASS] Best UI/UX": k = "[HACKUMASS] Best UI or UX"
        with open(f"Category-{k}-Results.csv", "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerows(res)


