"""
src/eda.py

This module contains functions for exploratory data analysis (EDA) on the fraud detection datasets.
"""
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, column, hue=None): #Plot the distribution of a column, optionally colored by a hue.
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x=column, hue=hue, kde=True, bins=30)
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.show()

def plot_box(df, x, y): #Plot a boxplot of y grouped by x.
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f'{y} by {x}')
    plt.tight_layout()
    plt.show()
