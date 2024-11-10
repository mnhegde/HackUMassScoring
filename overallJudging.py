import pandas as pd
from getData import getData
import json

with open("weights.json", "r") as f:
    weights = json.loads(f.read())

# Get overall scores based on judge weights
projectScores, judgeScores = getData("Overall.csv", weights, False)