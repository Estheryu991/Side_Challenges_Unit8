from locale import normalize
from modulefinder import ModuleFinder
from numpy import compare_chararrays
import requests
import pandas as pd
import json
import numpy as np

# Replace this with your token (available on hackathon.unit8.com, after logging in)
# If your request returns {'detail': 'Invalid token.'} then you did not correctly set this variable
TOKEN_ID = '61259af05fdbca4da869e4838b15dc2cccbc53f7'

if __name__ == '__main__':

    submission_side_challenge = {"challenge_id":10} 
    response = requests.get('https://hackathon.unit8.com/api/get_resource',
                            headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
                            json=submission_side_challenge
                            )

    data_json = response.json()
    
    df = pd.read_json(data_json)

    df["professional_mistakes"]  = (df["professional_mistakes"]-df["professional_mistakes"].min())/(df["professional_mistakes"].max()-df["professional_mistakes"].min())
    df["days_off"]  = (df["days_off"]-df["days_off"].min())/(df["days_off"].max()-df["days_off"].min())
    df["calls_made"]  = (df["calls_made"]-df["calls_made"].min())/(df["calls_made"].max()-df["calls_made"].min())
    df["sales_made"]  = (df["sales_made"]-df["sales_made"].min())/(df["sales_made"].max()-df["sales_made"].min())
    df["behaviour"]  = (df["behaviour"]-df["behaviour"].min())/(df["behaviour"].max()-df["behaviour"].min())


    #!ModuleFinder
    df['actual'] = df['sales_made'] / df['calls_made'] *0.1 
    df["king"]= df["actual"]+ df["behaviour"] - df["professional_mistakes"] - df["days_off"]

    df = df.sort_values(by='king', ascending=False, na_position='first')

    print(df)
    df.max()
    column = df["king"]
    max_value = column.max()


response=requests.post(
  'https://hackathon.unit8.com/api/submit',
  headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
  json={'challenge_id': 13, 'submission': "8"
  }
)
print(response.json())
