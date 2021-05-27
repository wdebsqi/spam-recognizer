import unittest

import preprocessor


class TestPreprocessor(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        
        self.preprocessor = preprocessor.Preprocessor()
        
    def test_clean_column_containing_text(self):
        correct_text = 'this is a normal text'
        original_text = 'ThIs IS a nOrmAl TEXT'
        transformed_text = self.text_normalizer.transform_to_lowercase(original_text)
        self.assertEqual(transformed_text, correct_text)
    
    def test_normalize_labels(self):
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
