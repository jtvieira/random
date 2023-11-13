import plotly.graph_objects as go
import pandas as pd


def monthly_averages_for_years(city_data, years):
    month_map = {3: "March", 4: "April", 5: "May", 6: "June"}
    month_order = ["March", "April", "May", "June"]  # Define the desired order

    combined_data = pd.concat(city_data.values())
    filtered_data = combined_data[
        (combined_data["Month"].isin([3, 4, 5, 6]))
        & (combined_data["Year"].isin(years))
    ]
    monthly_avg = filtered_data.groupby(["Year", "Month"])["PM2.5"].mean().reset_index()
    # Replace month numbers with month names
    monthly_avg["Month"] = monthly_avg["Month"].replace(month_map)
    # Set the Month column to be categorical with a specific order
    monthly_avg["Month"] = pd.Categorical(
        monthly_avg["Month"], categories=month_order, ordered=True
    )

    pivot_table = monthly_avg.pivot(index="Month", columns="Year", values="PM2.5")
    return pivot_table


def plot(city_data):
    years = [2018, 2019, 2020, 2021, 2022, 2023]
    pivot_table = monthly_averages_for_years(city_data, years)

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["Month", "2018", "2019", "2020", "2021", "2022", "2023"]
                ),
                cells=dict(
                    values=[pivot_table.index]
                    + [pivot_table[year].tolist() for year in years]
                ),
            )
        ]
    )
    fig.show()
