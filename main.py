import pandas as pd
import plotly.graph_objects as go
import generateFiles
import createDataframe
import os

if __name__ == "__main__":
    # URLs for the cities
    urls = {
        "NYC": "https://data.berkeleyearth.org/air-quality/local/United_States/New_York/New_York.txt",
        "LA": "https://data.berkeleyearth.org/air-quality/local/United_States/California/Los_Angeles.txt",
        "Houston": "https://data.berkeleyearth.org/air-quality/local/United_States/Texas/Houston.txt",
        "Phoenix": "https://data.berkeleyearth.org/air-quality/local/United_States/Arizona/Phoenix.txt",
        "San Diego": "https://data.berkeleyearth.org/air-quality/local/United_States/California/San_Diego.txt",
    }
    # Fetch and process data for all cities
    city_data = {}
    for city, url in urls.items():
        if not os.path.exists(f"{city}_output.txt"):
            generateFiles.generate(city, url)
        city_df = createDataframe.create(
            f"{city}_output.txt", 8 if city == "NYC" else 10
        )
        city_data[city] = city_df

    import plotAllValues

    plotAllValues.plot(city_data)

    import plotMovingAverages

    plotMovingAverages.plot(city_data, pd)

    import plotMonthlyAverages

    plotMonthlyAverages.plot(city_data)
