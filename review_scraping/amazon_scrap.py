from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from review_scraping.create_dataset import DataCreator


REVIEW_URL = ("https://www.amazon.com/product-reviews/{item_id}/ref=acr_dp_hist_5?ie=UTF8&filterByStar="
              "{star}_star&reviewerType=all_reviews#reviews-filter-bar")


class CategoryURL:
    @staticmethod
    def get_url(category):
        if category == 'computers':
            base_url = "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=" \
                       "n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&page={page}&qid=1611406113&rnid=" \
                       "13896617011&ref=sr_pg_{page}"

        if category == 'cellphones':
            base_url = "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=" \
                       "n%3A2811119011%2Cn%3A2407748011&dc&page={page}&qid=1611564523&rnid" \
                       "=2811119011&ref=sr_pg_{page}"
        return base_url


class AmazonScrapper:
    def __init__(self, category, pages):
        self.driver, self.wait = self.configure_driver()
        self.category = category
        self.pages = pages
        self.base_url = CategoryURL.get_url(self.category)
        self.data_handler = DataCreator(self.category)
        self.cache = self.data_handler.set_id

    @staticmethod
    def configure_driver():
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 10)

        return driver, wait

    def navigate_amazon(self):
        for page in range(1, self.pages + 1):
            self.driver.get(self.base_url.format(page=page))

            id_list = []
            for item in range(1, 17):
                try:
                    item_id = self.get_item_id(item)
                except exceptions.NoSuchElementException:
                    continue

                if item_id in self.cache:
                    print(f'item {item_id} already scraped before, skipping.')
                    continue
                id_list.append(item_id)

            print(f"Scraping {len(id_list)} items in page {page} ...")
            for item_id in id_list:
                for counter, star in enumerate(('one', 'two', 'three', 'four', 'five'), 1):
                    if star == 'three':
                        # 3 stars reviews contain to much noise
                        continue
                    self.review_by_star(item_id, counter, star)

                self.data_handler.append_to_cache(item_id)

        self.driver.quit()

    def get_item_id(self, item):
        xpath = f"//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div[{item}]/div/span/div/div/div[2]/ \
                                 div[2]/div/div[1]/div/div/div[1]/h2/a"
        link = self.driver.find_element_by_xpath(xpath).get_attribute('href')
        item_id = link.split('/')[5]
        return item_id

    def review_by_star(self, item_id, counter, star):
        self.driver.get(REVIEW_URL.format(item_id=item_id, star=star))

        html = self.driver.execute_script('return document.body.innerHTML;')
        soup = BeautifulSoup(html, 'html.parser')
        self.data_from_soup(soup, item_id, counter)

    def data_from_soup(self, soup, item_id, counter):

        reviews = soup.find_all('div', class_='a-section review aok-relative')
        for review in reviews:
            title = review.find_all('a', class_="a-size-base a-link-normal review-title "
                                                "a-color-base review-title-content a-text-bold")
            try:
                title = title[0].text
            except IndexError:
                continue

            text = review.find_all('div', class_='a-row a-spacing-small review-data')
            text = text[0].text

            self.data_handler.append_data([self.category, item_id, title, text, counter])
