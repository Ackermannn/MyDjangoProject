from utills import wash_data
import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.DataFrame(data=np.random.rand(10, 2))
    df[0][1] = 100
    df[0][2] = 99
    print(df)
    washedDf = wash_data(df)
    print(washedDf)
