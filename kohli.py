import pandas as pd

df=pd.read_csv("Virat_Kohli.csv")
# print(df)
# print(df.head(10))
# print(df.tail(10))
# df.info()
# print(df.shape)
# print(df["Opposition"].describe())
# run_freq=df["Runs"].value_counts()
opp_freq=df["Opposition"].value_counts()
# print(opp_freq)
new_df=df[["Runs","SR","Opposition"]]
# print(new_df)
vs_aussies=df[df["Opposition"]=="v Australia"]
# print(vs_aussies)
century=df[df["Runs"]>=100]
# print(century)
strike_rate=df[df["SR"]>100]
# print(strike_rate)
srilanka_100=df[(df["Opposition"]=="v Sri Lanka") & (df["Runs"]>=100)]
# print(srilanka_100)
def find_cent(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"
df["Centuries"]=df["Runs"].apply(find_cent)
print(df)