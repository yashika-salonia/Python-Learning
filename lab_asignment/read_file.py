import pandas as pd

df=pd.read_csv('sData.csv')

# roll no input
roll=int(input("Enter roll no: "))

# try and except block to handle errors
try:
    
    # df['roll_no'] == roll checks which rows match the roll number you entered.
    student=df[df['roll_no']==roll].iloc[0] 
    # .iloc[0] means: “get the first row from the filtered results.”
    
    print(student.to_dict())
    # .to_dict() converts it to a Python dictionary

except IndexError:
    print("Roll number not found.")