import pandas as pd


def read_datas(x):
    df = pd.read_csv(x)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.drop(columns=["Unnamed: 0"])
    df.set_index("Date", inplace=True)
    df.head(10)
