from review_scraping.amazon_scrap import AmazonScrapper
from data_cleaning.data_management import DataManager
from model_creation.model_manager import ModelManager
from model_creation.model_builder import ModelBuilder
from model_creation.model_testing import ModelTest
from analysis_and_visualization.data_exploration import explore_data


def scraping():
    scrapper = AmazonScrapper('computers', 100)
    scrapper.navigate_amazon()


def cleaning():
    data_manager = DataManager('computers')
    data_manager.initiate_cleaning()
    new_df = data_manager.create_dataframe()
    data_manager.save_dataframe(new_df)


def create_models():
    models = ModelBuilder('computers').build_models()
    manager = ModelManager(models)
    manager.save_model()


def test_model():
    model_selected = '-support_vector'
    tester = ModelTest('cellphones', model_selected)
    # tester.create_test_dataset()
    tester.clean_data_set()
    tester.test_model()


def data_exploration():
    explore_data()


def analyze_results():
    pass