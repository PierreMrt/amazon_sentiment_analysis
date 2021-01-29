import pandas as pd
from data_cleaning.data_cleaner import DataCleaner

INPUT_PATH = 'review_scraping/data/{category}_raw_output.csv'
OUTPUT_PATH = 'data_cleaning/data/{category}_cleaned_output.csv'


class DataManager:
    def __init__(self, category):
        self.category = category
        self.df = self.open_dataframe()
        self.titles = []
        self.cleaned_titles = []
        self.reviews = []
        self.cleaned_reviews = []
        self.sentiments = []
        self.cleaner = DataCleaner()

    def open_dataframe(self):
        return pd.read_csv(INPUT_PATH.format(category=self.category))

    def save_dataframe(self, df):
        df.to_csv(OUTPUT_PATH.format(category=self.category))
        print(f"Output created in {OUTPUT_PATH.format(category=self.category)}")

    def create_lists(self):
        for index, row in self.df.iterrows():
            self.titles.append(row['titles'])
            self.reviews.append(row['reviews'])
            self.sentiments.append(row['grades'])

    def initiate_cleaning(self):
        self.df = self.df.dropna()
        self.df = self.df.drop(self.df[self.df.grades == 3].index)
        self.create_lists()

        print('cleaning titles')
        self.cleaned_titles = self.cleaner.clean_data(self.titles)

        print('cleaning reviews')
        self.cleaned_reviews = self.cleaner.clean_data(self.reviews)

        self.sentiments = self.cleaner.convert_grades(self.sentiments)

    def create_dataframe(self):
        new_df = pd.DataFrame(columns=['category', 'ID', 'titles', 'reviews', 'sentiment'])

        for col in ['category', 'ID']:
            new_df[col] = self.df[col]

        new_df['titles'] = self.cleaned_titles
        new_df['reviews'] = self.cleaned_reviews
        new_df['sentiment'] = self.sentiments

        return new_df


