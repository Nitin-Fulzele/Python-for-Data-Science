

import pandas as pd
import numpy as np 
emp = { "name":["nitin", "pawan", "saleem",], 
       "age":[35,45,40],
       "city":["nagpur","pune","mumbai"],
       "sal":[25000,35000,45000], 
       "Dept":["HR","IT","INFRA"]}

df=pd.DataFrame(emp)

print(df)