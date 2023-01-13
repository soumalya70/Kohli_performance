import pandas as pd
data={
    "apples": [4,3,6,1],
    "oranges":[3,7,4,1]
}
index_titles=[
    "Aaron","Shun","James","Wilson"
]
df=pd.DataFrame(data,index=index_titles)
# print(df)
# (type(df))
print(df.loc["Aaron"])
print(df.loc["Aaron"]["apples"])
print(df["oranges"].iloc[0])
