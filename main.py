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

# Step 1: Calculate weights using demo data
# makeWeights(f) - f = fileName

# Step 2: 

categoryResults("Overall.csv")