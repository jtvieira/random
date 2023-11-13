import plotly.graph_objects as go


def plot(city_data):
    # Plotting the data
    fig = go.Figure()

    for city, df in city_data.items():
        fig.add_trace(
            go.Scatter(x=df["Datetime"], y=df["PM2.5"], mode="lines", name=city)
        )

    fig.update_layout(
        title="pm2.5 values over time for different cities",
        xaxis_title="Time",
        yaxis_title="pm2.5 values",
    )
    fig.show()
