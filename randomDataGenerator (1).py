
import json
import pickle
import numpy as np
import pandas as pd

COLOMNS = 5
ROWS = 50
VARIANTS = 6

raspred = np.random.laplace
df = pd.DataFrame

var = 1
while var < VARIANTS+1:
    # print(f"var={var}")

    data = np.stack(
        [raspred(10 + np.random.randint(1, var + 1), 10 + np.random.randint(1, var + 1), ROWS) for i in range(COLOMNS)],
        axis=1)
    for i in np.random.randint(0, ROWS, np.random.randint(7, 10)):
        j = np.random.randint(0, COLOMNS)
        data[i][j] += np.random.randint(50, 250)

    headers = [("col%d%d" % (var, i)) for i in range(COLOMNS)]
    # print(headers)

    df = pd.DataFrame(data, columns=headers)
    df.to_csv(f"/Users/deniskozachenko/Desktop/var{var}.csv")
    #df.to_csv(f"data/var{var}.csv")
    
    var += 1






