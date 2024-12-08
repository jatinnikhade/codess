import numpy as np
import pandas as pd

data=np.array([[1,2,3],[4,5,6,],[7,8,9,]])
cplumn_names =['column_A','column_B','column_c']
df= pd.DataFrame(data, columns= cplumn_names)
print(df)