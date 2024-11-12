import pandas as pd
import json

f = "(Public) HackUMass Public Roster - Final Project Roster.csv"
teamData = pd.read_csv(f)
categoryMap = {}
nameMap = {}
devpostMap = {}
for i, r in teamData.iterrows():
    categoryMap[r["Table Assignment"]] = r["Which [Hackumass] Prize Category Are You Opting For?"]
    nameMap[r["Table Assignment"]] = r["Project Title"]
    devpostMap[r["Table Assignment"]] = r["Submission Url"]

with open("categoryMap.json", "w") as f:
    f.write(json.dumps(categoryMap))

with open("nameMap.json", "w") as f:
    f.write(json.dumps(nameMap))

with open("devpostMap.json", "w") as f:
    f.write(json.dumps(devpostMap))