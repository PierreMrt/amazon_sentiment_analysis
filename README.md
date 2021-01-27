[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:merlet.pierre@outlook.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

:yellow_circle: work in progress

# Amazon_sentiment_analysis
Full sentiment analysis project, based on Amazon reviews. Training of machine learning models to be able to detect the positive or negative sentiment of a review.

The project is done in 6 parts:

1. Scraping reviews from Amazon to create a dataset
2. Cleaning of the dataset and preparation for model training
3. Exploratory analysis of the scraped reviews
4. Machine learning model creation and training
5. Model testing against new reviews
6. Analysis of the results

### Business case
A company needs to know what its customers think about their products in order to asses their level of satisfaction. Internet provides a place for customers to express themselves, positively but also negatively. If the number of reviews is small, the analysis of the customers' satisfaction might be doable manually. But what if it it not the case and we have hundred or thousand of reviews?

That is where machine learning intervenes. 

The idea is to classify reviews based on their general sentiment - negative or positive. For this, we need to train Machine Learning (ML) algorithms through supervised training and Natural Language Processing (NLP) techniques. We first create a dataset of review for which we already know the general sentiment (4 to 5 stars - positive, 1 or 2 stars - negative) and then train our ML models against these scores. We are then able to extrapolate this results and can assess the sentiment of a review for which we don't have a score!

For this example, let's say that we are an online seller of electronic equipement and that we want to see what our customers say about us on social medias, on our website, ... Any platforms on internet where the customer cannot leave a rating, and thus forbid us to directly assess the satisfaction level. 

### Reviews scraping
The first part is to create a dataset for which we already have labels (rating). 

Here we scraped the first 100 pages of items in the computers category of Amazon. For each of these items, we fetch the first 10 reviews of each stars, which allows us to create a dataset of almost 20 000 different reviews.

[More details here.](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/review_scraping)

### Data cleaning
Once we have a large dataset, the next part is to clean it. Indeed when we work with NLP it is important to have normalized data. The main steps are as follow:
1. Tokenize the text
2. Remove punctuation and other special characters
3. Normalize the case (evry words need to be in lower case)
4. Remove stop words

[More details here.](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/data_cleaning)

### Data exploration
This part is about understanding our dataset and identify potential trends in it, in order choose the best parameters for our ML classifiers.

[More details here.](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization)

### Models creation and testing
We train 6 different ML classifiers with scikit learn:
* logistic regression
* decision tree
* random forest
* passive agressive
* support vector
* naive bayes

Based on the preliminary results, we can then test our best model against new data, to check how it would behave in a real scenario.

[More details here.](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/model_creation)

### Results analysis
How did each the 6 models fared ? Which one performed the best ?

[See the results here.](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization)

### Utilisation
To Launch the initial scraping: 
`python main.py scraping`

To clean the results:
`python main.py cleaning`

To view the data analysis:
`python main.py data_exploration`

To create the classifiers:
`python main.py create_models`

To test one of the model:
`python main.py test_model`

To view the results analysis:
`python main.py analyze_results`

### Requirements


### License

>MIT License
>
>Copyright (c) 2021 Pierre Merlet
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.

