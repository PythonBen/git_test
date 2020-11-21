import pandas as pd

df  = pd.read_csv('sampleSubmission.csv', nrows=100)

print(df.head())
print(df.tail())
