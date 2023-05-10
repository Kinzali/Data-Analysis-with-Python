import plotly.graph_objects as go
import pandas as pd

# Read the CSS file into a Pandas DataFrame
data = pd.read_csv("/Users/attirehman/Documents/sample_data.csv")
print(data.head())

# Split the Sector column into two separate columns
data["Site"] = data["Sector"].str.split("_", n=1, expand=True)[0]
data["Sector"] = data["Sector"].str.split("_", n=1, expand=True)[1]

# Create the first graph showing CQI by sector
fig1 = go.Figure()
for sector in data["Sector"].unique():
    fig1.add_trace(go.Box(
        x=data.loc[data["Sector"] == sector]["Sector"],
        y=data.loc[data["Sector"] == sector]["CQI"],
        name=sector
    ))
fig1.update_layout(
    title="CQI by Sector",
    xaxis_title="Sector",
    yaxis_title="CQI"
)

# Create the second graph showing Users by site
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=data.groupby("Site")["Users"].sum().index,
    y=data.groupby("Site")["Users"].sum().values,
    name="Total Users"
))
fig2.add_trace(go.Bar(
    x=data.groupby("Site")["Users"].mean().index,
    y=data.groupby("Site")["Users"].mean().values,
    name="Average Users"
))
fig2.update_layout(
    title="Users by Site",
    xaxis_title="Site",
    yaxis_title="Users"
)

# Create the third graph showing Cell Throughput by sector
fig3 = go.Figure()
for sector in data["Sector"].unique():
    fig3.add_trace(go.Scatter(
        x=data.loc[data["Sector"] == sector]["Sector"],
        y=data.loc[data["Sector"] == sector]["Cell throughput"],
        mode="markers",
        name=sector
    ))
fig3.update_layout(
    title="Cell Throughput by Sector",
    xaxis_title="Sector",
    yaxis_title="Cell Throughput"
)

# Display the graphs
fig1.show()
fig2.show()
fig3.show()
