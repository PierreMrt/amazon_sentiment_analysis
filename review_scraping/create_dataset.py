import csv
import pickle

OUTPUT_PATH = 'review_scraping/data/{category}_raw_output.csv'
CACHED_PATH = 'review_scraping/data/{category}_cache'


class DataCreator:
    def __init__(self, category):
        self.headers = ['category', 'ID', 'titles', 'reviews', 'grades']
        self.category = category

        self.set_id = self.cached_id()
        if len(self.set_id) == 0:
            self.create_headers()

    def append_data(self, row):
        with open(OUTPUT_PATH.format(category=self.category), 'a+', newline='', encoding='utf8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(i for i in row)

    def create_headers(self):
        with open(OUTPUT_PATH.format(category=self.category), 'a+', newline='') as f:
            writer = csv.DictWriter(f, delimiter=",", fieldnames=self.headers)
            writer.writeheader()

    def cached_id(self):
        try:
            cached_id = pickle.load(open(CACHED_PATH.format(category=self.category), 'rb'))
        except FileNotFoundError:
            cached_id = set()
        return cached_id

    def append_to_cache(self, item_id):
        self.set_id.add(item_id)
        pickle.dump(self.set_id, open(CACHED_PATH.format(category=self.category), 'wb'))
