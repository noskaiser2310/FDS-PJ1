import pandas as pd
import plotly.express as px


def chart_general(x):
    x = df[price]
    df_price_new = x / df_price.iloc[0]
    fig = px.line(data_frame=df_price_new)
    fig.show()
