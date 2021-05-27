import nltk
from nltk.corpus import stopwords

import text_normalizer

class Preprocessor:
    def __init__(self):
        self.label_text_to_int_mapping = {
            'ham': 0,
            'spam': 1
        }

        try:
            english_stopwords = stopwords.words('english')
        except LookupError:
            nltk.download('stopwords')
            english_stopwords = stopwords.words('english')
        
        self.text_normalizer = text_normalizer.TextNormalizer(stopwords_to_exclude=english_stopwords)

    def preprocess_data(self, source_data, column_mapping):
        data_with_clean_text = self.clean_column_containing_text(
            dataset=source_data,
            column_name=column_mapping['text_column'])
        preprocessed_data = self.normalize_labels(
            dataset=data_with_clean_text,
            column_name=column_mapping['label_column'])
        return preprocessed_data
    
    def clean_column_containing_text(self, dataset, column_name):
        dataset[column_name] = dataset[column_name].apply(lambda row: self.text_normalizer.normalize(row))
        return dataset
    
    def normalize_labels(self, dataset, column_name):
        dataset[column_name] = dataset.get(column_name).map(self.label_text_to_int_mapping)
        return dataset
