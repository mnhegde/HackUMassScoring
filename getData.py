import pandas as pd

def getData(f, weights={}, category=False):
    data = pd.read_csv(f)
    projectScores, judgeScores = {}, {}

    # Get all names of judges
    for i, r in data.iterrows():
        if r["Table Number"] not in projectScores: projectScores[r["Table Number"]] = []
        if r["Email Address"] not in judgeScores: judgeScores[r["Email Address"]] = {}

        total = 0
        total += r["Innovation Score"]
        total += r["Functionality Score"]
        total += r["Practicality Score"]
        total += r["Presentation Score"]
        
        if weights: 
            total += r["Q & A Score"] + weights[r["Email Address"]]
        if category: 
            total += r["Category Fit Score"]

        # Add point total to project score and for judge
        projectScores[r["Table Number"]].append(total)
        judgeScores[r["Email Address"]][r["Table Number"]] = total
    
    return projectScores, judgeScores