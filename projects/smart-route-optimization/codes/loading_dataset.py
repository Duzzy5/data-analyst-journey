import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df = pd.read_csv(r"C:\Users\Vishrant kumar Sahu\Downloads\archive (3)\indian-cities-dataset.csv")

df.head()

df = pd.read_excel(
    r"C:\Users\Vishrant kumar Sahu\Downloads\archive (3)\Intercity_Speed_Traffic_TravelTime_Analysis.xlsx",
    header=2
)

df.head()
print(df.info)
