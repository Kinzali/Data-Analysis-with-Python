import plotly.graph_objects as go
import pandas as pd

# Read the CSS file into a Pandas DataFrame
data = pd.read_csv("/sample_data.csv")
print(data.head())

# Create the first graph showing CQI by sector
fig1 = go.Figure()
for sector in data["Product"].unique():
    fig1.add_trace(go.Box(
        x=data.loc[data["Product"] == sector]["Product"],
        y=data.loc[data["Product"] == sector]["Revenue"],
        name=sector
    ))
fig1.update_layout(
    title="Revenue by Product",
    xaxis_title="Product",
    yaxis_title="Revenue"
)

# Display the graphs
fig1.show()

