import pandas as pd


df = pd.read_csv("GiveMeSomeCredit/cs-training.csv")

print(df.info())
print("*"*50)
print(df.describe())