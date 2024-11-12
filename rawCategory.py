import json, csv
from getData import getData
from helper import compileData

def rawCategories(fileName):
    with open("categoryMap.json", "r") as f:
        categoryMap = json.loads(f.read())

    projectScores, judgeScores = getData(fileName, {}, True, False, (6, 60))

    finalScores = []
    for k, v in projectScores.items(): finalScores.append([k, sum(v) / 3])

    with open("categoryMap.json", "r") as f:
        categoryMap = json.loads(f.read())

    finalOutput = {}
    for table, score in finalScores:
        if categoryMap[str(table)] not in finalOutput: finalOutput[categoryMap[str(table)]] = []
        finalOutput[categoryMap[str(table)]].append([table, score])

    for k, v in finalOutput.items():
        v.sort(key=lambda x: x[1], reverse=True)
        res = compileData(v)
        if "/" in k: k = k.replace("/", " or ")
        with open(f"Raw/Raw-Category-{k}-Results.csv", "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerows(res)