import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
import pandas as pd


class PlotWeeklyPrice:
    def __init__(self, df):
        self.df = df

    def weekly_price(self, x):
        weekly_price = self.df[x].resample("W").mean()
        local_max_index = argrelextrema(weekly_price.values, np.greater)[0]
        local_min_index = argrelextrema(weekly_price.values, np.less)[0]
        local_max_prices = weekly_price.iloc[local_max_index]
        local_min_prices = weekly_price.iloc[local_min_index]
        plt.figure(figsize=(15, 8))
        weekly_price.plot(label="Giá Trung Bình Hàng Tuần")
        plt.scatter(
            local_max_prices.index,
            local_max_prices,
            color="red",
            label="Điểm Cao",
            marker="^",
        )
        plt.scatter(
            local_min_prices.index,
            local_min_prices,
            color="green",
            label="Điểm Thấp",
            marker="v",
        )
        plt.title(f"Biểu Đồ Biến Động {x} Hàng Tuần")
        plt.ylabel(f"Giá {x} (USD)")
        plt.xlabel("Ngày")
        plt.legend()
        plt.grid(True)
        return plt.show()
