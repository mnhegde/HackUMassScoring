import json, math

def fileData():
    with open("weights.json", "r") as f:
        weights = json.loads(f.read())

    with open("tableMap.json", "r") as f:
        tableMap = json.loads(f.read())

    with open("nameMap.json", "r") as f:
        nameMap = json.loads(f.read())
    
    return weights, tableMap, nameMap

def compileData(k, scores, tableMap=None, nameMap=None):
    if not tableMap or not nameMap:
        tableMap, nameMap = fileData()[1:]

    res = [["Team Name", "Average Score", "Written Feedback (3 Sentences Max Please)"]]
    criteria = ["Innovation Score", "Functionality Score", "Practicality Score", "Presentation Score", "Q & A Score", "Category Fit Score", "Written Feedback (3 Sentences Max Please)"]
    for tableNum, s in scores[:k]:
        rows = tableMap[str(tableNum)]
        newRow = [nameMap[str(tableNum)], s]
        feedback = ""
        for r in rows: 
            if type(r["Written Feedback (3 Sentences Max Please)"]) == str or not math.isnan(r["Written Feedback (3 Sentences Max Please)"]):
                feedback += r["Written Feedback (3 Sentences Max Please)"] + "\n"
        # for c in criteria: newRow.append(row[c])
        newRow.append(feedback)
        res.append(newRow)
    
    return res