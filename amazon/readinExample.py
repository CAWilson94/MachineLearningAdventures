#import numpy as np
#data = np.loadtxt('Advertising.csv', delimiter=',')

""" 
import pandas as pd
data = pd.read_csv(open('myfile.csv'))
target = data[target_column_name]
del data[target_column_name]

# Then fit a scikit-learn estimator
SVC().fit(data, target)
"""

import pandas as pd
data = pd.read_csv(open('Advertising.csv'))
#target is column 2
index_col = data.columns[3]
print index_col
target = index_col
print target

