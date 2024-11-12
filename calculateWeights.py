import pandas as pd
from getData import getData
import json, math

# Demo data to create weights - Give correct csv here
def calcWeights(f):
    projectScores, judgeScores = getData(f)

    # Get avg score for each project
    projectAvg = {}
    for k, v in projectScores.items(): projectAvg[k] = sum(v) / len(v)

    newScores, judgeMetrics = {}, {}
    totalMetric = 0
    for judge, scores in judgeScores.items():
        metric = 0
        count = 0
        for proj, avg in projectAvg.items():
            if proj in scores:
                metric += (scores[proj] - avg) # Make this subtraction if changed
                count += 1
        
        # Get avg difference across all projects, and inverse as this is the direction we want score to move
        # (If metric was positive, this means we want to move the score lower and vice versa)
        metric /= -count # Divide by -count instead for new weight
        # metric /= count
        metric = max(metric, -5)
        metric = min(metric, 5)
        # metric = 1 / metric # Don't need this if changed

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