from review_scraping.amazon_scrap import AmazonScrapper
from data_cleaning.data_management import DataManager
from model_creation.model_manager import ModelManager
from model_creation.model_builder import ModelBuilder
from model_creation.model_testing import ModelTest
from analysis_and_visualization.data_exploration import explore_data


TRAINING_CATEGORY = 'computers'
TESTING_CATEGORY = 'cellphones'
TESTED_MODEL = 'support_vector'


def scraping():
    scrapper = AmazonScrapper(TRAINING_CATEGORY, 100)
    scrapper.navigate_amazon()


def cleaning():
    data_manager = DataManager(TRAINING_CATEGORY)
    data_manager.initiate_cleaning()
    new_df = data_manager.create_dataframe()
    data_manager.save_dataframe(new_df)


def create_models():
    models = ModelBuilder(TRAINING_CATEGORY).build_models()
    manager = ModelManager(models)
    manager.save_model()


def test_model():
    tester = ModelTest(TESTING_CATEGORY, TESTED_MODEL)
    # tester.create_test_dataset()
    tester.clean_data_set()
    tester.test_model()


def data_exploration():
    explore_data()


def analyze_results():
    pass
