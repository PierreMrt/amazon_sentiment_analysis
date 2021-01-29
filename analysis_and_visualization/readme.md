[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:merlet.pierre@outlook.com)

# Data exploration and classifier analysis

First part is about analyzing the cleaned version of the reviews scraped from Amazon, second is about analyzing the 
results obtained through the training of the different machine learning classifiers.

1. [Data exploration](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization#data-exploration)
2. [Results analysis](https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization#results-of-the-models)

### Data exploration
1. analysis of review numbers
2. sentiment wordclouds and word frequency
3. most frequent words after a negation 

##### Review numbers:
![Figure_1](https://user-images.githubusercontent.com/69766734/106306773-c9fa3d00-625e-11eb-9751-4cdf769f440a.png)

The data set is built upon a total of 18 542 reviews, of which around 60% are positive. This provides a good equilibrium between both sentiments, which will allows the ML classifiers to strike a good balance and avoiding bias towards one sentiment.

From the second graph, we can see that the average length of the positive reviews are generally a bit longer (Intuituively I would have said the opposite). However the difference is not enough to impact the predictions, possitively or negatively. 

##### Word frequency:
![Figure_2](https://user-images.githubusercontent.com/69766734/106306767-c8c91000-625e-11eb-9170-137db61347d2.png)
Without surprise, the words related to the computer category directly caught the eyes, such as screen, laptop, computer, chromebook... We can also see that positive words such as great or good appear in both category as well as negative ones, like problem.

However, if we look a bit more at the frequency of these words, we can see for example that good or great are much more present in the positive reviews. We still need to take this into consideration when building the models and remove the words that appear too much in both type of reviews.

As the negations were all normalized into 'not', it is not surprising to see it as the top word for each category. But let's dive a bit deeper into what it means.

##### Word frequency following a negation:
![Figure_3](https://user-images.githubusercontent.com/69766734/106306772-c9fa3d00-625e-11eb-8c20-52435331acf7.png)

From this figure we can see that the meaning of these two words sentences express much stronger feeling for the negative reviews. Indeed, even if 'not sure', 'not really' or even 'not like' and 'not work' are not exactly positive, 'not buy', 'not even' and 'not clearer' are more clearer about the sentiment of the review. We can also see that the laters are much  more frequent.

This means that the negation are important and that it was correct to remove them from the sop words while cleaning the data and keeping them. However, we need to take this parameter in consideration when building the models and that is why we will use a n_gram range of 1 to 2, meaning that we will look at each word separately, but also in batch of 2.

___________________

### Results of the models

to do




