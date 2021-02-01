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

##### First results:
Here are the results of the classifiers, from worst to best:
This objective is obvisouly to have the highest accuracy score possible, but not only. As a company, it's always a good feeling to have positive reviews, but if we want to understand our weaknesses we need to focus on the negative reviews and as such, we want as few false negative as possible (we don't want to misinterpret a negative review as a positive one).

* Decision tree:

This model classified the correct sentiment around 78% of the time. The confusion matrix can give us a deeper understanding of the results:

Out the the 1428 negative reviews in the testing set, the model classified 403 of them as positive, or a 28% of false negative. 

![decision_tree_training](https://user-images.githubusercontent.com/69766734/106483757-2a7fb900-64af-11eb-9da0-5ddf0b0df50a.png)

* Naive Bayes:

The overall accuracy of the Naive Bayes method is slighty better, but even if the number of false positive is really low (1.4% only !), the false negative represent 53% of the negative reviews, which makes it not worth at all to use this model alone.

![naive_bayes_training](https://user-images.githubusercontent.com/69766734/106483759-2b184f80-64af-11eb-99ff-f6a2c36a5cf1.png)

* Random Forest:

87% accuracy, but still too much false negative (24%).
![random_forest_training](https://user-images.githubusercontent.com/69766734/106483752-294e8c00-64af-11eb-9ccb-f7844d4b9b14.png)

Logistic Regression:

89% of accuracy, 17% of false positives.

![logistic_regression_training](https://user-images.githubusercontent.com/69766734/106483758-2a7fb900-64af-11eb-95b0-3167c8575350.png)

Passive Aggressive:

90.3% of accuracy, and 12.7% of false negatives. Much better !

![passive_aggressive_training](https://user-images.githubusercontent.com/69766734/106483750-28b5f580-64af-11eb-88c3-a862f6f4cce3.png)

Support Vector:
90.7% accuracy, and 13.2% of false negatives.
![support_vector_training](https://user-images.githubusercontent.com/69766734/106483755-29e72280-64af-11eb-99c2-d8d8ca3b5bad.png)

Clearly, the two best classifiers are therefore the passive aggressive method and the support vector, with the later having slightly more false negative but an overall better accuracy. Let's see how these two models perform outside of our training set.

##### Testing against new data:

* Support vector:

With only 63 false positive out of 462 negative reviews, this model performed really well outside of the training set, with an overall accuracy of 85.8% !

![support_vector_test](https://user-images.githubusercontent.com/69766734/106483753-29e72280-64af-11eb-9425-1408675952ca.png)

* Passive aggressive:

While still showing correct results, this classifier only get the second place when testing the models against reviews of a different category.

![passive_aggressive_test](https://user-images.githubusercontent.com/69766734/106483747-28b5f580-64af-11eb-9ca4-fa1fb341e438.png)

##### Conclusion:

The support vector model showed the best results out of all the model tested, being the most accurate overall and resulting in the least number of false negatives.

We trained these classifiers on a category and tested them on a different one to show that the process can be generalized. However, in order to have better results, it could be possible to train the model on the category where the company is competing. 

On the other hand, it could also be possible to train the models on multiple categories, increasing the width of this tool and potentially improve the performance across all these categories.

Another solution to further improve the performances would be to use multiple classifiers at the same time and choose the best one for each reviews.







