from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class DataCleaner:
    def __init__(self):
        self.stopwords = self.create_stopwords()

    def clean_data(self, list_to_clean):
        cleaned_list = []

        for element in list_to_clean:
            try:
                tokens = word_tokenize(element)
            except TypeError:
                print(element)

            no_punctuation = [self.keep_text_only(w) for w in tokens]
            lower_case = [w.lower() for w in no_punctuation]
            adjusted = [self.adjust_contractions(w) for w in lower_case]
            stopped = [w for w in adjusted if w not in self.stopwords]
            # stemmed = self.stemming(stopped)
            string = ' '.join(w for w in stopped)
            cleaned_list.append(string)

        return cleaned_list

    @staticmethod
    def stemming(to_stem):
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in to_stem]
        return stemmed

    @staticmethod
    def keep_text_only(text):
        whitelist = string.ascii_letters + ' ' + "'"
        try:
            cleaned_text = ''.join(character for character in text if character in whitelist)
        except TypeError:
            cleaned_text = ''

        return cleaned_text

    @staticmethod
    def convert_grades(grades):
        sentiments = []
        for grade in grades:
            if grade == 5 or grade == 4:
                sentiments.append('positive')
            elif grade == 3:
                sentiments.append('neutral')
            else:
                sentiments.append('negative')
        return sentiments

    @staticmethod
    def adjust_contractions(string):
        string = string.replace("n't", 'not')
        string = string.replace("'m", '')
        string = string.replace("'s", '')

        return string

    @staticmethod
    def create_stopwords():
        white_list = ['not']
        stop_words = set(stopwords.words('english'))
        stop_words = [w for w in stop_words if w not in white_list]
        return stop_words


