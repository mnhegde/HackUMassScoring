import json
from Testing.getScores import getData

with open("weights.json", "r") as f:
    weights = json.loads(f.read())

with open("projectData.json", "r") as f:
    projectData = json.loads(f.read())

for k in weights.keys(): weights[k] *= 0.5

projectScores, judgeScores = getData("Category.csv", weights)
