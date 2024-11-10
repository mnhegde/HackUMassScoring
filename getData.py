import pandas as pd

def getData(f, weights={}, category=False, test=True):
    data = pd.read_csv(f)
    projectScores, judgeScores = {}, {}

    # Get all names of judges
    for i, r in data.iterrows():
        if not test and r["Table Number"] != r["Please Enter the Table Number Once More"]: continue
        
        if r["Table Number"] not in projectScores: projectScores[r["Table Number"]] = []
        if r["Email Address"] not in judgeScores: judgeScores[r["Email Address"]] = {}

        total = 0
        total += r["Innovation Score"]
        total += r["Functionality Score"]
        total += r["Practicality Score"]
        total += r["Presentation Score"]
        # Initially 35 points
        if not test:
            total += r["Q & A Score"] + weights.get(r["Email Address"], 0)
            if category: total += r["Category Fit Score"] * 2 # We want this 20 points total

        # Add point total to project score and for judge
        projectScores[r["Table Number"]].append(total)
        judgeScores[r["Email Address"]][r["Table Number"]] = total
    
    return projectScores, judgeScores