import math
import itertools
import numpy as np
import pandas as pd

def multinomial_prob(k, z, p):
    prob = math.factorial(k)
    for i in range(len(z)):
        prob /= math.factorial(z[i])
        prob *= p[i]**z[i]
    return prob

preds = pd.read_csv("DSTG_Result/predict_output.csv", index_col=0)
true = pd.read_csv("DSTG_Result/true_output.csv", index_col=0)
true["Blood"] = 0.0
k = 10
n = 7

p = preds.div(preds.sum(axis=1), axis=0)
map = k * p
map = map.applymap(np.floor)

print(map.head())
print(true.head())

for index, row in map.iterrows():
    sum = np.sum(row)
    if sum < k:
        diff = int(k - sum)

        spots = list(range(1, n + 1))
        combinations = itertools.combinations_with_replacement(spots, diff)

        max_prob = 0.0
        map_z = []
        for combo in combinations:
            z = map.iloc[index].tolist()
            for i in range(diff):
                z[combo[i]-1] = z[combo[i]-1] + 1

                prob = multinomial_prob(k, z, p.iloc[index].tolist())

                if prob > max_prob:
                    max_prob = prob
                    map_z = z

        map.iloc[index] = np.array(map_z)

pred_prop = map / 10
rmse = np.sum((pred_prop-true)**2) / (7*260)
rmse = np.sum(rmse)
rmse = np.sqrt(rmse)
print(pred_prop.head())
print(rmse)