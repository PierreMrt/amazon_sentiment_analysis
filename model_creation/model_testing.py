import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix

from review_scraping.amazon_scrap import AmazonScrapper
from data_cleaning.data_management import DataManager
from model_creation.model_builder import ModelSelector
from model_creation.model_manager import ModelManager

OUTPUT_PATH = 'model_creation/data/{category}_predictions_output.csv'


class ModelTest:
    def __init__(self, category, model):
        self.category = category

        self.model_selector = ModelSelector
        self.manager = ModelManager(None)
        self.model = self._fetch_model(model)

        self.scrapper = AmazonScrapper(self.category, 2)
        self.clean_df = pd.DataFrame()

    def create_test_dataset(self):
        print(f"Creating test data, scraping {self.category} reviews on Amazon")
        self.scrapper.navigate_amazon()

    def clean_data_set(self):
        data_manager = DataManager(self.category)
        data_manager.initiate_cleaning()
        self.clean_df = data_manager.create_dataframe()
        data_manager.save_dataframe(self.clean_df)

    def test_model(self):
        print('Predicting sentiments')
        reviews = []
        for index, row in self.clean_df.iterrows():
            reviews.append(row['reviews'])

        predictions = []
        for element in reviews:
            text = self.model.transform_text(element)

            predictions.append(self.model.model.predict(text)[0])

        self.save_predictions(predictions)

    def save_predictions(self, predictions):
        self.clean_df['predictions'] = predictions
        self.clean_df.to_csv(OUTPUT_PATH.format(category=self.category))

    def _fetch_model(self, model):
        models = self.manager.load_models()
        model_selected = self.model_selector.selector.get(model)[0]
        for model in models:
            if model.type == model_selected:
                model_selected = model
                continue

        return model_selected


