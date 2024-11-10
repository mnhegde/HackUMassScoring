import pandas as pd
import json

f = "test"
teamData = pd.read_csv(f)
categoryMap = {}
for i, r in teamData.iterrows():
    categoryMap[r["Table Assignment"]] = r["Which [Hackumass] Prize Category Are You Opting For?"]

with open("categoryMap.json", "w") as f:
    f.write(json.dumps(categoryMap))