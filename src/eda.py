# src/eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column, hue=None):
    sns.histplot(data=df, x=column, hue=hue, kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_box(df, x, y):
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f'{y} by {x}')
    plt.show()
