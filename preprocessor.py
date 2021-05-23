import re
from nltk.corpus import stopwords

class Preprocessor:
    def __init__(self):
        self.label_text_to_int_mapping = {
            'ham': 0,
            'spam': 1
        }
    def preprocess_data(self, source_data):
        data_with_clean_text = self.clean_column_containing_text(
            dataset=source_data,
            column_name='message')
        preprocessed_data = self.normalize_labels(
            dataset=data_with_clean_text,
            column_name='label')
        return preprocessed_data
    
    def clean_column_containing_text(self, dataset, column_name):
        dataset[column_name] = dataset[column_name].apply(lambda row: self._text_cleanup(row))
        return dataset
    
    def _text_cleanup(self, original_text):
        
        # 1. Original to lowercase
        lower_text = original_text.lower()
        
        # 2. Remove all non-alphanumeric characters
        alphanumeric_text = re.sub(r'[^\d\w\s]', '', lower_text)
        
        # 3. Remove redundant whitespaces.
        whitespaces = ' '.join([word for word in alphanumeric_text.split() if word != ' '])
        
        # 4. Remove stopwords
        stop = stopwords.words('english')
        without_stopwords = ' '.join([word for word in whitespaces.split() if word not in stop])
        
        return without_stopwords
    
    def normalize_labels(self, dataset, column_name):
        dataset[column_name] = dataset.get(column_name).map(self.label_text_to_int_mapping)
        return dataset