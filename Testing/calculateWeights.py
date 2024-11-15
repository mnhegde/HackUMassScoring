import json
from Testing.getScores import getData

projectScores, judgeScores = getData("Overall.csv")

# Get avg score for each project
projectAvg = {}
for k, v in projectScores.items(): projectAvg[k] = sum(v) / len(v)

# For every judge, get their difference between their score and the project's average across all projects
# Assign this as their personal weight to be added to scores to normalize judging
newScores, judgeMetrics = {}, {}
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

# Save all info into json files (weights and project scores)
weights = json.dumps(judgeMetrics)
with open("weights.json", "w") as f:
    f.write(weights)
