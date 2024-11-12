import pandas as pd
from getData import getData
import json, csv
from helper import fileData, compileData

def overall(f):
    weights, tableMap, nameMap = fileData()

    # Weights are for 35 points initially
    # for k in weights.keys(): weights[k] *= 40/35

    # Get overall scores based on judge weights
    projectScores, judgeScores = getData(f, weights, False, False, (5, 40))

    finalScores = []
    for k, v in projectScores.items(): finalScores.append([k, sum(v) / 3])
    finalScores.sort(key=lambda x: x[1], reverse=True)
    res = compileData(finalScores, tableMap, nameMap)

    with open("Results/GeneralResults.csv", "w") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerows(res)

