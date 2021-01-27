[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:merlet.pierre@outlook.com)

# Data cleaning
In order to analyze the data obtained and train our models, we need to clean and 
uniformize the reviews. 

Using nltk, a Natural Language Processing (NLP) library.

### Steps:
1. Tokenize the reviews using nltk: transform the text into a list of words
2. Remove the punctuation, numbers and other special characters. In other words, 
keep only the alphabetic characters
3. Uniformize all the elements into lower case characters
4. Adjust contractions. To understand the meaning of a sentence, it is important 
to keep the negations. Change all instances of "doesn't", "shouldn't", ... into two 
words: the base word + not
5. Remove the most frequent words of the english language using a custom version of the 
nltk corpus of stopwords (ie: cutting "not" from the list of words to remove).
6. It is also be possible to stem or lemmatize the words, bringing them to their very roots 
(ie: happy, happily > happi). However, it did not produce improvements in the model training and only made the data 
exploration less readable.

7. Save the cleaned reviews and titles in a new data frame: `data_cleaning/data/cleaned_output`

### Utilisation:

From the Amazon_sentiment_analysis folder: `python main.py cleaning`