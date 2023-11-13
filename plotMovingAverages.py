import plotly.graph_objects as go


def plot(city_data, pd_instance):
    fig = go.Figure()

    for city, df in city_data.items():
        # Calculate daily averages
        daily_avg = (
            df.groupby([df["Year"], df["Month"], df["Day"]])["PM2.5"]
            .mean()
            .reset_index()
        )
        daily_avg["Datetime"] = pd_instance.to_datetime(
            daily_avg["Year"].astype(str)
            + "-"
            + daily_avg["Month"].astype(str)
            + "-"
            + daily_avg["Day"].astype(str),
            format="%Y-%m-%d",
        )

        # Calculate 5-day moving averages
        daily_avg["5-day MA"] = daily_avg["PM2.5"].rolling(window=5).mean()

        # Plot daily averages
        fig.add_trace(
            go.Scatter(
                x=daily_avg["Datetime"],
                y=daily_avg["PM2.5"],
                mode="lines",
                name=f"{city} Daily Avg",
            )
        )

        # Plot 5-day moving averages
        fig.add_trace(
            go.Scatter(
                x=daily_avg["Datetime"],
                y=daily_avg["5-day MA"],
                mode="lines",
                name=f"{city} 5-day MA",
                line=dict(dash="dash"),
            )
        )

    fig.update_layout(
        title="Daily Averages and 5-day Moving Averages of pm2.5 values for different cities",
        xaxis_title="Time",
        yaxis_title="pm2.5 values",
    )
    fig.show()
