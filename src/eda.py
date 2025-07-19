# src/eda.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, column, hue=None):
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x=column, hue=hue, kde=True, bins=30)
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.show()

def plot_box(df, x, y):
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f'{y} by {x}')
    plt.tight_layout()
    plt.show()
