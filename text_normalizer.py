import re

class TextNormalizer:
    def __init__(self, stopwords_to_exclude=None):
        self.stopwords_to_exclude = stopwords_to_exclude

    def normalize(self, original_text):
        lowered_text = self.tranform_to_lowercase(original_text)
        
        alphanumeric_text = self.remove_non_alphanumeric_chars(lowered_text)
        
        text_with_correct_whitespaces = self.remove_redundant_whitespaces(alphanumeric_text)

        fully_normalized_text = self.remove_stopwords(text_with_correct_whitespaces)
    
        return fully_normalized_text
    
    def transform_to_lowercase(self, text):
        return text.lower()
    
    def remove_non_alphanumeric_chars(self, text):
        return re.sub(r'[^\d\w\s]', '', text)
    
    def remove_redundant_whitespaces(self, text):
        return ' '.join([word for word in text.split() if word != ' '])
    
    def remove_stopwords(self, text):
        stop = stopwords.words('english')
        return ' '.join([word for word in text.split() if word not in stop])
