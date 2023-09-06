# Corpus pre-processing
from nltk.corpus import stopwords
import unicodedata
import nltk
import chardet
nltk.download('stopwords')

class Corpus_preprocessing:
    """
    A class that aims to pre-process the corpus entry.

    This class is responsable to convert the text to Lower-Case format, remove punctuation, remove stopwords and more...
    """
    def __init__(self, text):
        """
        Initializes a Corpus_preprocessing with a given text.

        Parameters:
        - text: The text to be pre-processed.

        """
        self.text = text
        self.words = []
        self.full_preprocessing()
    

    def full_preprocessing(self):
        """
        Applies all the pre-processing methods to the text.
        """
        self.to_lower_case()
        self.remove_punctuation()
        self.text_to_words()
        self.remove_stopwords()
        self.remove_accents()
        self.check_repeated_words()

    def to_lower_case(self):
        """
        Converts the text to lower-case format.
        """
        self.text = self.text.lower()

    def remove_punctuation(self):
        """
        Removes punctuation from the text.
        """
        list_punctuation = [".", ",", "!", "?", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "'", '"']
        # Remove punctuation if there is any in the text
        for punctuation in list_punctuation:
            if punctuation in self.text:
                self.text = self.text.replace(punctuation, "")


    # remove accents in two steps
    def _accents_processer(self, word):
        normalized_word = unicodedata.normalize('NFKD', word)
        return ''.join([c if not unicodedata.combining(c) else '' for c in normalized_word])
                
    def remove_accents(self):
        """
        Removes accents from the text.
        """
        # Remove accents if there is any in the text
        self.words = [self._accents_processer(word) for word in self.words]

    # transform text into a list of words
    def text_to_words(self):
        """
        Converts the text to a list of words.
        """
        self.words = self.text.split()

    # remove stopwords
    def remove_stopwords(self):
        """
        Removes stopwords from the text.
        """
        # Remove stopwords if there is any in the text
        stop_words = set(stopwords.words('portuguese'))
        self.words = [word for word in self.words if word not in stop_words]

    def check_repeated_words(self):
        self.words = list(set(self.words))



def read_file_corpus(file_path):
    """
    Reads txt file, as corpus, and returns its content.
    """

    # Use chardet to detect the encoding
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())

    # The 'result' output will contain information about the encoding
    detected_encoding = result['encoding']

    # Read the file with the detected encoding
    with open(file_path, 'r', encoding=detected_encoding) as corpus_file:
        text = corpus_file.read()

    return text