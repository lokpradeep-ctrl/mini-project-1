import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("trades_orderbook_STUDENT_dirty.csv", dtype=str)
df["price"] = pd.to_numeric(df["price"].str.replace(r"[$,]", "", regex=True), errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"].str.replace(r"[$,]", "", regex=True), errors="coerce")

print(df.describe())                                   
print(df["side"].value_counts(dropna=False))           
print(df["symbol"].value_counts(dropna=False))        
print(df[["price", "quantity"]].agg(["min", "max", "mean", "median"]))
