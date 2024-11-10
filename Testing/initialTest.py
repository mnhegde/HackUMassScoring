import pandas as pd
import csv
import math

# Retrieve judging data on projects

data = pd.read_csv("HackUMass Mock Judging - JudgeSoftware (1).csv")

# Keep track of scores for each project
projectScores = {}

# Keep track of scores for each judge
judgeScores = {}

# For each row of data, get the total points given to project by judge and save
for i, r in data.iterrows():
    groupName = f"{r["Email Address"]} ({r["Table Name"]})"
    if groupName not in projectScores: projectScores[groupName] = []
    if groupName not in judgeScores: judgeScores[groupName] = {}

    total = 0
    total += r["Innovation Score"]
    total += r["Functionality Score"]
    total += r["Presentation Score"]
    total += r["Q & A Score"]

    # Add point total to project score and for judge
    projectScores[groupName].append(total)
    judgeScores[r["Email Address"]][groupName] = total

# Get average score for each project
projectAvg = {}
for k, v in projectScores.items(): projectAvg[k] = sum(v) / len(v)

# For every judge, get their difference between their score and the project's average across all projects
# Assign this as their personal weight to be added to scores to normalize judging
newScores = {}
judgeMetrics = {}
totalMetric = 0
for judge, scores in judgeScores.items():
    # Metric stores total difference
    metric = 0
    for proj, avg in projectAvg.items():
        metric += (scores[proj] - avg)
    
    # Get avg difference across all projects, and inverse as this is the direction we want score to move
    # (If metric was positive, this means we want to move the score lower and vice versa)
    metric /= -len(projectAvg)

    # For each of the judge's scores, we add this metric for the new score
    # newJudgeScores = {}
    # for k, s in scores.items():
    # newJudgeScores[k] = s + metric
    # newScores[judge] = newJudgeScores

    totalMetric += metric # Keep track of totalMetric from all judges
    judgeMetrics[judge] = metric

print(f"Total: {totalMetric}")

# Write new scores to CSV to compare result
# Testing data
writeData = [["Judge", "Project", "Old Score", "New Score"]]
for judge, scores in judgeScores.items():
    for proj, values in scores.items():
        line = [judge, proj, values, newScores[judge][proj]]
        writeData.append(line)

with open("newScores.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(writeData)


print(judgeMetrics)
testData = pd.read_csv("JD2 - assignments.csv")
oldProjectScores = {}
newProjectScores = {}
newJudgeData = []
for i, r in testData.iterrows():
    newScores = [r[0]]
    for i, v in enumerate(r[1:]):
        if not math.isnan(v):
            newScores.append(v + judgeMetrics[r[0]])
        else: newScores.append("")
    newJudgeData.append(newScores)

with open("testScores.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(newJudgeData)

