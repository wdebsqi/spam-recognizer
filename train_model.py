import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import loader
import preprocessor as pp

class ModelCreator:
    def __init__(self):
        self.source_data = None
        self.loader = loader.Loader()
        self.preprocessor = pp.Preprocessor()
        self.vectorizer = CountVectorizer()
    
    def prepare_data(self):
        self.source_data = self.loader.load_source_data(
            path_to_file='spam.csv')
        self.preprocessed_data = self.preprocessor.preprocess_data(self.source_data)

    def create_model(self):
        inputs = self.preprocessed_data.message
        labels = self.preprocessed_data.label
        X_train, X_test, y_train, self.y_test = train_test_split(inputs, labels, random_state=1)
        X_train_dtm = self.vectorizer.fit_transform(X_train)
        self.X_test_dtm = self.vectorizer.transform(X_test)
        self.nb = MultinomialNB()
        self.nb.fit(X_train_dtm, y_train)
    
    def test_model(self):
        y_pred_class = self.nb.predict(self.X_test_dtm)
        self.acc_score = metrics.accuracy_score(self.y_test, y_pred_class)
        self.confusion_matrix = metrics.confusion_matrix(self.y_test, y_pred_class)
        print(f'Accuracy score: {self.acc_score}')
        print(f'Confusion matrix:\n {self.confusion_matrix}')
    
    def export_model(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.nb, file)

if __name__ == '__main__':
    model_creator = ModelCreator()
    model_creator.prepare_data()
    model_creator.create_model()
    model_creator.test_model()
    model_creator.export_model('model_exported')
    