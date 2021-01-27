import pickle

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



