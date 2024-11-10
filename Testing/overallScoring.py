import pandas as pd
import math, json
from Testing.getScores import getData

with open("weights.json", "r") as f:
    weights = json.loads(f.read())

# Get overall scores based on judge weights
projectScores, judgeScores = getData("Overall.csv", weights, False)

judgeData = json.dumps(judgeScores)
with open("judgeData.json", "w") as f:
    f.write(judgeData)

projectData = json.dumps(projectScores)
with open("projectData.json", "w") as f:
    f.write(projectData)

