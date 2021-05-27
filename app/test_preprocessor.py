import pandas as pd
import unittest

import preprocessor


class TestPreprocessor(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        
        self.preprocessor = preprocessor.Preprocessor()
        column_names = ['label', 'text']
        data_to_process = {
            'label':  ['ham', 'ham', 'spam'],
            'text': ['Not normalized   #$text', '   AnOthEr not normalized TEXT', 'Not normalized     SPAM'],
        }
        self.dataset_to_process = pd.DataFrame (data_to_process, columns=column_names)

        correct_data = {
            'label':  [0, 0, 1],
            'text': ['normalized text', 'another normalized text', 'normalized spam'],
        }
        self.correct_dataset = pd.DataFrame(correct_data, columns=column_names)
        
    def test_clean_column_containing_text(self):
        dataset_to_process = self.dataset_to_process.copy(deep=True)
        transformed_dataset = self.preprocessor.clean_column_containing_text(
            dataset=dataset_to_process,
            column_name='text')
        transformed_column_values = transformed_dataset['text'].tolist()
        correct_column_values = self.correct_dataset['text'].tolist()
        self.assertListEqual(transformed_column_values, correct_column_values)
    
    def test_normalize_labels(self):
        dataset_to_process = self.dataset_to_process.copy(deep=True)
        transformed_dataset = self.preprocessor.normalize_labels(
            dataset=dataset_to_process,
            column_name='label')

        transformed_column_values = transformed_dataset['label'].tolist()
        correct_column_values = self.correct_dataset['label'].tolist()

        self.assertListEqual(transformed_column_values, correct_column_values)
    
    def test_preprocess_data(self):
        dataset_to_process = self.dataset_to_process.copy(deep=True)
        transformed_dataset = self.preprocessor.preprocess_data(
            source_data=dataset_to_process,
            column_mapping={'text_column': 'text', 'label_column': 'label'})
        transformed_label_values = transformed_dataset['label'].tolist()
        transformed_text_values = transformed_dataset['text'].tolist()
        correct_label_values = self.correct_dataset['label'].tolist()
        correct_text_values = self.correct_dataset['text'].tolist()

        self.assertListEqual(transformed_label_values, correct_label_values)
        self.assertListEqual(transformed_text_values, correct_text_values)
    

if __name__ == '__main__':
    unittest.main()
