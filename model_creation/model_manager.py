import pickle

from data_cleaning.data_cleaner import DataCleaner

INPUT_PATH = 'model_creation/data/models'


class ModelManager:
    def __init__(self, models):
        self.models = models
        self.existing_models = []

    def save_model(self):
        pickle.dump(self.models, open(INPUT_PATH, 'wb+'))

    def load_models(self):
        try:
            self.existing_models = pickle.load(open(INPUT_PATH, 'rb'))
        except FileNotFoundError:
            print('No model was found. Please create them first.\n'
                  'python main.py create_models')
        return self.existing_models


class Model:
    def __init__(self, name, tfidf_vectorizer):
        self.name = name
        self.score = 0
        self.confusion_matrix = None

        self.model = None
        self.tfidf_vectorizer = tfidf_vectorizer

        self.test_matrix = None
        self.test_score = 0

    def transform_text(self, text):
        text = [text]
        tfidf_text = self.tfidf_vectorizer.transform(text)
        return tfidf_text
