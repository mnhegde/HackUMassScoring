from calculateWeights import calcWeights
from overallJudging import overall
from categoryJudging import categories
from rawCategory import rawCategories

def makeWeights(f):
    calcWeights(f)


def overallResults(f):
    overall(f)


def categoryResults(f):
    categories(f)


def rawCategoryResults(f):
    rawCategories(f)

# Done:
# Calculate weights for each judge
# Create the name and category maps for each tableNumber

# toDo
# Create rowMap of all the rows in general data table to reference for final entries
# Once name, category, and row maps are done along with weights, run actual judging

# Overall and Category judging, raw Categorical as well

# Step 2: 

rawCategoryResults("Official Data.csv")