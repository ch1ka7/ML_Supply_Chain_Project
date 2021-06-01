import pandas as pd
from apyori import apriori

# N is a number of columns to import from csv file
N = 10

# read data from csv file and put it in dataframe
df = pd.read_csv("groceries.csv", header=None, names=range(N), na_filter=True)

# create a list of lists removing "nan" value
transactions = df.T.apply(lambda x: x.dropna().tolist()).tolist()
# print(transactions)

# apply apriori algorithm

association_rules = apriori(transactions, min_support=0.011, min_confidence=0.2, min_lift=3, min_length=2)
# association_results = list(association_rules)

# Fields of output mean:
#
# Base item.
# Appended item.
# Support.
# Confidence.
# Lift.

# Visualizing the list of rules
results = list(association_rules)
for i in results:
    print("\n")
    print(i)
    print("**********")

for item in results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    if len(items) == 2:
        print("\n")
        print("Rule: " + items[0] + " -> " + items[1])

        print("Support: " + str(item[1]))

        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
    else:
        print("\n")
        print("Rule: " + items[0] + ", " + items[1] + ", " + items[2])

        print("Support: " + str(item[1]))

        print(str(item[2][0][0]) + " -> " + str(item[2][0][1]))

        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))

        print(str(item[2][1][0]) + " - > " + str(item[2][1][1]))

        print("Confidence: " + str(item[2][1][2]))
        print("Lift: " + str(item[2][1][3]))

        print("=====================================")
