import pandas as pd

df = pd.read_csv("../data/dataset.csv")


df_z = (df - df.mean()) / df.std()
anomaly_mask = df_z.abs() > 2

df["anomaly_count"] = anomaly_mask.sum(axis = 1)
df["anomaly_score"] = df_z.abs().sum(axis = 1)

print("---- FINAL DATASET ----")
print(df)