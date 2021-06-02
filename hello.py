import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("python.csv")
student_df = df.loc[df["student_id"] == "TRL_xyz"]
print(student_df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = student_df.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    # 'h' denotes horizontal bar graph
    orientation = 'h'
))
fig.show()