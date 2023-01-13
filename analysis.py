import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Virat_Kohli.csv")
# print(df.head())

# Total no of runs
# print("Total number of runs: ",df["Runs"].sum())

# total number of balls he faced
# print("Total number of balls he faced: ",df["BF"].sum())

# avg strike rate
# print("AVg strike rate: ",df["SR"].mean())

#number of matches he has played at different postions
# print(df["Pos"].head(10))
positions=df["Pos"].unique()
# print(positions)

df["Pos"]=df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "batting at 2",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})
# print(df[["Runs","Pos"]])

# Total runs scored in differnt positions
pos_counts=df["Pos"].value_counts()
# print(pos_counts)
pos_counts_values=pos_counts.values
pos_counts_labels=pos_counts.index
# fig=plt.figure(figsize=(10,7))
# plt.pie(pos_counts_values,labels=pos_counts_labels)
# plt.show()

# total number of matches against differnt opposition
# print(df[["6s","Pos"]].head)
def show_pie(df,key):
    counts=df[key].value_counts()
    counts_values=counts.values
    counts_labels=counts.index
    plt.pie(counts_values,labels=counts_labels)
    plt.show()
# show_pie(df,"Opposition")
#number of matches played in different grounds
# show_pie(df,"Ground")
#total sixes scored in different positions
runs_at_pos=df.groupby("Pos")["6s"].sum()
# print(runs_at_pos)
runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index
fig=plt.figure(figsize=(10,7))
# plt.bar(
#     runs_at_pos_labels,
#     runs_at_pos_values,
#     color="green",
#     width=0.3
# )
# plt.show()
#Total runs scored in different countries
total_runs=df.groupby("Opposition")["Runs"].sum()
total_runs_values=total_runs.values
total_runs_labels=total_runs.index
# plt.bar(
#     runs_at_pos_labels,
#     runs_at_pos_values,
#     color="blue",
#     width=0.3
# )
# plt.show()
#Number of centuries scored by him in 1st innings
centuries=df.query("Runs >= 100")
# print(centuries)
inninigs=centuries["Inns"].value_counts()
# print(inninigs)
plt.pie(inninigs.values,labels=inninigs.index)
plt.show()