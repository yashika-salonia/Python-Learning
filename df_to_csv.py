import pandas as pd
df=pd.DataFrame({'Name':['a','b','c'],'Marks':[90,80,70]})
df.to_csv("demo.csv",index=False) # not include index
# df.to_csv("newDemo.csv",index=True) #makes index visible

df['Age']=[20,40,30]
print(df)

#null - Isnumm().sum