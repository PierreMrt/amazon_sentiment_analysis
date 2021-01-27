[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/PierreMrt/ama)

# Amazon reviews scraping

In order to create the labelized dataset which will be used to create supervised learning models, the first 100 pages of the 'computers' category on Amazon were scraped.

On each page, there are around 16 articles, and for each article we fetched around 10 reviews per stars. The 3 stars reviews were skipped, as after a first analysis, it was noted that they provided too much noise and were actually not really indicative of a neutral review. Indeed, more often that not, they contained either a positive or a negative sentiment and thus did not provide added value for the training of the models.

______________
The scraping results in a dataset of almost 20 000 reviews and can therefore take a large amount of time to be executed. It took indeed around 1h with an average internet connection. That is because even though the number of html requests was reduced to the minimum needed, I still had to use Selenium instead of Requests as the pages contain a lot of javascript elements. Still, that is around 5 reviews per second.

______________
So what if anything problematic happens during this time ? (internet loss, sudden captcha request from Amazon, etc..)

The solution was to directly write the reviews in the .csv file immediately after getting them. All the scraped items are also put in a cache file, allowing to skip them if there is a need to start the scraping again. In this case the scraping will automatically restart from where it was, saving significant time in case of problems.

_______________
If the url of the page is provided, any category could potentially be scraped, as it is demonstrated by the scraping of the cellphones category, which is later used to test our models against an untrained for dataset.

### Utilisation:
From the Amazon_sentiment_analysis folder:
`python main.py scraping`
