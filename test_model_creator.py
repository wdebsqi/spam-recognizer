import unittest

import train_model as tm


class TestModelCreator(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.model_creator = tm.ModelCreator()

        self.model_creator.prepare_data()
        self.source_data = self.model_creator.source_data

        self.model_creator.create_model()

        self.model_creator.test_model()
        self.accuracy = self.model_creator.acc_score
        
    def test_source_data_count(self):
        self.assertGreater(
            self.source_data.count()[0], 
            100, 
            "Should be greater than 100")
    def test_source_data_label_values(self):
        labels = list(self.source_data.label.unique())
        self.assertListEqual(labels, ['ham', 'spam'])
    
    def test_accuracy(self):
        self.assertGreater(self.accuracy, 0.9, 'Should be greater than 0.9')

if __name__ == '__main__':
    unittest.main()
    