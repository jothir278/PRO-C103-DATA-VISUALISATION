import csv
import plotly.express as px
with open("Data.csv") as file:
	df = csv.DictReader(file)
	fig = px.scatter(df,x="country",y = "cases",color = "date",title = "Per Capita Income")
	fig.show()