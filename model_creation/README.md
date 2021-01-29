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

* Separating training and testing data

    `parameters: test_size=0.2, random_state=7`

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

[Find out which model was selected and check the results here !](
https://github.com/PierreMrt/Amazon_sentiment_analysis/tree/main/analysis_and_visualization)

### Utilisation:
From the Amazon_sentiment_analysis folder: `python main.py create_models`