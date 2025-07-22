import pandas as pd


df = pd.read_csv("GiveMeSomeCredit/cs-training.csv")

print(df.info())
print("*"*50)


df2 = pd.read_csv("GiveMeSomeCredit/cs-test.csv")

print(df2.info())


