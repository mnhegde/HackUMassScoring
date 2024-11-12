import csv, json

res = [["Name", "Devpost"]]

with open("devpostMap.json", "r") as f:
    devposts = json.loads(f.read())

with open("nameMap.json", "r") as f:
    nameMap = json.loads(f.read())

for k, v in nameMap.items():
    res.append([v, devposts[k]])

with open("Devposts.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(res)