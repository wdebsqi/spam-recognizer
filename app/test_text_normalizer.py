import unittest
import nltk
from nltk.corpus import stopwords

import text_normalizer


class TestTextNormalizer(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        try:
            english_stopwords = stopwords.words('english')
        except LookupError:
            nltk.download('stopwords')
            english_stopwords = stopwords.words('english')
        
        self.text_normalizer = text_normalizer.TextNormalizer(
            stopwords_to_exclude=english_stopwords)
        
    def test_transform_to_lowercase(self):
        correct_text = 'this is a normal text'
        original_text = 'ThIs IS a nOrmAl TEXT'
        transformed_text = self.text_normalizer.transform_to_lowercase(original_text)
        self.assertEqual(transformed_text, correct_text)
    
    def test_remove_non_alphanumeric_chars(self):
        correct_text = '123 This is a normal text'
        original_text = '!@#123!@# $%^Th&&is* is(()) a normal text.++'
        transformed_text = self.text_normalizer.remove_non_alphanumeric_chars(original_text)
        self.assertEqual(transformed_text, correct_text)
    
    def test_remove_redundant_whitespaces(self):
        correct_text = '123 This is a normal text'
        original_text = '       123   This    is a normal  text '
        transformed_text = self.text_normalizer.remove_redundant_whitespaces(original_text)
        self.assertEqual(transformed_text, correct_text)
    
    def test_remove_stopwords(self):
        correct_text = '123 normal text'
        original_text = 'i 123 you this does is between a the normal very text'
        transformed_text = self.text_normalizer.remove_stopwords(original_text)
        self.assertEqual(transformed_text, correct_text)
    
    def test_normalize(self):
        correct_text = '123 normal text'
        original_text = 'i      !@#123$%^^& you ThIs does is(()) #   #  BETWEen a the noRMal very text.++'
        transformed_text = self.text_normalizer.normalize(original_text)
        self.assertEqual(transformed_text, correct_text)

if __name__ == '__main__':
    unittest.main()
