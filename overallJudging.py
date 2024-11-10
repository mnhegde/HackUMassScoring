import pandas as pd
from getData import getData
import json, csv

with open("weights.json", "r") as f:
    weights = json.loads(f.read())

# Weights are for 35 points initially
for k in weights.keys(): weights[k] *= 40/35

# Get overall scores based on judge weights
projectScores, judgeScores = getData("Overall.csv", weights, False, False)

finalScores = []
for k, v in projectScores.items(): finalScores.append([k, sum(v) / len(v)])
finalScores.sort(key=lambda x: x[1], reverse=True)

with open("GeneralResults.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(["Table Number", "Overall Score"])
    wr.writerows(finalScores)

