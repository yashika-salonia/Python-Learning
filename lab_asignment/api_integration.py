from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df=pd.read_csv('sData.csv')


@app.get('/student/{roll}')

def get_student(roll:int):
    try:
        student=df[df['roll_no']==roll].iloc[0] 

        return student.to_dict()

    except IndexError:
        
        return {'error': 'Roll number not found. \U0001F928'}