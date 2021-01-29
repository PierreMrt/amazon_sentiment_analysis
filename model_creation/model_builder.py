import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score

from model_creation.model_manager import Model


INPUT_PATH = 'data_cleaning/data/{category}_cleaned_output.csv'


class ModelSelector:
    selector = {
        'logistic_regression': (LogisticRegression(max_iter=200)),
        'decision_tree': (DecisionTreeClassifier()),
        'random_forest': (RandomForestClassifier()),
        'passive_aggressive': (PassiveAggressiveClassifier()),
        'support_vector': (SGDClassifier()),
        'naive_bayes': (MultinomialNB()),
    }


class ModelBuilder:
    def __init__(self, category):
        self.category = category
        self.models = []
        self.tfidf_vectorizer = TfidfVectorizer(max_df=0.7, ngram_range=(1, 2))
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

    def prepare_data(self):
        data_set = self.open_dataset()
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(data_set['reviews'],
                                                                                data_set['sentiment'],
                                                                                test_size=0.2, random_state=7)

        tfidf_train = self.fit_and_transform_train_set(self.x_train)
        tfidf_test = self.transform_test(self.x_test)

        return tfidf_train, tfidf_test

    def build_models(self):
        tfidf_train, tfidf_test = self.prepare_data()

        for model_type in ModelSelector.selector:
            name = model_type
            model_type = ModelSelector.selector[model_type]
            model = Model(name, self.tfidf_vectorizer)
            model.model = model_type.fit(tfidf_train, self.y_train)

            y_pred = model.model.predict(tfidf_test)
            model.score = accuracy_score(self.y_test, y_pred)
            model.confusion_matrix = confusion_matrix(self.y_test, y_pred)

            self.models.append(model)
            self.print_results(model)

        return self.models

    def fit_and_transform_train_set(self, x_train):

        return self.tfidf_vectorizer.fit_transform(x_train.values.astype('U'))

    def transform_test(self, x_test):
        return self.tfidf_vectorizer.transform(x_test.values.astype('U'))

    @staticmethod
    def print_results(model):
        print(f"Model built. \n"
              f"Accuracy of {model.name}: {round(model.score * 100, 2)}%\n\n"
              f"Confusion matrix:\n{model.confusion_matrix}\n")
        print('*' * 50)

    def open_dataset(self):
        return pd.read_csv(INPUT_PATH.format(category=self.category))





