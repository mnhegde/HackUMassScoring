import pandas as pd
import json

f = "shi - Sheet1.csv"
teamData = pd.read_csv(f)
categoryMap = {}
nameMap = {}
for i, r in teamData.iterrows():
    categoryMap[r["Table Assignment"]] = r["Which [Hackumass] Prize Category Are You Opting For?"]
    nameMap[r["Table Assignment"]] = r["Project Title"]

with open("categoryMap.json", "w") as f:
    f.write(json.dumps(categoryMap))

with open("nameMap.json", "w") as f:
    f.write(json.dumps(nameMap))