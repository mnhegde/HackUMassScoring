import pandas as pd
import math

def getData(f, weights={}, category=False):
    data = pd.read_csv(f)
    projectScores, judgeScores = {}, {}

    # Get all names of judges
    for i, r in data.iterrows():
        groupName = f"{r["Email Address"]} ({r["Table Name"]})"
        if groupName not in projectScores: projectScores[groupName] = []
        if groupName not in judgeScores: judgeScores[groupName] = {}

        total = 0
        total += r["Innovation Score"]
        total += r["Functionality Score"]
        total += r["Practicality Score"]
        total += r["Presentation Score"]
        
        if weights: total += r["Q & A Score"]
        if category: total += r["Category Fit Score"]

        # Add point total to project score and for judge
        projectScores[groupName].append(total)
        judgeScores[r["Email Address"]][groupName] = total
    
    return projectScores, judgeScores