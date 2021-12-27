import pandas as pd
import csv
import plotly.graph_objects as pk
import plotly.express as px
 
bf=pd.read_csv("data.csv")

level=bf.groupby("level")["attempt"].mean()
print (level)

fig=pk.Figure(pk.Bar(x=level,y=["level1","level2","level3","level4"],orientation='h')) 
fig.show()
 
mean=bf.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig2=px.scatter(mean,x="student_id",y="level",color="attempt")
fig2.show()
