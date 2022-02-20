from locale import normalize
from modulefinder import ModuleFinder
from matplotlib.cbook import ls_mapper
from numpy import compare_chararrays
# import pandas_profiling
import requests
import pandas as pd
import json
from sklearn.linear_model import LinearRegression
import numpy as np
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Replace this with your token (available on hackathon.unit8.com, after logging in)
# If your request returns {'detail': 'Invalid token.'} then you did not correctly set this variable
# TOKEN_ID = '61259af05fdbca4da869e4838b15dc2cccbc53f7'

if __name__ == '__main__':

    
    response = requests.get('https://hackathon.unit8.com/api/get_resource',
    headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
    json={'challenge_id': 3})

#print(response.json())
df = pd.read_json(response.json())


#split VS ML Algorithm
x = df.loc[:, df.columns != "productivity"]

y = df["productivity"]


reg = LinearRegression().fit(x,y)

#print(x, y)

#print(reg.coef_)

# from pandas_profiling import ProfileReport
# profile = ProfileReport(dataJson, title = "Report", explorative=True)

response=requests.post(
  'https://hackathon.unit8.com/api/submit',
  headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
  json={'challenge_id': 3, 'submission': "feature_39"}
)
print(response.json())


# [1, 788, 894, 944, 967, ]
# MA Detection Disease 
# test

