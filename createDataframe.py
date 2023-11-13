import pandas as pd


def create(url, skip_rows=10):
    df = pd.read_csv(url, skiprows=skip_rows, delimiter="\t", header=None)
    df_headers = pd.read_csv(url, skiprows=skip_rows - 1, nrows=0, delimiter=",")
    df_headers = [i.replace(" ", "").replace("%", "") for i in df_headers]
    df.columns = list(df_headers)
    df["Datetime"] = pd.to_datetime(
        df["Year"].astype(str)
        + "-"
        + df["Month"].astype(str)
        + "-"
        + df["Day"].astype(str)
        + "-"
        + df["UTCHour"].astype(str),
        format="%Y-%m-%d-%H",
    )
    return df
