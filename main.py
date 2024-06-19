from typing import Union

from fastapi import FastAPI

import os
import cohere
import pandas as pd
from IPython.display import clear_output

os.environ['COHERE_API_KEY'] = 'yARQQpDOyath4wS5cphHJooAbgUQslMTaT6gEmyP'
co = cohere.Client(api_key=os.getenv('COHERE_API_KEY'))
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


app = FastAPI()
@app.get("/")
def read_root():
    def get_completion(prompt, temp=0):
        response = co.generate(
            model='command-r-plus',
            prompt=prompt,
            max_tokens=5000,
            temperature=temp)
        return response.generations[0].text
        
    Apex_Data = f"""Tools_Release, Tools_Build, Feature,Status,Point_of_contact,P1_Bugs, P2_Bugs,P1_Bugs_Unfixed, P2_Bugs_Unfixed,Comment
    8.61, 132W, Decimal Precision,In Progress,Murali,4,6,1,3,50% Complete
    8.62, 120W, CREF Description Update,Completed,Hamesh,1,3,1,1,Completed Last week
    8.62, 114W, Apex Project,Not Started,Sangeetha,0,0,0,0,Will start next week
    8.63, 102R, Fluid Grid Personalization,On Hold,Balaji,5,1,1,1,Tools environment is not stable
    8.61, 902W, OpenSearch enhancements, Completed,Samudrip,5,6,4,6,Completed with delay.
    8.61, 140W, Homepage Refresh, Completed, Sangeetha, 1,1,0,0, 
    """

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

    
