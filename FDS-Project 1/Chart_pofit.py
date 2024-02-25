import pandas as pd
import matplotlib.pyplot as plt

def chart_pofit (x='Các cột đánh giá') :
    df = pd.read_csv("Group Stock.csv" ,index_col='Date')
    df = df.drop(columns=["Unnamed: 0"])
    mean_simple_return_day = 0
    mean_simple_return_year = 0
    mean_simple_return_array_day = []
    mean_simple_return_array_year = []
    for i in x :
        mean_simple_return_day = df[i].mean()
        mean_simple_return_year=mean_simple_return_day*365
    data_visual = pd.DataFrame({'Stock': price, 'Daily_Return': mean_simple_return_array_day, 'Weekly_Return': mean_simple_return_array_year})

    plt.figure(figsize=(12, 8))
    sns.barplot(x='Stock', y='Weekly_Return', data=data_visual, color='salmon', alpha=0.7, label='Weekly Return')
    plt.xticks(rotation=45)
    plt.xlabel('Stock')
    plt.ylabel('Average Return')
    plt.title('Average Weekly Returns of Stocks')
    plt.legend()
    plt.show()
    