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

    def review_numbers(self, fig):
        df = self.df.groupby('sentiment')['reviews'].count()
        labels = ['negative',  'positive']
        ax = fig.add_subplot(121)
        ax.pie(df, autopct=lambda pct: self.plot_pie_values(pct, df), labels=labels)
        ax.set_title('Sentiment distribution of the reviews')

    @staticmethod
    def plot_pie_values(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    def review_length(self, fig):
        length_positive = list(self.df.loc[self.df['sentiment'] == 'positive']['reviews'])
        length_positive = [str(w) for w in length_positive]
        length_negative = list(self.df.loc[self.df['sentiment'] == 'negative']['reviews'])
        length_negative = [str(w) for w in length_negative]

        avg_positive = int(sum(map(len, length_positive)) / len(length_positive))
        avg_negative = int(sum(map(len, length_negative)) / len(length_negative))

        ax = fig.add_subplot(122)
        ax.bar('negative', avg_negative)
        ax.text(0, avg_negative + 2, avg_negative)
        ax.bar('positive', avg_positive)
        ax.text(1, avg_positive + 2, avg_positive)
        ax.set_title('Average length of each reviews')

    @staticmethod
    def create_wordclouds(fig, i, sentiment, text):
        wordcloud = WordCloud(max_font_size=50, max_words=100).generate(text)
        ax = fig.add_subplot(2, 2, i)
        ax.imshow(wordcloud)
        ax.title.set_text(f"{sentiment} reviews")
        ax.axis('off')

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

    @staticmethod
    def plot():
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()


def explore_data():
    explorer = DataExplorer('computers')

    # Plot first figure
    # The number of reviews for each sentiment and the average length of each reviews
    fig = plt.figure()
    explorer.review_numbers(fig)
    explorer.review_length(fig)
    explorer.plot()

    # Plot second figure
    # Word cloud of most frequent words and their bar distribution, for both sentiments
    fig = plt.figure()
    for i, sentiment in enumerate(['positive', 'negative'], 1):
        text = explorer.create_text_from_df(sentiment)
        explorer.create_wordclouds(fig, i, sentiment, text)

    for i, sentiment in enumerate([('positive', explorer.positive), ('negative', explorer.negative)], 1):
        explorer.plot_frequency(fig, 2, i, '', sentiment[1])

    fig.suptitle('Words frequency')
    explorer.plot()

    # Plot third figure
    # Frequency of most common words after 'not', for both sentiments
    fig = plt.figure()
    for i, sentiment in enumerate([('positive', explorer.positive), ('negative', explorer.negative)], 1):
        not_freq = []
        for index, word in enumerate(sentiment[1]):
            if word == 'not':
                not_freq.append('not ' + sentiment[1][index + 1])

        explorer.plot_frequency(fig, 1, i, sentiment[0], not_freq)

    fig.suptitle("Most common words after 'not'")
    explorer.plot()
