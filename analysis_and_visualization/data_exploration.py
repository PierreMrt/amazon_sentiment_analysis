from data_cleaning.data_management import DataManager
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from collections import Counter


INPUT_PATH = 'data_cleaning/data/{category}_cleaned_output.csv'


class DataExplorer:
    def __init__(self, category):
        self.df = pd.read_csv(INPUT_PATH.format(category=category))
        self.positive = self.create_list('positive')
        self.negative = self.create_list('negative')

    def review_numbers(self):
        df = self.df.groupby('sentiment')['reviews'].count()
        labels = ['negative',  'positive']
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
        ax.pie(df, autopct=lambda pct: self.plot_values(pct, df), labels=labels)
        plt.show()

    @staticmethod
    def plot_values(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    @staticmethod
    def create_wordclouds(fig, i, sentiment, text):
        wordcloud = WordCloud(max_font_size=50, max_words=100).generate(text)
        ax = fig.add_subplot(2, 2, i)
        ax.imshow(wordcloud)
        ax.title.set_text(f"{sentiment} reviews")
        ax.axis('off')
        return wordcloud

    def create_list(self, sentiment):
        df = self.df[(self.df['sentiment'] == sentiment)]
        return ' '.join([str(i) for i in df['reviews']]).split()

    def create_text_from_df(self, sentiment):
        df = self.df[(self.df['sentiment'] == sentiment)]
        return " ".join(str(review) for review in df['reviews'])

    @staticmethod
    def plot_frequency(fig, col, i, sentiment, ls):
        freq = Counter(ls).most_common()[:10]
        x = [x[0] for x in freq]
        y = [y[1] for y in freq]
        ax = fig.add_subplot(2, col, 2 * (col - 1) + i)
        ax.bar(x, y)
        ax.set_title(sentiment)

        return ax


def explore_data():
    explorer = DataExplorer('computers')
    explorer.review_numbers()

    fig = plt.figure()
    for i, sentiment in enumerate(['positive', 'negative'], 1):
        text = explorer.create_text_from_df(sentiment)
        wordcloud = explorer.create_wordclouds(fig, i, sentiment, text)

    for i, sentiment in enumerate([('positive', explorer.positive), ('negative', explorer.negative)], 1):
        ax = explorer.plot_frequency(fig, 2, i, '', sentiment[1])

    plt.show()

    fig = plt.figure()
    for i, sentiment in enumerate([('positive', explorer.positive), ('negative', explorer.negative)], 1):
        not_freq = []
        for index, word in enumerate(sentiment[1]):
            if word == 'not':
                not_freq.append('not ' + sentiment[1][index + 1])

        ax = explorer.plot_frequency(fig, 1, i, sentiment[0], not_freq)

    plt.show()
