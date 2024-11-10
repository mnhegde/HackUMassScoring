import pandas as pd
import json

# Raw data from judges
data = pd.read_csv("Overall.csv")

tableMap = {}
for i, r in data.iterrows():
    if r["Table Number"] not in tableMap: tableMap[r["Table Number"]] = []
    tableMap[r["Table Number"]].append(dict(r))

with open("tableMap.json", "w") as f:
    f.write(json.dumps(tableMap))