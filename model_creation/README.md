[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:merlet.pierre@outlook.com)

# Building and training the classifiers
Using scikit-learn libraries to create different classification models, able to determine the overall sentiment of a 
text (positive or negative).


### Models:
* logistic regression
* decision tree
* random forest
* passive aggressive
* support vector
* naive bayes

### Building:
* Initializing a TfidfVectorizer
 
    `parameters: max_df=0.7, ngram_range=(1, 2)`

As we saw during the exploratory analysis, it important to clear the words that appear too often in both sentiments, such as 'computer', 'laptop' etc.. 
That's why 0.7 is a good parameter for the max_df. It means that words that appear in 70% or more of the reviews won't be taken into consideration by the vectorizer. 

Moreover, we saw that the negations were quite important to get the meaning of a sentence, and this is the reason for a ngram range of 1 to 2. This way the vectorizer 
will also look at the word sequence, vectorizing up to 2 words together and thus, not loosing the meaning of the negations. 

* Separating training and testing data

    `parameters: test_size=0.2, random_state=7`

80% of the reviews being used as a training set, and therefore 20% for testing the models, is a good balance between letting a lot of data for the algorithms to train,
 without overfitting our models. 

Secondly, a random state of 7 allows to remove the randomness of this separation, to be able to run this multiple times and reproduce the same results. 

* Fit and transform training set

* Transform testing set

* For each model:
    1. Fit the model against the expected sentiment using the transformed training set
    2. Predict the sentiments of the testing set
    3. Check the results using the accuracy and confusion matrix
    
* Save the models so they can be used later

### Testing the most promising model:

* Create a new data set scraping the reviews of the category "cellphones" on Amazon (first 2 pages of articles). 
* Clean this new dataset
* Using the model to guess the sentiment of the reviews
* Saving the new dataframe into: `model_creation/data/cellphones_predictions_output.csv`
* Compare the predictions against the "true" sentiment of the reviews (1 and 2 stars = negative, 4 and 5 positive).


### Results:

[Find out how each model performed, check the results here !](
https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization#results-of-the-models)

### Utilisation:
From the Amazon_sentiment_analysis folder: `python main.py create_models`
